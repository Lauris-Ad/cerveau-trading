---
id: e08
numero: 8
titre: "Les coûts : ce que la leçon ne dit pas"
description: "Complément de la leçon 09 : compter les coûts en R plutôt qu'en pour cent, l'exemple réel de l'ouverture US où un vrai signal meurt sous les frais, pourquoi la fréquence multiplie la facture, le même signal sur un autre marché, trois erreurs et un exercice."
date: 2026-11-27
sources:
  - "02 - Leçons/09 - Les coûts, le vrai adversaire.md"
  - "Outil/rapports_backtest/ouverture_us_rapport.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 8.

Cet épisode ne relit pas ta leçon 9. Il suppose que tu l'as lue : tu sais déjà qu'un aller-retour nous coûte 0,30 pour cent, et pourquoi c'est trop sur une heure. Ici, on va plus loin, avec quatre choses que la leçon ne dit pas. Pourquoi il faut compter les coûts en R, et pas en pour cent. Un vrai test, fait cette semaine, où un signal réel est mort sous les frais. Pourquoi trader souvent multiplie la facture. Et pourquoi la même méthode peut vivre sur un marché et mourir sur un autre.

## Compter les coûts en R

Souviens-toi du R : c'est ce que tu perds si ton stop est touché. Si ton stop est à 1 pour cent du prix d'entrée, un R vaut 1 pour cent.

La leçon compare le coût au mouvement du marché. Mais il y a une comparaison encore plus parlante : le coût comparé à ton stop. Avec un stop à 3 pour cent, nos 0,30 pour cent de coûts valent un dixième de R. C'est gérable. Avec un stop à 0,30 pour cent, le coût vaut un R entier. Chaque trade commence alors avec une perte d'un R, avant même que le marché ait bougé.

Retiens le calcul, il tient en une ligne : le coût divisé par la distance du stop. Plus ton stop est serré, plus le coût pèse lourd.

## Un vrai test : l'ouverture américaine

Le 26 novembre, on a testé une méthode tirée d'une vidéo YouTube. On regarde la première bougie de 5 minutes après l'ouverture de la bourse de New York, on entre dans le sens de la cassure, et on met le stop de l'autre côté de cette bougie. Objectif : 10 fois le risque. On l'a testée sur le bitcoin en 5 minutes, sur près de trois ans.

Voici ce qu'on a mesuré, sur 711 trades. Avant les frais, la méthode gagne un tout petit peu : plus 0,06 pour cent par trade. Après les frais, elle perd 0,24 pour cent par trade. Et la raison est exactement celle du R : le stop médian était à 0,25 pour cent du prix. Nos 0,30 pour cent de coûts valaient donc plus d'un R, à chaque trade.

La deuxième version, dite de la zone de bruit, montre la même chose encore plus clairement. 578 trades. Avant frais, plus 0,15 pour cent par trade, et c'est assez régulier pour ne pas être de la chance. Il y a donc bien quelque chose. Mais ce quelque chose fait la moitié de nos coûts. Après frais : moins 0,15 pour cent par trade. Les deux versions sont archivées.

C'est la leçon la plus dure du trading : un signal peut être réel et quand même inutilisable.

## La fréquence multiplie la facture

Un deuxième piège se cache dans le nombre de trades. 711 trades fois 0,30 pour cent, ça fait plus de 200 points de pourcentage payés en frais au total. Si chaque trade avait engagé tout le capital, on aurait payé en frais plus de deux fois sa mise de départ.

Compare avec notre test de cassure hebdomadaire, sur 8 cryptos. Seulement 93 trades, et un résultat moyen de plus 7,3 pour cent par trade, frais déjà payés. Là, nos 0,30 pour cent ne pèsent qu'environ 4 pour cent du gain brut. Mêmes frais, même plateforme : c'est l'horizon et le nombre de trades qui changent tout.

Attention, cette idée n'a pas passé nos critères pour autant : trop peu de trades, et des gains venus surtout des achats en marché haussier. Elle sert ici à montrer le poids des frais, pas à être tradée.

## Même méthode, autre marché

Dernier point surprenant. La méthode de l'ouverture a été écrite pour les futures sur l'indice américain, pas pour le bitcoin. On a fait un petit contrôle sur deux fonds indiciels américains, SPY et QQQ, avec un coût proche de celui d'un future : 0,02 pour cent. Sur 60 jours, les deux versions étaient positives.

Ce contrôle ne compte pas : entre 44 et 59 trades, c'est beaucoup trop peu pour conclure. Mais il montre une idée importante : une méthode n'est pas bonne ou mauvaise en soi. Elle est bonne ou mauvaise pour un marché et pour un coût donnés. Un coût quinze fois plus petit peut changer le verdict.

## Trois erreurs fréquentes

Première erreur : regarder le taux de réussite. Notre méthode d'ouverture ne gagnait que 16 pour cent de ses trades, parce qu'elle vise 10 R. Ce chiffre n'est pas le problème. Le problème, c'est ce que chaque trade gagne en moyenne une fois les frais payés.

Deuxième erreur : serrer son stop pour « risquer moins ». En pour cent du capital, oui, tu risques moins par trade. Mais en R, le coût grossit. Un stop deux fois plus serré, c'est un coût deux fois plus lourd.

Troisième erreur : croire que 0,30 pour cent, c'est tout. Nos backtests ajoutent déjà du slippage par prudence, mais il en manque d'autres. Le funding, si tu gardes un perpétuel, comme on l'a vu dans l'épisode 7. Et l'ordre limite qui n'est pas exécuté : souvent, l'ordre qui ne passe pas, c'est celui du trade qui partait dans ton sens.

## Exercice sur ton dashboard

Cette semaine, ouvre l'onglet Ouverture US. Regarde la première bougie de 5 minutes d'une séance, et note la distance entre son haut et son bas, en pour cent du prix. Divise 0,30 par ce chiffre : tu obtiens ce que nos frais auraient coûté en R ce jour-là.

Fais-le sur trois séances et note-les dans ton journal. Tu n'en tires aucun trade : tu entraînes ton œil à voir le coût avant d'entrer.

## Questions

Deux questions nouvelles, qui ne sont pas dans ton quiz.

Question 1. Ton stop est à 0,60 pour cent du prix d'entrée. Combien de R te coûtent nos frais d'aller-retour ?

[pause 8]

Réponse : un demi-R. 0,30 divisé par 0,60. Chaque trade commence avec une perte d'un demi-R avant que le marché bouge.

Question 2. Une méthode gagne 0,15 pour cent par trade avant frais, de façon régulière. Pourquoi l'a-t-on quand même archivée ?

[pause 8]

Réponse : parce que nos frais font 0,30 pour cent. Le signal est réel, mais il est deux fois plus petit que ce que coûte chaque trade. Après frais, il perd 0,15 pour cent par trade.

## Fin

La leçon 9 complète est dans ton coffre Obsidian, avec ses sources, et le rapport du test de l'ouverture est dans le dossier des rapports de backtest. Réécoute cet épisode après avoir fait l'exercice. À bientôt.
