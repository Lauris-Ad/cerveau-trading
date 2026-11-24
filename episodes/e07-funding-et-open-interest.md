---
id: e07
numero: 7
titre: "Funding et open interest : ce que la leçon ne dit pas"
description: "Complément de la leçon 08 : pourquoi le funding revient toujours vers 0,01 %, ce qu'il coûte vraiment quand on garde une position, comment naît une cascade de liquidations, trois erreurs fréquentes et un exercice sur ton dashboard."
date: 2026-11-24
sources:
  - "02 - Leçons/08 - Funding rate et open interest.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 7.

Cet épisode ne relit pas ta leçon 8. Il suppose que tu l'as lue : tu sais déjà qui paie qui, et ce que compte l'open interest. Ici, on va plus loin, avec quatre choses que la leçon ne dit pas. Pourquoi le funding revient toujours vers sa valeur calme. Ce qu'il coûte vraiment quand on garde une position. Comment naît une cascade de liquidations. Et trois erreurs que font presque tous les débutants.

## Pourquoi le funding revient au calme

Dans nos données, le funding est positif 86 pour cent du temps, et sa moyenne sur sept ans est presque exactement la valeur calme, 0,01 pour cent. Ce n'est pas un hasard. Il y a des gens dont le métier est de le ramener là.

Imagine un trader prudent. Il achète un bitcoin au comptant, et en même temps il vend à découvert un bitcoin en contrat perpétuel. Si le prix monte, il gagne sur l'un et perd autant sur l'autre. Il ne parie donc ni sur la hausse ni sur la baisse. Mais comme il est short sur le perpétuel, quand le funding est positif, c'est lui qui encaisse le paiement des longs, toutes les 8 heures.

Quand le funding monte très haut, ce montage devient très rentable, donc beaucoup de gens le font. Et en vendant le perpétuel, ils font baisser son prix vers le vrai prix, ce qui fait redescendre le funding. On appelle souvent ça le cash and carry. Retiens l'idée : un funding extrême attire ceux qui le font disparaître.

## Le coût caché quand on garde une position

Dans la leçon, on calcule le funding sur 8 heures. Ça paraît minuscule. Le piège, c'est le temps.

Prenons nos moyennes annuelles. En 2021, l'année de l'euphorie, le funding moyen faisait 30,6 pour cent par an. Un long de 1 000 dollars gardé un mois payait donc environ 25 dollars de funding. Compare avec nos frais d'aller-retour, 0,30 pour cent, soit 3 dollars. Un mois de funding coûtait environ huit fois plus que les frais.

En 2026, jusqu'ici, la moyenne est de 3,3 pour cent par an : environ 2 dollars 75 par mois pour le même long. Même position, même durée, un coût environ neuf fois plus faible. La leçon pratique : avant de garder un long à levier plusieurs semaines, regarde le funding du moment. Un backtest qui oublie le funding peut avoir l'air gagnant alors qu'il ne l'est pas.

## Comment naît une cascade de liquidations

Dans la grille de lecture, « le prix baisse et l'open interest baisse » se termine par le mot liquidés. Voyons ce que ça veut dire.

Avec un effet de levier de 10, tu ne mets qu'un dixième de ta position. Si le prix baisse d'environ 10 pour cent, cette mise est mangée, et la plateforme ferme ta position de force, en vendant. C'est une liquidation. En réalité elle arrive même un peu avant, à cause d'une marge minimale à garder.

Le problème, c'est que cette vente forcée fait encore baisser le prix. Ce qui atteint le seuil de liquidation d'autres longs. Qui vendent à leur tour. C'est une cascade : des dominos. Pendant ce temps, l'open interest fond, parce que des milliers de positions se ferment d'un coup.

Notre record de funding négatif, moins 0,30 pour cent, date du 13 mars 2020, le jour du krach du Covid. Ce jour-là, les longs n'étaient plus pressés d'acheter : ils étaient pressés de sortir.

## Trois erreurs fréquentes

Première erreur : croire qu'un funding très haut est un signal de vente. On l'a testé dans notre boucle : l'idée « funding extrême » a été archivée, 96 trades, une perte de 0,08 pour cent par trade après frais. Une foule à levier peut rester euphorique longtemps.

Deuxième erreur : croire qu'un open interest qui monte, c'est haussier. Chaque contrat ouvert a un acheteur et un vendeur. L'open interest qui monte dit seulement que plus de monde se bat, pas qui va gagner. Il faut le lire avec le prix.

Troisième erreur : oublier le funding dans ses calculs, comme on vient de le voir. Petit sur 8 heures, gros sur un mois.

## Exercice sur ton dashboard

Cette semaine, ouvre l'onglet Volatilité BTC et descends jusqu'à la carte des dérivés. Clique sur « Mesurer l'OI », puis clique sur deux points du graphique, par exemple le début et la fin d'une journée agitée.

Le dashboard te donne la variation de l'open interest, la variation du prix et le funding moyen, puis la case de la grille qui correspond. Note ce que tu vois dans ton journal, avec la date. Tu n'en tires aucun trade : tu entraînes ton œil.

## Questions

Deux questions nouvelles, qui ne sont pas dans ton quiz.

Question 1. Le funding est à plus 0,10 pour cent depuis deux jours. Pourquoi a-t-il de bonnes chances de redescendre, même si personne ne vend de bitcoin ?

[pause 8]

Réponse : parce qu'à ce niveau, le montage comptant plus short perpétuel rapporte beaucoup. Des traders le font, ils vendent le perpétuel, son prix se rapproche du vrai prix, et le funding redescend.

Question 2. Le prix chute de 8 pour cent en une heure et l'open interest baisse fortement en même temps. Quelle est la lecture la plus probable ?

[pause 8]

Réponse : des longs ferment ou sont liquidés. La baisse se nourrit d'elle-même tant que des positions atteignent leur seuil de liquidation.

## Fin

La leçon 8 complète est dans ton coffre Obsidian, avec ses sources. Cet épisode en est le complément : réécoute-le après avoir fait l'exercice. À bientôt.
