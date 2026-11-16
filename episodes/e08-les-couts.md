---
id: e08
numero: 8
titre: "Les coûts, le vrai adversaire"
description: "Leçon 09 et fiche backtest : maker, taker, slippage, et la mesure qui explique pourquoi nos idées sur une heure ont échoué."
date: 2026-11-16
sources:
  - "02 - Leçons/09 - Les coûts, le vrai adversaire.md"
  - "02 - Leçons/Fiche - Backtest honnête.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 8.

Chaque trade paie des frais et du slippage. Sur des petits mouvements, ces coûts sont plus gros que ce que le marché peut te donner. C'est exactement ce qui a fait échouer nos premières idées sur le bitcoin en une heure. Cet épisode reprend ta leçon 9.

## Idée 1

Première idée : maker et taker.

Le taker, le preneur, est exécuté tout de suite contre un ordre déjà présent dans le carnet. C'est le cas d'un ordre au marché.

Le maker, le faiseur, attend dans le carnet à un prix choisi. C'est un ordre limite qui n'est pas exécuté immédiatement.

Chez Binance au comptant, avec un compte normal, c'est 0,10 pour cent dans les deux cas. Nos backtests prennent ce taux plein : 0,10 pour cent par côté.

## Idée 2

Deuxième idée : le spread et le slippage.

Le spread, c'est l'écart entre le meilleur acheteur et le meilleur vendeur. On l'a mesuré ensemble : environ 0,012 pour cent sur le bitcoin.

Le slippage, c'est l'écart entre le prix voulu et le prix obtenu, surtout quand ça bouge vite. Notre règle prend 0,05 pour cent par côté, environ 4 fois le spread mesuré, par prudence.

Au total : 2 fois 0,15, soit 0,30 pour cent par aller-retour.

## Idée 3

Troisième idée : la mesure qui change tout.

Sur le bitcoin, le mouvement médian en une heure est de 0,20 pour cent. Le coût d'un aller-retour en représente 154 pour cent. Deux fois sur trois, le mouvement est plus petit que ce qu'on paie pour entrer et sortir.

Sur une journée, le mouvement médian est de 1,13 pour cent, et le coût n'en représente plus que 27 pour cent. Sur une semaine, 3,35 pour cent de mouvement, et le coût ne pèse plus que 9 pour cent.

L'analogie de ta leçon : vendre des sandwichs à 3 euros quand la livraison en coûte 4,60. Plus tu vends, plus tu perds. Vendre des plateaux-repas à 30 euros avec la même livraison, c'est jouable.

## Ce que nos tests ont montré

Pic de volatilité et fair value gap, sur une heure : un résultat brut proche de zéro, et environ moins 0,33 pour cent par trade une fois les coûts payés. Les coûts font toute la perte.

La cassure de canal sur 4 heures est la seule idée positive après coûts, avec plus 0,12 pour cent, mais pas assez solide pour exclure la chance.

D'où la décision : les prochaines idées visent des horizons de plusieurs jours.

## Le backtest honnête

Ta fiche « backtest honnête » ajoute les règles du jeu. Les critères sont écrits avant le premier test, et ne changent plus. On ne teste que sur 70 pour cent des données ; les 30 derniers pour cent servent une seule fois, à la fin. On compte chaque variante essayée, et plus on en essaie, plus l'exigence monte. Et une idée qui échoue est archivée avec sa raison, jamais retouchée jusqu'à ce qu'elle passe.

## Questions

Trois questions, tirées du quiz de ta leçon.

Question 1. Combien coûte un aller-retour dans nos backtests ?

[pause 8]

Réponse : 0,30 pour cent. 0,10 de frais et 0,05 de slippage, de chaque côté.

Question 2. Pourquoi un ordre limite n'est-il pas une solution gratuite ?

[pause 8]

Réponse : il coûte moins cher en frais, mais il peut ne jamais être exécuté. On peut rater justement les meilleurs trades.

Question 3. Une idée gagne 0,25 pour cent brut par trade. Est-elle rentable chez nous ?

[pause 8]

Réponse : non. Après 0,30 pour cent de coûts, elle perd 0,05 pour cent par trade.

## Fin

La note complète est dans ton coffre, leçon 9, avec la fiche backtest honnête. Les liens sont dans la description. À bientôt.
