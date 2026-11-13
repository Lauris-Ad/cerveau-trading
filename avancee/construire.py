"""Fabrique avancee/avancee.json : l'avancée du projet racontée par le Laurisverse du téléphone.
Le chef d'orchestre le relance après chaque cycle :  python avancee/construire.py CHEMIN/JOURNAL.md CHEMIN/BACKLOG.md CHEMIN/registre_variantes.json
On ne publie QUE les phrases « À dire » (écrites pour être lues), jamais le journal complet."""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

RE_CYCLE = re.compile(r"^## Cycle (\d+) · ([ABC]) · (.+)$", re.M)


def main(journal, backlog, registre):
    texte = Path(journal).read_text(encoding="utf-8")
    blocs = list(RE_CYCLE.finditer(texte))
    cycles = []
    for k, m in enumerate(blocs):
        corps = texte[m.end(): blocs[k + 1].start() if k + 1 < len(blocs) else len(texte)]
        d = re.search(r"\*\*À dire\*\*\s*:?\s*(.+)", corps)
        if d:
            cycles.append({"n": int(m.group(1)), "axe": m.group(2), "titre": re.sub(r"[*_`]", "", m.group(3)).strip(),
                           "dire": d.group(1).strip()})
    reg = json.loads(Path(registre).read_text(encoding="utf-8"))
    strat = {"testees": len(reg), "archivees": sum(1 for f in reg.values() if f.get("statut") == "archivee"),
             "candidates": sum(1 for f in reg.values() if f.get("statut") == "candidate"),
             "variantes": sum(len(f.get("variantes", [])) for f in reg.values())}
    prochaine = None
    for ligne in Path(backlog).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([ABC])\s*\|\s*(.+?)\s*\|", ligne)
        if m:
            prochaine = re.sub(r"\s+", " ", re.sub(r"[*_`«»]", "", m.group(3))).split(". ")[0].strip()
            break
    sortie = Path(__file__).parent / "avancee.json"
    sortie.write_text(json.dumps({"maj": datetime.now().strftime("%Y-%m-%d %H:%M"), "cycles": cycles,
                                  "strategies": strat, "prochaine": prochaine}, ensure_ascii=False, indent=1),
                      encoding="utf-8")
    print(f"{len(cycles)} cycles, {strat}, prochaine : {prochaine}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
