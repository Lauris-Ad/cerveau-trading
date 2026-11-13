---
id: e04
numero: 4
titre: "Options et gamma, partie 1 : indices, options et open interest"
description: "Leçon 07, parties 1 à 3 : SPX, SPY, ES, ce qu'est une option, l'open interest et les 0DTE."
date: 2026-11-13
sources:
  - "02 - Leçons/07 - Options et gamma, les bases.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 4, première partie d'une série de trois sur les options et le gamma.

Voici l'idée de toute la série. Des banques, qu'on appelle les teneurs de marché, vendent et achètent des millions d'options sur la Bourse américaine. Pour ne pas parier, elles se couvrent en achetant ou en vendant l'indice. Le gamma mesure à quel point cette couverture va les obliger à acheter ou vendre quand le prix bouge. Et l'onglet Gamma de ton dashboard essaie d'estimer où ces achats et ventes forcés pourraient se produire.

Avant d'y arriver, il faut trois briques. C'est le programme de cet épisode, qui reprend les parties 1 à 3 de la leçon 7.

## Idée 1

Première idée clé : indice, ETF, future, qui est qui ?

Un indice, c'est une moyenne : un seul nombre qui résume le prix d'un panier d'actions. On ne peut pas l'acheter directement, comme on ne peut pas acheter la température moyenne de la France.

Le SPX, c'est l'indice S and P 500 : les 500 plus grosses entreprises américaines. Il vaut quelques milliers de points. Le NDX, c'est le Nasdaq 100 : 100 grosses entreprises, surtout de la tech, comme Apple, Nvidia ou Microsoft. Il vaut environ 3 à 4 fois le SPX.

Le SPY est un ETF : une action qu'on peut acheter, qui copie le S and P 500. Il vaut environ le SPX divisé par 10. Le QQQ est l'ETF qui copie le Nasdaq 100, environ le NDX divisé par 40.

Et enfin les futures. Un future, c'est un contrat qui dit : on se met d'accord aujourd'hui sur un prix pour une date future. En pratique, presque personne n'attend la date : on l'achète et on le revend, comme une action. L'ES est le future sur le S and P 500, à la bourse CME de Chicago. Un point d'ES vaut 50 dollars. Sa version mini, le MES, vaut 5 dollars par point. Le NQ est le future sur le Nasdaq 100 : 20 dollars par point, et 2 dollars pour la version mini, le MNQ.

Pourquoi les traders aiment l'ES et le NQ ? Parce qu'ils s'échangent presque 24 heures sur 24, 5 jours sur 7, alors que le SPX ne bouge que pendant la séance de New York, de 15 heures 30 à 22 heures, heure de Paris. Et parce qu'ils ont un effet de levier. C'est puissant, et très dangereux : 10 points d'ES contre toi, c'est 500 dollars de perte sur un seul contrat.

Dernier détail : l'ES n'est pas exactement le SPX. Il y a un petit écart de quelques points, qu'on appelle la base, et qui fond jusqu'à l'échéance du future, en mars, juin, septembre et décembre.

L'analogie de ta leçon : le SPX est le thermomètre. Le SPY est une photo du thermomètre qu'on peut acheter. Et l'ES est un pari sur ce que dira le thermomètre, avec un levier.

## Idée 2

Deuxième idée clé : une option, c'est un droit, pas une obligation, d'acheter ou de vendre quelque chose à un prix fixé, jusqu'à une date fixée. Et ce droit se paie.

Un call, c'est le droit d'acheter. On l'achète si on pense que ça va monter. C'est comme verser des arrhes pour réserver un appartement au prix d'aujourd'hui.

Un put, c'est le droit de vendre. On l'achète si on pense que ça va baisser, ou pour s'assurer. C'est comme une assurance auto : on paie, et si l'accident arrive, l'assurance rembourse.

Le strike, c'est le prix fixé dans le contrat. L'échéance, la date où le droit expire. La prime, le prix payé pour acheter l'option. Et le multiplicateur : une option SPX porte sur 100 fois l'indice. Une prime de 20 points coûte donc 2 000 dollars.

On dit qu'une option est à la monnaie quand son strike est tout près du prix actuel. Dans la monnaie, quand elle vaudrait déjà quelque chose si elle expirait maintenant. Et hors de la monnaie, quand elle ne vaudrait rien maintenant.

## Idée 3

Troisième idée clé : l'open interest et les 0DTE.

L'open interest, c'est le nombre de contrats encore ouverts sur un strike et une échéance. Le volume, c'est le nombre de contrats échangés aujourd'hui. L'analogie de ta leçon : pour un concert, le volume, c'est le nombre de billets vendus aujourd'hui au guichet. L'open interest, c'est le nombre de billets encore valides dans la poche des gens.

Point clé pour ton outil : l'open interest est publié une seule fois par jour, le matin, pour la veille. Toute la journée, le calcul utilise donc des positions d'hier.

0DTE veut dire zero days to expiration : des options qui expirent aujourd'hui. Le SPX a des échéances tous les jours de la semaine, et les 0DTE représentent souvent autour de la moitié du volume des options SPX, voire plus. Le problème : un 0DTE acheté à 16 heures et revendu à 19 heures n'apparaît jamais dans l'open interest. Une partie importante de l'activité du jour est donc invisible. C'est pour ça que l'onglet a un filtre « 0DTE seul » et « Sans 0DTE ».

## Exemple concret

L'exemple chiffré de ta leçon, avec des chiffres inventés. Le SPX est à 6 000. Tu achètes un call de strike 6 050, échéance vendredi, pour une prime de 20 points, donc 2 000 dollars.

Si vendredi le SPX finit à 5 950, ton call vaut zéro : tu n'as aucun intérêt à acheter à 6 050. Tu perds 2 000 dollars, ta prime, et pas plus.

S'il finit à 6 050, pile sur le strike, le call vaut toujours zéro : tu perds encore 2 000 dollars.

À 6 070, ton call vaut 20 points : tu récupères juste ta prime, résultat nul.

Et à 6 100, il vaut 50 points, soit 5 000 dollars. Moins ta prime, tu gagnes 3 000 dollars.

Ce qu'il faut retenir : l'acheteur d'option risque au maximum sa prime, et il gagne gros seulement si le mouvement est grand et rapide. Le vendeur encaisse la prime, mais son risque peut être énorme : c'est lui qui joue l'assureur. Et la plupart des options achetées finissent à zéro, comme la plupart des assurances ne servent jamais.

## Récap

On récapitule.

Un : le SPX est l'indice, le SPY est un ETF qui le copie, et l'ES est le future, avec un point à 50 dollars et un fort effet de levier.

Deux : un call est le droit d'acheter, un put le droit de vendre, à un strike fixé, jusqu'à une échéance, contre une prime. L'acheteur risque au maximum sa prime.

Trois : l'open interest date d'hier, et les 0DTE ouverts et fermés dans la journée sont invisibles pour l'outil.

## Questions

Trois questions, tirées du quiz de ta leçon.

Question 1. Quelle est la différence entre le SPX, le SPY et l'ES ?

[pause 8]

Réponse : le SPX est l'indice, on ne peut pas l'acheter. Le SPY est un ETF, une action qui le copie. L'ES est le future, un contrat à terme avec effet de levier.

Question 2. Combien gagnes-tu ou perds-tu si l'ES bouge de 8 points sur un contrat ? Et sur un contrat MES ?

[pause 10]

Réponse : 8 fois 50, soit 400 dollars sur un ES. Et 8 fois 5, soit 40 dollars sur un MES.

Question 3. Pourquoi l'open interest affiché le matin ne voit-il pas les 0DTE du jour ?

[pause 8]

Réponse : parce qu'il est publié une fois par jour, pour la veille. Un 0DTE ouvert et fermé dans la journée n'y apparaît jamais.

## Fin

C'est la fin de la première partie. Dans l'épisode 5 : le delta, le gamma, et le rôle des dealers. La note complète est dans ton coffre, leçon 7, et le lien est dans la description. À bientôt.
