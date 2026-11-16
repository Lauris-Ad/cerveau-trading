---
id: e10
numero: 10
titre: "Gamma, partie 5 : la confirmation et le test honnête"
description: "Leçon 10, parties 4 à 6 : attendre la confirmation, ce que dit la recherche sur la couverture des dealers, le gratuit contre le payant, et la règle pré-enregistrée."
date: 2026-11-16
sources:
  - "02 - Leçons/10 - Gamma, niveaux, flux et confirmation.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 10, suite de la méthode TikTok sur le gamma.

Dans l'épisode 9, on a vu les niveaux valides et le flux de primes. Aujourd'hui, la troisième règle, la confirmation. Puis le tableau honnête de ce qu'on peut faire gratuitement, et la façon dont on va tester la méthode.

## Idée 1

La confirmation.

Ne pas acheter parce que le prix touche un niveau, mais attendre qu'il reparte du niveau. On rate une partie du mouvement, mais on évite d'entrer quand le niveau ne tient pas.

## Ce que dit la recherche

Deux travaux éclairent cette règle.

Baltussen, Da, Lammers et Martens, dans le Journal of Financial Economics en 2021, ont étudié plus de 60 futures, actions, obligations, matières premières et devises, de 1974 à 2020. Le rendement de la journée prédit celui de la dernière demi-heure. Ils relient cet élan à la couverture des teneurs de marché quand ils sont courts en gamma : ils doivent acheter quand ça monte, et vendre quand ça baisse.

Barbon et Buraschi, dans un document de travail de 2021 appelé Gamma Fragility, trouvent la même chose côté actions. Quand les dealers sont courts en gamma et que le marché est peu liquide, le prix a tendance à continuer. Quand ils sont longs en gamma, il a tendance à revenir.

En résumé : un frein pourrait plutôt faire rebondir le prix, un accélérateur plutôt le laisser passer. La confirmation sert à voir lequel des deux se produit aujourd'hui.

## Idée 2

Le gratuit contre le payant.

Le GEX par strike : oui, on l'a, avec la chaîne Cboe différée. Les niveaux à fort open interest : oui, c'est la nouvelle carte. Le flux de primes haussier ou baissier : seulement une approximation, puisqu'on ne sait pas qui achète. Le classement des actions par primes : non, il faudrait toutes les chaînes en direct. Et la confirmation sur le future NQ en direct : non plus. Nous confirmerons sur l'indice, avec une photo toutes les 15 minutes, elle-même différée de 15 minutes. C'est plus lent, et ce retard sera compté dans le test.

## Idée 3

Le test honnête.

La règle complète est écrite avant tout test, dans ta fiche d'idée. Un niveau valide est touché, à 0,10 pour cent près. Quinze minutes plus tard, le prix s'en est éloigné d'au moins 0,10 pour cent : c'est la confirmation, et elle donne le sens. Le flux ne doit pas être contraire. On entre à la photo suivante, pour compter le retard des données. Le stop est de l'autre côté du niveau, à 0,15 pour cent. L'objectif est de 2 fois le risque. Et on sort avant la clôture.

Une seule variante. Les critères ne changent pas : au moins 100 trades, et 0,30 pour cent de coûts par aller-retour. Le collecteur aura assez de photos vers la mi-décembre. Avant ça, aucun verdict.

## Mon avis

Les trois règles de la vidéo sont du bon sens de gestion du risque. Et la recherche confirme que la couverture des dealers déplace bien les prix, à certains moments. Mais bon sens plus effet réel ne veut pas dire méthode rentable après frais. La seule réponse qui compte viendra du backtest.

## Questions

Trois questions, tirées du quiz de ta leçon.

Question 1. Selon Baltussen et ses co-auteurs, que se passe-t-il quand les dealers sont courts en gamma ?

[pause 8]

Réponse : leur couverture les oblige à acheter quand ça monte et à vendre quand ça baisse. Ça crée un élan, surtout en fin de journée.

Question 2. Pourquoi notre confirmation est-elle plus lente que celle de la vidéo ?

[pause 8]

Réponse : nos données gratuites sont différées de 15 minutes, et le collecteur ne prend qu'une photo toutes les 15 minutes, sur l'indice et pas sur le future.

Question 3. La vidéo prouve-t-elle que la méthode gagne de l'argent ?

[pause 8]

Réponse : non. Elle ne montre aucun chiffre. Il faut un backtest avec des règles écrites à l'avance, au moins 100 trades, et les coûts.

## Fin

C'est la fin de la leçon 10. La note complète, avec toutes les sources, est dans ton coffre. Le lien est dans la description. À bientôt.
