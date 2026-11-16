---
id: e07
numero: 7
titre: "Funding rate et open interest des contrats perpétuels"
description: "Leçon 08 : qui paie qui toutes les 8 heures, ce que compte l'open interest, et comment lire les deux ensemble sans en faire un signal."
date: 2026-11-16
sources:
  - "02 - Leçons/08 - Funding rate et open interest.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 7.

Sur Binance, des milliers de traders parient sur le bitcoin avec des contrats perpétuels. Deux chiffres résument ce qu'ils font : le funding rate, qui dit quel camp est le plus pressé, et l'open interest, qui dit combien de paris sont encore ouverts. Cet épisode reprend ta leçon 8.

## Idée 1

Première idée : le contrat perpétuel.

C'est un future sans date de fin. On parie sur la hausse, on dit être long, ou sur la baisse, on dit être short, souvent avec un effet de levier, sans jamais posséder de bitcoin.

Le problème : sans date de fin, rien ne force le prix du contrat à rester collé au vrai prix. La solution, c'est le funding.

## Idée 2

Deuxième idée : le funding rate.

Toutes les 8 heures, à 1 heure, 9 heures et 17 heures à Paris en hiver, les longs et les shorts s'échangent un paiement. Binance ne prend rien : c'est de trader à trader.

Taux positif : les longs paient les shorts. Le contrat est plus cher que le vrai prix, trop de monde veut acheter. Taux négatif : les shorts paient les longs.

Le montant, c'est la valeur de la position multipliée par le taux. Une position de 1 000 dollars avec un taux de 0,01 pour cent paie 10 centimes toutes les 8 heures.

Et 0,01 pour cent, c'est justement la valeur calme. Elle vient d'un taux d'intérêt fixé par Binance à 0,01 pour cent par période. Tant que l'écart de prix reste petit, le funding reste là.

Pense à une balançoire : si trop d'enfants s'assoient du côté hausse, ceux-là paient pour que d'autres viennent de l'autre côté.

## Nos chiffres

Sur nos 7 864 relevés, de septembre 2019 à novembre 2026, le funding moyen est de 0,0104 pour cent par 8 heures. Il est positif 86 pour cent du temps. Les records : plus 0,30 pour cent en février 2020, et moins 0,30 pour cent le 13 mars 2020, pendant le krach du Covid.

En rythme annuel, ça faisait 30,6 pour cent en 2021, l'année de l'euphorie, contre 4,2 pour cent en 2022, le marché baissier.

Un funding très haut et longtemps positif veut dire beaucoup d'acheteurs à levier. Ce n'est pas un signal de vente en soi. C'est une mesure de foule, à tester avant d'y croire. Et on l'a testé : l'idée « funding extrême » a été archivée, avec 96 trades et une perte de 0,08 pour cent par trade après frais.

## Idée 3

Troisième idée : l'open interest.

C'est le nombre de contrats encore ouverts. Ce n'est pas le volume. Le volume compte tout ce qui s'échange et repart de zéro à chaque période. L'open interest s'additionne tant que les positions restent ouvertes.

Un nouvel acheteur et un nouveau vendeur ouvrent : l'open interest monte. Deux anciens ferment : il baisse. L'un ferme et l'autre ouvre, le contrat change de main : il ne bouge pas.

Limite pratique : Binance ne donne l'historique de l'open interest que sur le dernier mois. Notre fichier grossit seulement parce que la tâche planifiée le met à jour chaque matin.

## Lire les deux ensemble

Voici la grille de lecture habituelle, à garder comme hypothèse.

Le prix monte et l'open interest monte : de nouveaux acheteurs entrent. Le prix monte et l'open interest baisse : des vendeurs ferment, on parle de rachat de shorts. Le prix baisse et l'open interest monte : de nouveaux vendeurs entrent. Le prix baisse et l'open interest baisse : des acheteurs ferment, ou sont liquidés.

Ce sont des lectures, pas une stratégie. Avant de s'en servir, il faut une fiche d'idée, des critères figés et un backtest.

## Questions

Trois questions, tirées du quiz de ta leçon.

Question 1. Le funding est à plus 0,05 pour cent. Qui paie qui ?

[pause 8]

Réponse : les longs paient les shorts. Pour une position de 2 000 dollars, c'est 1 dollar toutes les 8 heures, donc 3 dollars par jour.

Question 2. Quelle différence entre volume et open interest ?

[pause 8]

Réponse : le volume compte tout ce qui s'échange et repart de zéro. L'open interest compte les contrats encore ouverts. Si un contrat change simplement de main, le volume monte mais l'open interest ne bouge pas.

Question 3. Le prix monte et l'open interest baisse. Quelle est la lecture habituelle ?

[pause 8]

Réponse : des vendeurs ferment leurs positions, c'est un rachat de shorts.

## Fin

La note complète est dans ton coffre, leçon 8, avec les sources officielles de Binance. Le lien est dans la description. À bientôt.
