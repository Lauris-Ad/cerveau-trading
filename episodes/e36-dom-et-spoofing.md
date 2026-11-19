---
id: e36
numero: 36
titre: "Le DOM et le spoofing"
description: "Leçon 36 : pourquoi le carnet d'ordres affiché ment plus souvent que les trades exécutés, avec les affaires Sarao et JPMorgan."
date: 2026-11-19
sources:
  - "02 - Leçons/36 - Le DOM et le spoofing.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 36.

Le carnet d'ordres montre des intentions. Les trades exécutés montrent des faits. Quand les deux se contredisent, on croit les faits.

## Ce que dit la recherche

Spoofer, c'est poser un gros ordre qu'on ne veut pas exécuter, pour tromper les autres, puis l'annuler. C'est interdit aux États-Unis depuis la loi Dodd-Frank de 2010. Navinder Sarao l'a fait sur le future du S&P 500, y compris le jour du flash crash de 2010 ; il a plaidé coupable en 2016. JPMorgan a payé environ 920 millions de dollars en 2020 pour du spoofing sur les métaux et les obligations.

## Idée 1

C'est pour ça que Dualis Flow lit l'absorption au footprint, sur les trades exécutés, et garde le DOM pour confirmer en scalping.

## Idée 2

Chez nous, il n'y a pas d'historique gratuit du carnet, donc aucune règle de DOM n'est testable. Les trades exécutés de Binance sont gratuits. Mais attention : au cycle 34, la divergence du CVD sur BTC a perdu même avant frais. Un fait n'est pas forcément un signal.

## Questions

Question 1. Quelle différence entre un ordre du DOM et un trade exécuté ?

[pause 8]

Réponse : l'ordre est une intention qu'on peut annuler, le trade est un fait.

Question 2. Qu'est-ce que le spoofing ?

[pause 8]

Réponse : un faux gros ordre posé pour tromper, puis annulé avant d'être touché.

Question 3. Quelle loi l'a interdit aux États-Unis ?

[pause 8]

Réponse : la loi Dodd-Frank, en 2010.

## Fin

La note complète est dans ton coffre, leçon 36. À bientôt.
