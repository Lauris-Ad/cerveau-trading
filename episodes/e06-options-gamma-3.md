---
id: e06
numero: 6
titre: "Options et gamma, partie 3 : lire l'onglet Gamma et ses limites"
description: "Leçon 07, parties 7 et 8 : GEX, call wall, put wall, zéro gamma, régime, et tout ce que l'outil ne dit pas."
date: 2026-11-13
sources:
  - "02 - Leçons/07 - Options et gamma, les bases.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 6, dernière partie sur les options et le gamma.

Sur Internet, et sur TikTok, beaucoup de discours présentent le gamma comme une boule de cristal. Ta leçon prend le chemin inverse : on apprend à lire l'onglet Gamma de ton dashboard, élément par élément, et on regarde surtout ce qu'il ne dit pas. Tu ne le croiras que si ton propre backtest le montre.

Cet épisode reprend les parties 7 et 8 de la leçon 7.

## Idée 1

Première idée clé : la formule de base, dite en mots.

Pour chaque option, l'outil calcule le GEX. On multiplie le gamma par l'open interest, par 100, par le prix au carré, et par 1 pour cent. Le résultat est positif pour les calls et négatif pour les puts.

En français, le GEX répond à la question : combien de dollars d'indice les dealers devraient-ils acheter ou vendre si l'indice bougeait de 1 pour cent ? L'outil l'affiche en milliards de dollars.

Dans l'onglet, tu choisis d'abord l'indice : le SPX, pour l'ES, ou le NDX, pour le NQ. Le NDX plutôt que le QQQ, parce que c'est l'indice qui colle au NQ. Ensuite, un filtre : toutes échéances, 0DTE seul, ou sans 0DTE. Si presque tout le gamma vient des 0DTE, les niveaux peuvent changer vite dans la journée. Et le prix de l'indice est différé d'environ 15 minutes : ce n'est pas un prix pour trader.

## Idée 2

Deuxième idée clé : les niveaux.

Le graphique GEX par strike montre des barres vertes pour les calls et rouges pour les puts, à plus ou moins 4 pour cent du prix. Les grandes barres sont les endroits où la couverture des dealers pèse le plus.

Le call wall, c'est le strike où les calls pèsent le plus, à plus ou moins 5 pour cent. Il est souvent vu comme un plafond possible : en montant vers lui, les dealers vendent de plus en plus.

Le put wall, c'est le strike où les puts pèsent le plus. Il est souvent vu comme un plancher possible. Mais attention : s'il casse, la baisse peut accélérer, parce qu'on passe dans la zone short gamma.

Enfin, l'outil montre des niveaux clés : les pics, où le GEX net est le plus positif, et les creux, où il est le plus négatif. Ce sont des zones à surveiller, pas des ordres à placer.

## Idée 3

Troisième idée clé : le profil gamma, le zéro gamma et le régime.

Le profil gamma, c'est le GEX total recalculé comme si l'indice était à un autre prix. Une seule courbe qui montre où le marché serait plutôt calme, et où il serait plutôt nerveux.

Le zéro gamma, c'est le prix où cette courbe passe par zéro. C'est la frontière entre les deux régimes. Au-dessus, plutôt calme. En dessous, plutôt nerveux.

Et le régime, c'est le signe du GEX total au prix actuel. Positif : les dealers freinent, comme un thermostat. Négatif : ils amplifient, comme une boule de neige.

## Exemple concret

L'exemple de lecture de ta leçon, avec des chiffres inventés. Le SPX est à 6 000. Le zéro gamma est à 5 950. Le call wall à 6 100, le put wall à 5 900. Le régime est positif.

Lecture : le prix est au-dessus du zéro gamma, donc en théorie, les dealers freinent les mouvements. On s'attendrait plutôt à une journée qui oscille entre 5 900 et 6 100. Si le prix passe sous 5 950, on change de régime, et les mouvements pourraient devenir plus amples.

Remarque le vocabulaire : en théorie, plutôt, pourraient. C'est voulu.

## Récap

On récapitule avec les cinq limites de l'outil. À relire à chaque fois.

Un : la position des dealers est supposée, pas connue.

Deux : l'open interest date d'hier, et les 0DTE ouverts et fermés dans la journée sont invisibles.

Trois : les données sont différées d'environ 15 minutes, parce que la source Cboe est gratuite.

Quatre : la volatilité implicite est figée quand on simule d'autres prix pour le profil. En vrai, elle change quand le marché bouge.

Cinq : le SPX n'est pas l'ES. Il faudra convertir avec la base, qui varie.

Et surtout : aucun de ces niveaux n'est une règle de trading. Ton outil ne sera cru que si ton propre backtest le montre, avec environ un mois d'archives du collecteur. D'ici là, on observe, on note, on ne trade pas. Ta règle d'or : objectif numéro un, ne pas perdre.

## Questions

Trois questions, tirées du quiz de ta leçon.

Question 1. Que veut dire « régime négatif », et pourquoi le marché pourrait-il y être plus nerveux ?

[pause 8]

Réponse : le GEX total est négatif au prix actuel. Les dealers seraient short gamma : ils achètent quand ça monte et vendent quand ça baisse, donc ils amplifient les mouvements.

Question 2. Cite trois limites de l'onglet gamma.

[pause 10]

Réponse : par exemple, la position des dealers est supposée. L'open interest date d'hier. Les données sont différées d'environ 15 minutes. Tu pouvais aussi citer la volatilité implicite figée, ou l'écart entre le SPX et l'ES.

Question 3. Le SPX passe sous le zéro gamma. Est-ce un signal de vente ?

[pause 8]

Réponse : non. Aucun niveau n'est une règle de trading. Le marché pourrait devenir plus nerveux, mais tant que ton propre backtest ne l'a pas montré, on observe et on note, on ne trade pas.

## Fin

C'est la fin de la série sur les options et le gamma. Ta leçon te propose maintenant un exercice de 15 minutes par jour pendant 5 jours de bourse sur l'onglet Gamma : il est détaillé dans la note. La note complète est dans ton coffre, leçon 7, et le lien est dans la description. À bientôt.
