"""Laurisverse : l'univers 3D de mes notes Obsidian.

Lit toutes les notes .md du coffre, en extrait : dossier, type, tags, date,
longueur et liens [[...]], puis fabrique une page laurisverse.html
(dans le dossier Outil) et l'ouvre dans le navigateur.
Lit aussi les fiches d'agents (dossier « 10 - Agents ») pour la vue Organigramme,
et recense les leçons du coffre et les épisodes du podcast.

Lancement : double-clic sur Lancer-Laurisverse.bat, ou  py laurisverse.py
Options   : py laurisverse.py --coffre "C:\\chemin\\vers\\un\\autre\\coffre"
            py laurisverse.py --sans-ouvrir      (tâche planifiée : met à jour en silence)
La voix automatique a été retirée (choix de Lauris) : le bouton « Écouter » de la page reste.
"""

import argparse
import json
import os
import re
import unicodedata
import webbrowser
from datetime import date, datetime
from pathlib import Path

ICI = Path(__file__).resolve().parent
COFFRE_PAR_DEFAUT = ICI.parent           # Outil est rangé dans le coffre
MODELE = ICI / "laurisverse_modele.html"
ORGANIGRAMME = ICI / "laurisverse_organigramme.html"   # vue Organigramme, ajoutée à la page
SORTIE = ICI / "laurisverse.html"

DOSSIERS_IGNORES = {".obsidian", ".trash", "__pycache__", ".git", "Templates", "Modèles"}

RE_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(\n|\Z)", re.S)
RE_LIEN = re.compile(r"(?<!!)\[\[([^\]\|#\^]+)(?:[#\^][^\]\|]*)?(?:\|[^\]]*)?\]\]")
RE_TAG = re.compile(r"(?:^|\s)#([A-Za-zÀ-ÿ0-9_\-/]+)")
RE_DATE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
RE_TITRE = re.compile(r"^#\s+(.+)$", re.M)
RE_CODE = re.compile(r"```.*?```", re.S)
RE_TACHE = re.compile(r"^\s*[-*] \[( |x|X)\]\s+(.+)$")
RE_SECTION = re.compile(r"^#{2,4}\s+(.+)$")


def texte_parle(t):
    """Nettoie un texte Markdown pour qu'il soit lisible à voix haute."""
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)   # [[note|alias]] -> alias
    t = re.sub(r"\[\[([^\]]+)\]\]", r"\1", t)               # [[note]] -> note
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)           # [texte](lien) -> texte
    t = re.sub(r"[*_`#>]", "", t)
    t = re.sub(r"[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F]", "", t)  # emojis
    return re.sub(r"\s+", " ", t).strip()


def lire_taches(corps):
    """Cases à cocher de la note : [{texte, section}] pour celles à faire, + nombre de cases cochées."""
    a_faire, faites, section = [], 0, ""
    for ligne in corps.splitlines():
        m = RE_SECTION.match(ligne)
        if m:
            section = texte_parle(m.group(1))
            continue
        m = RE_TACHE.match(ligne)
        if not m:
            continue
        if m.group(1) == " ":
            a_faire.append({"texte": texte_parle(m.group(2)), "section": section})
        else:
            faites += 1
    return a_faire[:40], faites


def lire_frontmatter(texte):
    """Lecture simple du bloc --- en haut de la note (clé: valeur, listes)."""
    m = RE_FRONTMATTER.match(texte)
    if not m:
        return {}, texte
    meta, cle_liste = {}, None
    for ligne in m.group(1).splitlines():
        if not ligne.strip():
            continue
        if ligne.lstrip().startswith("- ") and cle_liste:
            meta.setdefault(cle_liste, [])
            if isinstance(meta[cle_liste], list):
                meta[cle_liste].append(ligne.strip()[2:].strip().strip("\"'"))
            continue
        if ":" in ligne and not ligne.startswith(" "):
            cle, valeur = ligne.split(":", 1)
            cle, valeur = cle.strip().lower(), valeur.strip()
            if valeur == "":
                meta[cle] = []
                cle_liste = cle
            else:
                cle_liste = None
                if valeur.startswith("[") and valeur.endswith("]"):
                    meta[cle] = [v.strip().strip("\"'") for v in valeur[1:-1].split(",") if v.strip()]
                else:
                    meta[cle] = valeur.strip("\"'")
    return meta, texte[m.end():]


def trouver_date(meta, nom):
    for cle in ("date", "created", "cree", "créé", "creation"):
        v = meta.get(cle)
        if isinstance(v, str):
            m = RE_DATE.search(v)
            if m:
                return m.group(0)
    m = RE_DATE.search(nom)
    if m:
        try:
            date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            return m.group(0)
        except ValueError:
            pass
    return None


def lire_coffre(coffre: Path):
    notes = []
    for racine, dossiers, fichiers in os.walk(coffre):
        dossiers[:] = sorted(d for d in dossiers if d not in DOSSIERS_IGNORES and not d.startswith("."))
        for f in sorted(fichiers):
            if not f.lower().endswith(".md"):
                continue
            chemin = Path(racine) / f
            rel = chemin.relative_to(coffre)
            try:
                texte = chemin.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            meta, corps = lire_frontmatter(texte)
            corps_sans_code = RE_CODE.sub(" ", corps)

            tags = meta.get("tags") or meta.get("tag") or []
            if isinstance(tags, str):
                tags = [t for t in re.split(r"[,\s]+", tags) if t]
            tags = {t.lstrip("#") for t in tags}
            tags |= set(RE_TAG.findall(corps_sans_code))

            titre = RE_TITRE.search(corps)
            titre = titre.group(1).strip() if titre else chemin.stem
            dossier = rel.parts[0] if len(rel.parts) > 1 else "(racine)"
            taches, faites = lire_taches(corps_sans_code)
            try:
                semaine = int(str(meta.get("semaine", "")).strip())
            except ValueError:
                semaine = None

            notes.append({
                "id": len(notes),
                "nom": chemin.stem,
                "titre": titre,
                "chemin": rel.as_posix(),
                "dossier": dossier,
                "type": str(meta.get("type") or "") or None,
                "tags": sorted(tags),
                "date": trouver_date(meta, chemin.stem),
                "modif": datetime.fromtimestamp(chemin.stat().st_mtime).strftime("%Y-%m-%d"),
                "mots": len(corps_sans_code.split()),
                "_liens": [l.strip().rstrip("\\").strip() for l in RE_LIEN.findall(corps)],
                "taches": taches,
                "faites": faites,
                "semaine": semaine,
                "statut": str(meta.get("statut") or "") or None,
                "extrait": re.sub(r"\s+", " ", re.sub(r"[#*>`|\[\]]", " ", corps_sans_code)).strip()[:280],
            })

    # Résolution des liens [[Nom]] -> numéro de note (par nom de fichier, sans tenir compte des majuscules)
    par_nom = {}
    for n in notes:
        par_nom.setdefault(unicodedata.normalize("NFC", n["nom"].lower()), n["id"])
        par_nom.setdefault(unicodedata.normalize("NFC", n["chemin"][:-3].lower()), n["id"])
    liens, vus, introuvables = [], set(), 0
    for n in notes:
        for cible in n.pop("_liens"):
            cle = unicodedata.normalize("NFC", cible.lower()).removesuffix(".md")
            j = par_nom.get(cle, par_nom.get(cle.split("/")[-1]))
            if j is None:
                introuvables += 1
                continue
            if j == n["id"]:
                continue
            paire = (min(n["id"], j), max(n["id"], j))
            if paire not in vus:
                vus.add(paire)
                liens.append([n["id"], j])
    return notes, liens, introuvables


# ---------- Avancée du projet (le chef d'orchestre écrit JOURNAL.md, BACKLOG.md et le registre des stratégies) ----------
RE_CYCLE = re.compile(r"^## Cycle (\d+) · ([ABC]) · (.+)$", re.M)
VU = ICI / "laurisverse_vu.json"           # dernier cycle déjà raconté par la voix
NOMS_IDEES = {"pic_volatilite": "suite d'un pic de volatilité", "fair_value_gap": "fair value gap",
              "funding_extreme": "funding extrême", "cassure_4h": "cassure de canal 4 heures"}
AXES = {"A": "dashboard", "B": "connaissance", "C": "stratégies"}


def phrase_courte(t, n=220):
    t = texte_parle(t)
    if len(t) <= n:
        return t
    coupe = t[:n].rsplit(". ", 1)[0]
    return (coupe if len(coupe) > 60 else t[:n].rsplit(" ", 1)[0]) + "."


RE_MEMBRE = re.compile(r"`?\[{0,2}([a-z0-9][a-z0-9\-]+)\]{0,2}`?\s*(?:\(([^)]*)\))?")


def lire_membres(texte):
    """« markets-backtest, hocs (GO), avocat-du-diable (NO-GO) » -> [{id, issue}]"""
    out = []
    for morceau in re.split(r"[,;·]", texte):
        m = RE_MEMBRE.search(morceau.strip())
        if m:
            out.append({"id": m.group(1), "issue": (m.group(2) or "").strip()})
    return out


def lire_orchestre(coffre: Path) -> dict:
    """Ce que la boucle a fait : cycles du JOURNAL, échelle des stratégies, collecteur, prochaines tâches."""
    out = {"cycles": [], "nouveaux": [], "strategies": [], "candidates": 0, "collecteur": None, "prochaines": [], "phrases": []}
    journal = coffre / "JOURNAL.md"
    if journal.exists():
        texte = journal.read_text(encoding="utf-8", errors="replace")
        blocs = list(RE_CYCLE.finditer(texte))
        for k, m in enumerate(blocs):
            corps = texte[m.end(): blocs[k + 1].start() if k + 1 < len(blocs) else len(texte)]
            dire = re.search(r"\*\*À dire\*\*\s*:?\s*(.+)", corps)     # phrase écrite pour la voix
            res = dire or re.search(r"\*\*Résultat\*\*\s*:?\s*(.+)", corps)
            ag = re.search(r"\*\*Agents\*\*\s*:?\s*(.+)", corps)       # qui a travaillé (rituels de l'Équipe)
            dt = re.search(r"\*\*Date\*\*\s*:?\s*(\d{4}-\d{2}-\d{2})", corps)
            out["cycles"].append({"n": int(m.group(1)), "axe": m.group(2), "titre": texte_parle(m.group(3)),
                                  "resultat": phrase_courte(res.group(1)) if res else "", "dire": bool(dire),
                                  "agents": lire_membres(ag.group(1)) if ag else [], "date": dt.group(1) if dt else None})
    try:
        deja = json.loads(VU.read_text(encoding="utf-8")).get("dernier_cycle", 0)
    except Exception:
        deja = 0
    out["nouveaux"] = [c for c in out["cycles"] if c["n"] > deja]
    out["dernier_cycle"] = max((c["n"] for c in out["cycles"]), default=0)
    reg = ICI / "registre_variantes.json"
    if reg.exists():
        try:
            for idee, f in json.loads(reg.read_text(encoding="utf-8")).items():
                out["strategies"].append({"idee": NOMS_IDEES.get(idee, idee.replace("_", " ")), "statut": f.get("statut"),
                                          "variantes": len(f.get("variantes", []))})
        except Exception:
            pass
    out["candidates"] = sum(1 for x in out["strategies"] if x["statut"] == "candidate")
    etat = ICI / "archives_gamma" / "etat.json"
    if etat.exists():
        try:
            e = json.loads(etat.read_text(encoding="utf-8"))
            jours = len([d for d in (ICI / "archives_gamma").glob("20??-??-??") if d.is_dir()])
            out["collecteur"] = {"photos": e.get("photos", 0), "erreurs": e.get("erreurs", 0), "jours": jours}
        except Exception:
            pass
    backlog = coffre / "BACKLOG.md"
    if backlog.exists():
        for ligne in backlog.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^\|\s*(\d+)\s*\|\s*([ABC])\s*\|\s*(.+?)\s*\|", ligne)
            if m:
                out["prochaines"].append({"n": int(m.group(1)), "axe": m.group(2), "texte": phrase_courte(m.group(3), 140)})
        out["prochaines"] = out["prochaines"][:3]
    # Les phrases que la voix lira
    ph = out["phrases"]
    nv = out["nouveaux"]
    if nv:
        ph.append(f"Côté projet, {len(nv)} {'nouveaux cycles' if len(nv) > 1 else 'nouveau cycle'} depuis ta dernière écoute.")
        for c in nv[-5:]:
            ph.append(c["resultat"] if c["dire"] else f"Cycle {c['n']}, {AXES.get(c['axe'], '')} : {c['titre']}. {c['resultat']}")
        if len(nv) > 5:
            ph.append(f"Les {len(nv) - 5} autres sont dans le journal, et dans le guide à gauche.")
    elif out["cycles"]:
        ph.append(f"Côté projet, rien de nouveau depuis ta dernière écoute. Le dernier cycle est le numéro {out['dernier_cycle']}.")
    if out["strategies"]:
        arch = sum(1 for x in out["strategies"] if x["statut"] == "archivee")
        ph.append(f"Stratégies : {len(out['strategies'])} idées testées, {arch} archivées, "
                  + (f"{out['candidates']} candidate{'s' if out['candidates'] > 1 else ''}." if out["candidates"] else "aucune candidate pour l'instant."))
    if out["candidates"]:
        ph.insert(0, "Rappel important, et je le répéterai tant que tu ne m'as pas répondu : une stratégie est candidate. "
                     "Pour qu'elle puisse être misée, crée une clé sur ta plateforme, autorisée à trader mais jamais à retirer, "
                     "et dis-moi ton budget maximum.")
    c = out["collecteur"]
    if c:
        ph.append(f"Collecteur gamma : {c['jours']} jour{'s' if c['jours'] > 1 else ''} d'archives sur 21 visés, {c['erreurs']} erreur{'s' if c['erreurs'] > 1 else ''}.")
    if out["prochaines"]:
        ph.append("Prochaine tâche de la boucle : " + out["prochaines"][0]["texte"].rstrip(".") + ".")
    return out


def marquer_vu(orchestre: dict) -> None:
    try:
        VU.write_text(json.dumps({"dernier_cycle": orchestre["dernier_cycle"],
                                  "le": datetime.now().strftime("%Y-%m-%d %H:%M")}), encoding="utf-8")
    except Exception:
        pass


# ---------- Organigramme : fiches d'agents (dossier « 10 - Agents ») ----------
DOSSIER_AGENTS = "10 - Agents"
PLACES = {"ceo", "cos", "board", "direction", "poste"}
# Les cycles du chef d'orchestre sont des passages du Head of Markets et de ses postes
POSTE_PAR_AXE = {"A": "markets-data-dashboard", "B": "markets-pedagogue", "C": "markets-backtest"}
POSTE_CROQ = {"P": "croq-produit", "D": "croq-dev", "G": "croq-growth"}
CROQ_DEFAUT = Path.home() / "Documents" / "Croq"          # dépôt Lauris-Ad/Croq sur le PC
JOURNAL_CROQ = "docs/equipe/JOURNAL.md"
RE_CYCLE_CROQ = re.compile(r"^## Cycle (\d+) · ([PDG]) · (.+)$", re.M)


def lire_journal_croq(dossier: Path):
    """Cycles de l'équipe Croq : journal de la branche main sur GitHub (git fetch silencieux), sinon copie locale."""
    import subprocess
    texte = None
    if (dossier / ".git").exists():
        env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never")
        options = {"capture_output": True, "env": env, "timeout": 25}
        if os.name == "nt":
            options["creationflags"] = 0x08000000           # aucune fenêtre
        try:
            subprocess.run(["git", "-C", str(dossier), "fetch", "--quiet", "origin", "main"], **options)
            r = subprocess.run(["git", "-C", str(dossier), "show", "origin/main:" + JOURNAL_CROQ], **options)
            if r.returncode == 0:
                texte = r.stdout.decode("utf-8", errors="replace")
        except Exception:
            pass
    if texte is None and (dossier / JOURNAL_CROQ).exists():
        texte = (dossier / JOURNAL_CROQ).read_text(encoding="utf-8", errors="replace")
    cycles = []
    if not texte:
        return cycles
    blocs = list(RE_CYCLE_CROQ.finditer(texte))
    for k, m in enumerate(blocs):
        corps = texte[m.end(): blocs[k + 1].start() if k + 1 < len(blocs) else len(texte)]
        dire = re.search(r"\*\*À dire\*\*\s*:?\s*(.+)", corps) or re.search(r"\*\*Résultat\*\*\s*:?\s*(.+)", corps)
        ag = re.search(r"\*\*Agents\*\*\s*:?\s*(.+)", corps)
        dt = re.search(r"\*\*Date\*\*\s*:?\s*(\d{4}-\d{2}-\d{2})", corps)
        cycles.append({"n": int(m.group(1)), "axe": m.group(2), "titre": texte_parle(m.group(3)), "projet": "croq",
                       "resultat": phrase_courte(dire.group(1)) if dire else "", "agents": lire_membres(ag.group(1)) if ag else [],
                       "date": dt.group(1) if dt else None})
    return cycles
RE_LIGNE_TABLEAU = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([a-z0-9\-]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")


def _liste(v):
    if isinstance(v, list):
        return [x.strip() for x in v if x.strip()]
    return [x.strip() for x in str(v or "").split(",") if x.strip()]


def lire_agents(coffre: Path, cycles=None) -> dict:
    """Fiches d'agents + passages (tableau Passages.md) + cycles du JOURNAL rattachés aux postes Marchés."""
    dossier = coffre / DOSSIER_AGENTS
    agents, passages = [], []
    if dossier.is_dir():
        for f in sorted(dossier.glob("*.md")):
            try:
                texte = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            meta, corps = lire_frontmatter(texte)
            if f.stem.lower() == "passages":
                for ligne in corps.splitlines():
                    m = RE_LIGNE_TABLEAU.match(ligne.strip())
                    if m:
                        passages.append({"date": m.group(1), "agent": m.group(2), "projet": texte_parle(m.group(3)),
                                         "issue": texte_parle(m.group(4)), "note": texte_parle(m.group(5))})
                continue
            place = str(meta.get("place") or "").strip().lower()
            if place not in PLACES:
                continue
            reports = meta.get("reports_to")
            agents.append({
                "id": str(meta.get("name") or f.stem).strip(),
                "titre": str(meta.get("titre") or meta.get("name") or f.stem),
                "sigle": str(meta.get("sigle") or "")[:7],
                "place": place,
                "direction": str(meta.get("direction") or "").strip().lower(),
                "reports_to": reports.strip() if isinstance(reports, str) else "",
                "works_with": _liste(meta.get("works_with")),
                "description": str(meta.get("description") or ""),
                "modele": str(meta.get("model") or "—"),
                "outils": _liste(meta.get("tools")),
                "skills": str(meta.get("skills") or "aucune"),
                "statut": str(meta.get("statut") or "actif"),
                "fichier": f.relative_to(coffre).as_posix(),
                "corps": corps.strip()[:4000],
            })
    connus = {a["id"] for a in agents}
    sortie_cycles = []   # un cycle sans ligne « Agents » est rattaché au poste de son axe
    for c in cycles or []:
        titre = c.get("titre", "")
        croq = c.get("projet") == "croq"
        chef = "croq-ceo" if croq else "markets-head"
        poste = chef if "point d'étape" in titre.lower() else (POSTE_CROQ if croq else POSTE_PAR_AXE).get(c.get("axe"), chef)
        membres = [m for m in (c.get("agents") or []) if m.get("id") in connus] or [{"id": poste, "issue": ""}]
        sortie_cycles.append({"n": c["n"], "axe": c.get("axe"), "titre": titre, "date": c.get("date"),
                              "projet": "croq" if croq else "trading", "chef": chef,
                              "resultat": c.get("resultat") or c.get("dire") or "", "agent": membres[0]["id"], "membres": membres})
    return {"agents": agents, "passages": [p for p in passages if p["agent"] in connus] if connus else passages,
            "cycles": sortie_cycles}


# ---------- Bibliothèque : leçons du coffre et épisodes du podcast (repo cerveau-trading) ----------
PODCAST_SITE = "https://lauris-ad.github.io/cerveau-trading/"
PODCAST_DEPOT = "https://api.github.com/repos/Lauris-Ad/cerveau-trading/contents/episodes"
PODCAST_PROGRESSION = "https://raw.githubusercontent.com/Lauris-Ad/cerveau-trading/main/progression.json"
CACHE_PODCAST = ICI / "laurisverse_podcast.json"


def _json_url(url):
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "laurisverse", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=8) as r:
        return json.loads(r.read().decode("utf-8"))


def lire_podcast():
    """Épisodes écrits (repo) et publiés (site). Sans réseau : dernière lecture gardée en cache."""
    try:
        ecrits = sorted(x["name"][:-3] for x in _json_url(PODCAST_DEPOT) if re.match(r"e\d+.*\.md$", x["name"]))
        publies = _json_url(PODCAST_SITE + "episodes.json")
        try:
            prog = _json_url(PODCAST_PROGRESSION)
        except Exception:
            prog = {}
        info = {"ecrits": ecrits, "publies": [{"id": e["id"], "numero": e["numero"], "titre": e["titre"], "duree": e.get("duree", 0)} for e in publies],
                "lecon_en_cours": prog.get("lecon_en_cours"), "lecons_validees": prog.get("lecons_validees", []),
                "lu_le": datetime.now().strftime("%d/%m/%Y %H:%M")}
        try:
            CACHE_PODCAST.write_text(json.dumps(info, ensure_ascii=False), encoding="utf-8")
        except OSError:
            pass
        return info
    except Exception:
        try:
            return json.loads(CACHE_PODCAST.read_text(encoding="utf-8"))
        except Exception:
            return None


def bibliotheque(coffre: Path, podcast=None) -> dict:
    lecons = []
    dossier = coffre / "02 - Leçons"
    if dossier.is_dir():
        for f in sorted(dossier.glob("*.md")):
            m = re.match(r"(\d+)\s*-\s*(.+)", f.stem)
            lecons.append({"numero": m.group(1) if m else None, "titre": m.group(2) if m else f.stem,
                           "chemin": f.relative_to(coffre).as_posix()})
    pod = podcast if podcast is not None else lire_podcast()
    out = {"lecons": lecons, "nb_lecons": sum(1 for l in lecons if l["numero"]), "nb_fiches": sum(1 for l in lecons if not l["numero"])}
    if pod:
        out.update({"episodes_total": len(pod.get("ecrits", [])), "episodes_publies": len(pod.get("publies", [])),
                    "publies": pod.get("publies", []), "lecon_en_cours": pod.get("lecon_en_cours"),
                    "lecons_validees": pod.get("lecons_validees", []), "podcast_lu_le": pod.get("lu_le")})
    return out


def main():
    p = argparse.ArgumentParser(description="Laurisverse : univers 3D du coffre Obsidian")
    p.add_argument("--coffre", default=str(COFFRE_PAR_DEFAUT), help="dossier du coffre")
    p.add_argument("--sans-ouvrir", action="store_true", help="ne pas ouvrir le navigateur")
    p.add_argument("--prenom", default="Lauris", help="prénom affiché par le guide")
    p.add_argument("--croq", default=str(CROQ_DEFAUT), help="dossier du dépôt Croq (journal de l'équipe Croq)")
    p.add_argument("--parler", action="store_true", help=argparse.SUPPRESS)   # ancienne option, ignorée
    args = p.parse_args()

    coffre = Path(args.coffre).resolve()
    print(f"Lecture du coffre : {coffre}")
    notes, liens, introuvables = lire_coffre(coffre)
    if not notes:
        print("Aucune note .md trouvée. Vérifie le chemin du coffre.")
        return

    donnees = {
        "coffre": coffre.name,
        "prenom": args.prenom,
        "aujourdhui": date.today().isoformat(),
        "genere": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "notes": notes,
        "liens": liens,
        "orchestre": lire_orchestre(coffre),
    }
    cycles_croq = lire_journal_croq(Path(args.croq))
    donnees["agents"] = lire_agents(coffre, donnees["orchestre"]["cycles"] + cycles_croq)
    donnees["bibliotheque"] = bibliotheque(coffre)
    modele = MODELE.read_text(encoding="utf-8")
    if ORGANIGRAMME.exists():
        modele = modele.replace("</body>", ORGANIGRAMME.read_text(encoding="utf-8") + "\n</body>")
    json_txt = json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")
    SORTIE.write_text(modele.replace("/*__DONNEES__*/null", json_txt), encoding="utf-8")

    datees = sum(1 for n in notes if n["date"])
    print(f"{len(notes)} notes, {len(liens)} liens entre notes, {datees} notes datées.")
    if introuvables:
        print(f"({introuvables} liens pointent vers des notes qui n'existent pas encore.)")
    ag, bib = donnees["agents"], donnees["bibliotheque"]
    print(f"Organigramme : {len(ag['agents'])} agents, {len(ag['passages'])} passages notés, "
          f"{len(ag['cycles']) - len(cycles_croq)} cycles trading, {len(cycles_croq)} cycles Croq.")
    print(f"Bibliothèque : {bib['nb_lecons']} leçons, "
          + (f"{bib['episodes_publies']}/{bib['episodes_total']} épisodes publiés" if bib.get("episodes_total") else "épisodes inconnus (pas de réseau ni de cache)")
          + (f" (lu le {bib['podcast_lu_le']})" if bib.get("podcast_lu_le") else "") + ".")
    print(f"Laurisverse prêt : {SORTIE}")
    if args.parler:
        print("La voix automatique est désactivée : ouvre la page et clique « Écouter » si tu veux l'entendre.")
    if not args.sans_ouvrir:
        webbrowser.open(SORTIE.as_uri())
        marquer_vu(donnees["orchestre"])   # ouvert à la main : les cycles affichés comptent comme vus


if __name__ == "__main__":
    main()
