# Cerveau trading : podcast et quiz

- `episodes/` : un script par épisode, écrit pour l'oreille à partir des notes de `lecons/` (rien d'autre).
  `## Titre` = pause courte non lue, `[pause 6]` = silence de 6 secondes.
- `lecons/` : copie des notes du coffre Obsidian (02 - Leçons).
- `quiz/questions.json` : questions et réponses, reliées à une leçon et à un épisode.
- `web/` : page de quiz (hors-ligne, répétition espacée sur le téléphone).
- `outils/generer.py` : voix (edge-tts, gratuite), flux podcast, pages des leçons.

À chaque modification poussée sur `main`, GitHub régénère tout et publie le site (GitHub Pages, gratuit).
