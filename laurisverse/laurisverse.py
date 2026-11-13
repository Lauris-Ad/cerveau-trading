"""Laurisverse : l'univers 3D de mes notes Obsidian.

Lit toutes les notes .md du coffre, en extrait : dossier, type, tags, date,
longueur et liens [[...]], puis fabrique une page laurisverse.html
(dans le dossier Outil) et l'ouvre dans le navigateur.

Lancement : double-clic sur Lancer-Laurisverse.bat, ou  py laurisverse.py
Options   : py laurisverse.py --coffre "C:\\chemin\\vers\\un\\autre\\coffre"
            py laurisverse.py --sans-ouvrir
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


MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]


def texte_guide(notes, prenom):
    """Même point du jour que le bouton Écouter de la page, en texte simple."""
    heure = datetime.now().hour
    phrases = [("Bonsoir " if heure >= 18 or 5 > heure else "Bonjour ") + prenom + ". Voici ton point du jour."]
    semaines = sorted((n for n in notes if n["type"] == "semaine" and n["semaine"] is not None and n["taches"]),
                      key=lambda n: n["semaine"])
    if semaines:
        s = semaines[0]
        reste, faites = len(s["taches"]), s["faites"]
        theme = s["titre"].split(":", 1)[1].strip() if ":" in s["titre"] else s["titre"]
        phrases.append(f"Tu es en semaine {s['semaine']} : {theme}. Tu as coché {faites} "
                       f"{'tâches' if faites > 1 else 'tâche'} sur {reste + faites}, il en reste {reste}.")
        for k, tache in enumerate(s["taches"][:3]):
            phrases.append(["Ta prochaine tâche : ", "Ensuite : ", "Puis : "][k] + tache["texte"] + ".")
    else:
        phrases.append("Je ne trouve aucune case à cocher non cochée dans tes fiches Semaine.")
    journaux = sorted((n for n in notes if n["type"] == "journal" and n["date"]), key=lambda n: n["date"], reverse=True)
    if not journaux:
        phrases.append("Tu n'as encore aucune note de journal. Crée-en une aujourd'hui avec le modèle Journal du jour.")
    else:
        d = date.fromisoformat(journaux[0]["date"])
        ecart = (date.today() - d).days
        if 0 >= ecart:
            phrases.append("Tu as déjà écrit ton journal aujourd'hui. Bien joué.")
        elif ecart == 1:
            phrases.append("Ton dernier journal date d'hier. Pense à écrire celui d'aujourd'hui.")
        else:
            phrases.append(f"Ton dernier journal date du {d.day} {MOIS[d.month - 1]}, il y a {ecart} jours. "
                           "Prends cinq minutes aujourd'hui pour en écrire un, avec le modèle Journal du jour.")
    idees = [n for n in notes if n["type"] == "idee" and n["statut"] == "a_trier"]
    if idees:
        nb = len(idees)
        phrases.append(f"Tu as {nb} {'idées' if nb > 1 else 'idée'} de stratégie en attente de tri. "
                       "Pas d'urgence : on les trie quand tu auras les bases.")
    phrases.append("Une chose à la fois. Coche tes tâches dans Obsidian, puis relance le Laurisverse pour que je mette ta liste à jour.")
    return " ".join(phrases)


# Voix de Windows (hors navigateur, donc aucun clic nécessaire). Code retour 3 = pas de voix française.
PS_PARLER = (
    "Add-Type -AssemblyName System.Speech; "
    "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
    "$v = $s.GetInstalledVoices() | Where-Object { $_.Enabled -and $_.VoiceInfo.Culture.Name -like 'fr*' } | Select-Object -First 1; "
    "if (-not $v) { exit 3 }; "
    "$s.SelectVoice($v.VoiceInfo.Name); $s.Rate = 0; $s.Speak($env:LAURISVERSE_TEXTE)"
)


def parler(texte):
    import subprocess
    env = dict(os.environ, LAURISVERSE_TEXTE=texte)
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", PS_PARLER], env=env)
    except OSError:
        print("PowerShell introuvable : la voix ne peut pas parler.")
        return
    if r.returncode == 3:
        print("Aucune voix française dans Windows. Paramètres > Heure et langue > Voix : ajoute une voix française.")


def main():
    p = argparse.ArgumentParser(description="Laurisverse : univers 3D du coffre Obsidian")
    p.add_argument("--coffre", default=str(COFFRE_PAR_DEFAUT), help="dossier du coffre")
    p.add_argument("--sans-ouvrir", action="store_true", help="ne pas ouvrir le navigateur")
    p.add_argument("--prenom", default="Lauris", help="prénom utilisé par la voix")
    p.add_argument("--parler", action="store_true", help="ouvrir la page puis lire le point du jour avec la voix de Windows")
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
    }
    modele = MODELE.read_text(encoding="utf-8")
    json_txt = json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")
    SORTIE.write_text(modele.replace("/*__DONNEES__*/null", json_txt), encoding="utf-8")

    datees = sum(1 for n in notes if n["date"])
    print(f"{len(notes)} notes, {len(liens)} liens entre notes, {datees} notes datées.")
    if introuvables:
        print(f"({introuvables} liens pointent vers des notes qui n'existent pas encore.)")
    print(f"Laurisverse prêt : {SORTIE}")
    if not args.sans_ouvrir:
        webbrowser.open(SORTIE.as_uri())
    if args.parler:
        import time
        time.sleep(4)  # laisse la page s'ouvrir avant de parler
        print("Lecture du point du jour...")
        parler(texte_guide(notes, args.prenom))


if __name__ == "__main__":
    main()
