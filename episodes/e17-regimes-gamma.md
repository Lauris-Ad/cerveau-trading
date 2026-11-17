---
id: e17
numero: 17
titre: "Régimes de gamma : le flip et les walls"
description: "Leçon 17 : le gamma flip, la Call Wall et la Put Wall, ce que dit la recherche et ce qu'on va tester."
date: 2026-11-17
sources:
  - "02 - Leçons/17 - Régimes de gamma, flip et walls.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 17.

Dans les vidéos sur le Nasdaq, une ligne jaune revient souvent : le gamma flip. Au-dessus, le marché serait calme. En dessous, nerveux. D'où vient cette idée, et tient-elle ?

## Idée 1

Le gamma flip, aussi appelé zéro gamma, ou HVL dans certains outils, c'est le prix où le gamma total des teneurs de marché passe par zéro. Au-dessus, ils sont en général longs gamma : leurs couvertures amortissent les mouvements. En dessous, courts gamma : leurs couvertures les amplifient.

## Idée 2

Les walls. La Call Wall est le strike avec le plus de calls au-dessus du prix : souvent une résistance. La Put Wall, le strike avec le plus de puts en dessous : souvent un support. Attention, chaque fournisseur calcule un peu différemment.

## Ce que dit la recherche

Ni, Pearson, Poteshman et White, en 2021, montrent que le rééquilibrage des couvertures des teneurs de marché d'options change la volatilité des actions et la probabilité de grands mouvements. C'est la base sérieuse de l'idée.

## Idée 3

On va le mesurer sur nos archives gratuites. H2 : la séance du Nasdaq est-elle plus calme quand elle ouvre au-dessus du flip ? H4 : le prix réagit-il plus sur les walls que sur un niveau témoin ? En attendant, le badge régime gamma reste une hypothèse.

## Questions

Question 1. Que se passe-t-il en général pour la volatilité sous le gamma flip ?

[pause 8]

Réponse : elle augmente, parce que les couvertures amplifient les mouvements.

Question 2. Qu'est-ce que la Put Wall ?

[pause 8]

Réponse : le strike avec la plus forte concentration de puts sous le prix, souvent un support.

Question 3. Pourquoi deux outils affichent-ils des niveaux différents ?

[pause 8]

Réponse : chacun calcule le gamma avec ses propres données et hypothèses.

## Fin

La note complète est dans ton coffre, leçon 17. À bientôt.
