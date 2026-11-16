---
id: e09
numero: 9
titre: "Gamma, partie 4 : niveaux valides et flux de primes"
description: "Leçon 10, parties 1 à 3 : la méthode TikTok en trois règles, pourquoi l'open interest compte, et ce que vaut le flux de primes gratuit."
date: 2026-11-16
sources:
  - "02 - Leçons/10 - Gamma, niveaux, flux et confirmation.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 9.

Tu m'as envoyé une vidéo TikTok sur le gamma. Elle donne trois règles. Un : tous les niveaux ne se valent pas, garde ceux où l'open interest est le plus fort. Deux : le gamma seul ne suffit pas, regarde dans quel sens va l'argent des options. Trois : attends que le prix confirme avant d'entrer.

Ces règles sont raisonnables. Mais la vidéo ne montre aucun résultat : ni nombre de trades, ni gain moyen après frais. Dans cet épisode, on regarde les deux premières règles, ce que la recherche en dit, et ce qu'on a ajouté à ton dashboard.

## Idée 1

Première règle : les niveaux valides.

Rappel de la formule : le GEX d'un strike, c'est le gamma, multiplié par l'open interest, par 100, par le prix au carré et par 1 pour cent.

Un strike peut avoir un gros gamma parce qu'il est tout près du prix et expire bientôt, mais très peu de contrats ouverts. Derrière, il y a alors peu de couverture réelle. Un strike avec beaucoup de contrats ouverts, c'est beaucoup de couverture à ajuster quand le prix s'en approche.

La recherche donne un indice. Ni, Pearson et Poteshman, dans le Journal of Financial Economics en 2005, montrent que les jours d'expiration, les actions avec options cotées clôturent plus souvent près d'un strike. Le déplacement moyen est d'au moins 0,165 pour cent. Ils l'expliquent par la couverture des teneurs de marché, et par des manipulations. Attention : c'est mesuré les jours d'expiration, sur des actions. Ce n'est pas la preuve que chaque grand strike arrête le S&P 500.

## Dans ton dashboard

Dans l'onglet Options, une nouvelle carte s'appelle « Niveaux valides ». À plus ou moins 5 pour cent du prix, elle garde les strikes dont l'open interest est dans les 20 pour cent les plus forts, puis les 5 plus gros GEX nets.

Chaque niveau est marqué frein, si le GEX net est positif, ou accélérateur, s'il est négatif.

Exemple réel, le 13 novembre à 16 heures 45 : le SPX est à 7 520. Les 5 niveaux valides sont tous des accélérateurs. Le plus gros est 7 500, juste en dessous du prix, avec 8 pour cent de tout le GEX de la zone.

## Idée 2

Deuxième règle : le flux de primes.

La prime, c'est le prix d'une option, payé par l'acheteur au vendeur. Les outils payants de la vidéo regardent chaque transaction en direct, et la classent : achetée au prix vendeur, ou vendue au prix acheteur. Ça demande toutes les transactions en temps réel, et c'est payant.

La recherche dit que c'est justement ce sens qui compte. Pan et Poteshman, dans la Review of Financial Studies en 2006, ont utilisé des données non publiques du Cboe, qui disent qui achète pour ouvrir une position. Les actions avec peu de puts achetés ont battu les autres de plus de 0,40 pour cent le lendemain, et de plus de 1 pour cent sur la semaine. Mais ils concluent que l'effet vient surtout d'informations privées, et que la partie visible publiquement en contient beaucoup moins.

## Dans ton dashboard

Notre version gratuite s'appelle « Flux de primes depuis l'ouverture ». Pour chaque option, on multiplie le volume du jour par le prix milieu et par 100. Puis on compare les calls hors de la monnaie aux puts hors de la monnaie. Plus de 1,2 fois plus de calls : penchant calls. L'inverse : penchant puts.

La limite est majeure : on ne sait pas qui a acheté. Une grosse prime de puts peut venir d'un fonds qui achète une protection, ou d'un autre qui vend des puts pour encaisser la prime. Ce n'est donc pas un flux haussier ou baissier.

Le 13 novembre à 16 heures 45, sur le SPX : 774 millions de dollars de puts contre 378 millions de calls. Penchant puts.

## Questions

Trois questions, tirées du quiz de ta leçon.

Question 1. Pourquoi un strike avec un gros gamma mais peu d'open interest est-il un niveau faible ?

[pause 8]

Réponse : parce qu'il y a peu de contrats derrière, donc peu de couverture réelle à ajuster quand le prix s'en approche.

Question 2. Que veut dire « penchant puts » dans ton dashboard ?

[pause 8]

Réponse : plus de primes échangées sur les puts hors de la monnaie que sur les calls. Ce n'est pas forcément baissier : on ne sait pas si ces puts ont été achetés ou vendus.

Question 3. Pourquoi les données de Pan et Poteshman contenaient-elles plus d'information que notre flux gratuit ?

[pause 8]

Réponse : elles disaient qui achetait pour ouvrir une position. Notre source gratuite donne seulement le volume, sans le sens.

## Fin

Dans l'épisode 10, la troisième règle : la confirmation, ce que la recherche dit de la couverture des dealers, et comment on va tester tout ça. La note complète est dans ton coffre, leçon 10. À bientôt.
