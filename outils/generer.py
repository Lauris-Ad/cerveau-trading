"""Construit le podcast « Cerveau trading » : audio (edge-tts), flux RSS, pages des leçons, quiz.

Usage : python outils/generer.py --url https://<compte>.github.io/<depot>/ [--sortie _site] [--sans-audio]
Dépendances : edge-tts, markdown, pillow, et ffmpeg/ffprobe installés.
"""
import argparse, asyncio, email.utils, hashlib, html, json, re, shutil, subprocess, tempfile, urllib.parse
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
VOIX = "fr-FR-DeniseNeural"
TITRE = "Cerveau trading"
AUTEUR = "Cerveau trading"
RESUME = "Les leçons de mon coffre Obsidian, lues pour l'oreille. Fidèles aux notes, avec 3 questions à la fin de chaque épisode."


def lire_episode(chemin):
    texte = chemin.read_text(encoding="utf-8").replace("\r\n", "\n")
    _, entete, corps = texte.split("---\n", 2)
    meta, cle = {}, None
    for ligne in entete.splitlines():
        if ligne.startswith("  - "):
            meta.setdefault(cle, []).append(ligne[4:].strip().strip('"'))
        elif ":" in ligne:
            cle, val = ligne.split(":", 1)
            val = val.strip().strip('"')
            meta[cle] = val if val else []
    meta["corps"] = corps
    meta["fichier"] = chemin
    meta["empreinte"] = hashlib.sha256(texte.encode()).hexdigest()[:12]
    return meta


def morceaux(corps):
    """Découpe le script : ('texte', str) ou ('silence', secondes)."""
    sortie = []
    for bloc in re.split(r"\n\s*\n", corps.strip()):
        bloc = bloc.strip()
        m = re.fullmatch(r"\[pause (\d+(?:\.\d+)?)\]", bloc)
        if m:
            sortie.append(("silence", float(m.group(1))))
        elif bloc.startswith("## "):
            sortie.append(("silence", 1.0))
        elif bloc:
            sortie.append(("texte", " ".join(bloc.split())))
            sortie.append(("silence", 0.5))
    return sortie


async def synthese(texte, fichier):
    import edge_tts
    for essai in range(4):
        try:
            await edge_tts.Communicate(texte, VOIX, rate="-5%").save(str(fichier))
            return
        except Exception:
            if essai == 3:
                raise
            await asyncio.sleep(3 * (essai + 1))


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def construire_audio(ep, destination):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        liste = []
        for i, (genre, val) in enumerate(morceaux(ep["corps"])):
            f = tmp / f"{i:04d}.wav"
            if genre == "texte":
                mp3 = tmp / f"{i:04d}.mp3"
                asyncio.run(synthese(val, mp3))
                ffmpeg("-i", str(mp3), "-ar", "24000", "-ac", "1", str(f))
            else:
                ffmpeg("-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(val), str(f))
            liste.append(f"file '{f}'")
        (tmp / "liste.txt").write_text("\n".join(liste))
        ffmpeg("-f", "concat", "-safe", "0", "-i", str(tmp / "liste.txt"),
               "-c:a", "libmp3lame", "-b:a", "64k", "-ac", "1", str(destination))


def duree(fichier):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nk=1:nw=1", str(fichier)], capture_output=True, text=True)
    return int(float(r.stdout.strip() or 0))


def page(titre, contenu):
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titre)}</title>
<style>body{{font:17px/1.55 -apple-system,system-ui,sans-serif;max-width:720px;margin:0 auto;padding:16px;background:#fbfaf7;color:#1c1b19}}
table{{border-collapse:collapse;display:block;overflow-x:auto}}td,th{{border:1px solid #ddd;padding:4px 8px}}
a{{color:#2558b5}}audio{{width:100%}}.ep{{border-bottom:1px solid #e5e2da;padding:12px 0}}
@media(prefers-color-scheme:dark){{body{{background:#161615;color:#ecebe7}}a{{color:#8ab4ff}}td,th{{border-color:#444}}}}</style>
</head><body>{contenu}</body></html>"""


def nom_lecon(source):
    return Path(source).stem


def slug(texte):
    import unicodedata
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def lien_obsidian(source):
    return "obsidian://open?vault=Trading-Vault&file=" + urllib.parse.quote(source.removesuffix(".md"))


def couverture(destination):
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (1400, 1400), (22, 30, 46))
    d = ImageDraw.Draw(img)
    try:
        f1 = ImageFont.truetype("DejaVuSans-Bold.ttf", 150)
        f2 = ImageFont.truetype("DejaVuSans.ttf", 70)
    except OSError:
        f1 = f2 = ImageFont.load_default()
    for i, y in enumerate(range(380, 1020, 80)):
        d.line([(200, y), (1200, y + (i % 3 - 1) * 40)], fill=(60, 120, 200), width=6)
    d.text((700, 560), "Cerveau", font=f1, fill=(240, 240, 240), anchor="mm")
    d.text((700, 740), "trading", font=f1, fill=(120, 190, 255), anchor="mm")
    d.text((700, 1120), "leçons audio", font=f2, fill=(200, 200, 200), anchor="mm")
    img.save(destination)


def construire_laurisverse(coffre, out, pages, episodes):
    """Version téléphone du Laurisverse : même moteur que sur PC, dossiers publics seulement."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("laurisverse", RACINE / "laurisverse" / "laurisverse.py")
    lv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lv)
    notes, liens, _ = lv.lire_coffre(coffre)
    par_lecon = {}
    for ep in episodes:
        for src in ep["sources"]:
            par_lecon.setdefault(src, []).append({"id": ep["id"], "numero": int(ep["numero"]), "titre": ep["titre"]})
    for n in notes:
        n["page"] = pages.get(n["chemin"])
        n["episodes"] = par_lecon.get(n["chemin"], [])
    donnees = {"coffre": "Trading-Vault", "prenom": "Lauris", "aujourdhui": datetime.now().date().isoformat(),
               "genere": datetime.now().strftime("%d/%m/%Y"), "notes": notes, "liens": liens, "mobile": True}
    modele = (RACINE / "laurisverse" / "modele.html").read_text(encoding="utf-8")
    ajout = (RACINE / "laurisverse" / "mobile.html").read_text(encoding="utf-8")
    json_txt = json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")
    page_lv = modele.replace("/*__DONNEES__*/null", json_txt).replace("</body>", ajout + "\n</body>")
    page_lv = page_lv.replace("<head>", '<head>\n<link rel="apple-touch-icon" href="couverture.png">\n<meta name="apple-mobile-web-app-capable" content="yes">', 1)
    (out / "laurisverse.html").write_text(page_lv, encoding="utf-8")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True)
    p.add_argument("--sortie", default="_site")
    p.add_argument("--sans-audio", action="store_true")
    a = p.parse_args()
    base = a.url.rstrip("/") + "/"
    out = Path(a.sortie)
    shutil.rmtree(out, ignore_errors=True)
    (out / "audio").mkdir(parents=True)
    (out / "lecons").mkdir()

    import markdown
    coffre = RACINE / "coffre"
    (out / "notes").mkdir()
    pages = {}  # chemin relatif au coffre -> page web
    for src in sorted(coffre.rglob("*.md")):
        rel = src.relative_to(coffre).as_posix()
        texte = src.read_text(encoding="utf-8").replace("\r\n", "\n")
        texte = re.sub(r"^---\n.*?\n---\n", "", texte, flags=re.S)
        texte = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), texte)
        texte = texte.replace("- [ ]", "- ☐").replace("- [x]", "- ☑")
        corps = markdown.markdown(texte, extensions=["tables", "fenced_code"])
        nom = slug(rel.removesuffix(".md")) + ".html"
        (out / "notes" / nom).write_text(page(src.stem, corps + '<p><a href="../index.html">← Épisodes</a> · <a href="../laurisverse.html">Laurisverse</a></p>'), encoding="utf-8")
        pages[rel] = "notes/" + nom
    lecons_html = {Path(k).stem: v for k, v in pages.items() if k.startswith("02 - ")}

    episodes = [lire_episode(f) for f in sorted((RACINE / "episodes").glob("e*.md"))]
    items, blocs, catalogue = [], [], []
    for ep in episodes:
        mp3 = out / "audio" / f"{ep['id']}.mp3"
        if a.sans_audio:
            mp3.write_bytes(b"")
        else:
            construire_audio(ep, mp3)
        sec = duree(mp3) if mp3.stat().st_size else 0
        liens = []
        for s in ep["sources"]:
            n = nom_lecon(s)
            web = base + lecons_html[n] if n in lecons_html else None
            liens.append((n, web, lien_obsidian(s)))
        desc_html = f"<p>{html.escape(ep['description'])}</p><p>Notes sources :</p><ul>" + "".join(
            f'<li>{html.escape(n)} : ' + (f'<a href="{w}">lire sur le téléphone</a> · ' if w else "") +
            f'<a href="{o}">ouvrir dans Obsidian</a></li>' for n, w, o in liens) + "</ul>" + \
            f'<p><a href="{base}quiz.html">Passer le quiz</a></p>'
        date = datetime.fromisoformat(ep["date"]).replace(hour=6 + int(ep["numero"]), tzinfo=timezone.utc)
        items.append(f"""<item><title>{html.escape(ep['numero'] + '. ' + ep['titre'], quote=False)}</title>
<description><![CDATA[{desc_html}]]></description>
<enclosure url="{base}audio/{ep['id']}.mp3" length="{mp3.stat().st_size}" type="audio/mpeg"/>
<guid isPermaLink="false">{ep['id']}-{ep['empreinte']}</guid>
<pubDate>{email.utils.format_datetime(date)}</pubDate>
<itunes:duration>{sec}</itunes:duration><itunes:episode>{ep['numero']}</itunes:episode></item>""")
        blocs.append(f'<div class="ep" id="{ep["id"]}"><h3>{html.escape(ep["numero"] + ". " + ep["titre"])}</h3>'
                     f'<p>{html.escape(ep["description"])} ({sec // 60} min {sec % 60:02d})</p>'
                     f'<audio controls preload="none" src="audio/{ep["id"]}.mp3"></audio><p>'
                     + " · ".join(f'<a href="{lecons_html[n]}">{html.escape(n)}</a>' for n, w, o in liens if n in lecons_html)
                     + "</p></div>")
        catalogue.append({"id": ep["id"], "numero": int(ep["numero"]), "titre": ep["titre"],
                          "audio": f"audio/{ep['id']}.mp3", "duree": sec})

    couverture(out / "couverture.png")
    construire_laurisverse(coffre, out, pages, episodes)
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
<atom:link href="{base}feed.xml" rel="self" type="application/rss+xml"/>
<title>{TITRE}</title><link>{base}</link><language>fr</language>
<description>{html.escape(RESUME, quote=False)}</description><itunes:author>{AUTEUR}</itunes:author>
<itunes:image href="{base}couverture.png"/><itunes:explicit>false</itunes:explicit>
<itunes:owner><itunes:name>{AUTEUR}</itunes:name></itunes:owner>
<image><url>{base}couverture.png</url><title>{TITRE}</title><link>{base}</link></image>
<itunes:category text="Education"/><itunes:type>serial</itunes:type>
{''.join(reversed(items))}
</channel></rss>"""
    (out / "feed.xml").write_text(rss, encoding="utf-8")
    (out / "episodes.json").write_text(json.dumps(catalogue, ensure_ascii=False), encoding="utf-8")
    (out / "index.html").write_text(page(TITRE, f"<h1>{TITRE}</h1><p>{html.escape(RESUME)}</p>"
        f'<p><a href="laurisverse.html"><b>Laurisverse</b></a> · <a href="quiz.html"><b>Passer le quiz</b></a> · Flux podcast : <code>{base}feed.xml</code></p>'
        + "".join(blocs)), encoding="utf-8")
    for f in ["quiz.html", "sw.js", "manifest.webmanifest"]:
        shutil.copy(RACINE / "web" / f, out / f)
    shutil.copy(RACINE / "quiz" / "questions.json", out / "questions.json")
    if (RACINE / "avancee" / "avancee.json").exists():      # avancée du projet, lue par le Laurisverse du téléphone
        shutil.copy(RACINE / "avancee" / "avancee.json", out / "avancee.json")
    for ep in catalogue:
        print(f"::notice title=Episode {ep['id']}::{ep['duree']} s, {(out / ep['audio']).stat().st_size} octets")
    print(f"::notice title=Flux::{base}feed.xml")
    print(f"{len(episodes)} épisodes, {len(lecons_html)} leçons -> {out}")


if __name__ == "__main__":
    main()
