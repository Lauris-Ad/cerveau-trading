---
id: e05
numero: 5
titre: "Options et gamma, partie 2 : delta, gamma et dealers"
description: "Leçon 07, parties 4 à 6 : la vitesse, l'accélération, et pourquoi la couverture des dealers peut freiner ou amplifier le marché."
date: 2026-11-13
sources:
  - "02 - Leçons/07 - Options et gamma, les bases.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 5, deuxième partie sur les options et le gamma.

Certains jours, le marché semble freiné, comme s'il oscillait dans une boîte. D'autres jours, chaque baisse en appelle une autre. Une explication possible, selon ta leçon, vient de gros acteurs qui ne parient même pas sur la direction : les dealers, qui se couvrent. Pour comprendre leur mécanique, il faut deux mots : le delta et le gamma.

Cet épisode reprend les parties 4 à 6 de la leçon 7.

## Idée 1

Première idée clé : le delta, c'est la vitesse.

Le delta répond à la question : si l'indice monte d'un point, de combien bouge le prix de mon option ?

Un call très hors de la monnaie a un delta d'environ 0 virgule 05 : l'indice monte d'un point, l'option gagne 0 virgule 05 point. Elle réagit à peine. Un call à la monnaie a un delta d'environ 0 virgule 50 : il bouge moitié moins vite que l'indice. Un call très dans la monnaie, environ 0 virgule 95 : il bouge presque comme l'indice. Et un put a un delta entre zéro et moins un : il est négatif, parce que le put gagne quand l'indice baisse.

En bonus : le delta d'un call donne aussi une idée grossière de la probabilité qu'il finisse dans la monnaie. Un delta de 0 virgule 20, c'est environ 20 pour cent de chances.

## Idée 2

Deuxième idée clé : le gamma, c'est l'accélération.

Le delta ne reste pas fixe. Si l'indice monte, ton call à 0 virgule 50 devient un call à 0 virgule 60, puis 0 virgule 70. Le gamma mesure de combien le delta change quand l'indice bouge d'un point.

L'analogie de ta leçon : si le delta est la vitesse, le gamma est la pédale d'accélérateur. Un gros gamma, c'est une voiture nerveuse : la vitesse change brutalement au moindre mouvement.

Où le gamma est-il le plus fort ? À deux endroits. D'abord près du prix actuel, sur les options à la monnaie. Une option très loin du prix a un gamma presque nul. Ensuite près de l'échéance. Une option qui expire dans deux heures, avec un strike juste à côté du prix, passe très vite de « vaut zéro » à « vaut beaucoup ». C'est pour ça que les 0DTE ont un gamma énorme.

## Idée 3

Troisième idée clé : les dealers et leur couverture.

Les teneurs de marché, ou dealers, sont de grosses sociétés toujours prêtes à acheter ou vendre des options. Leur métier n'est pas de parier sur la direction, mais de gagner un peu sur l'écart entre prix d'achat et prix de vente : le spread, que tu as vu dans la leçon sur le carnet d'ordres. L'analogie : un bureau de change à l'aéroport. Il ne veut pas parier sur le dollar, il veut sa commission.

Pour ne pas parier, le dealer neutralise son delta : il achète ou vend des futures ES, ou du SPY, pour que ses gains et ses pertes s'annulent. C'est la couverture en delta. Et comme le delta change avec le prix, c'est-à-dire à cause du gamma, il doit ajuster en permanence.

Mais personne ne publie la vraie position des dealers. Ton outil, comme la plupart des sites de gamma, fait donc une hypothèse. Le public achète des puts pour s'assurer, donc les dealers les ont vendus : gamma négatif sur les puts. Le public vend des calls pour toucher la prime sur ses actions, donc les dealers les ont achetés : gamma positif sur les calls. C'est souvent à peu près vrai, mais pas toujours. Un jour d'euphorie où le public achète massivement des calls, la convention se trompe de signe.

## Exemple concret

L'exemple de ta leçon, en deux cas.

Cas A : le dealer est long gamma, il a acheté des options. Il a acheté un call à delta 0 virgule 50. Pour être neutre, il vend 0 virgule 50 unité d'indice. L'indice monte, le delta passe à 0 virgule 60 : il doit vendre encore 0 virgule 10. L'indice baisse, le delta retombe à 0 virgule 40 : il rachète 0 virgule 10. Il vend quand ça monte et achète quand ça baisse. Il freine le marché, comme un thermostat qui coupe le chauffage quand il fait trop chaud.

Cas B : le dealer est short gamma, il a vendu des options. Tout s'inverse. Il doit acheter quand ça monte et vendre quand ça baisse. Il pousse dans le sens du mouvement, comme une boule de neige qui grossit en dévalant la pente.

## Récap

On récapitule.

Un : le delta est la vitesse de l'option par rapport à l'indice. Entre zéro et un pour un call, entre zéro et moins un pour un put.

Deux : le gamma est l'accélération, la variation du delta. Il est le plus fort près du prix actuel et près de l'échéance, d'où le gamma énorme des 0DTE.

Trois : un dealer long gamma freine le marché, comme un thermostat. Un dealer short gamma l'amplifie, comme une boule de neige. Et la position des dealers n'est pas connue : elle est supposée.

## Questions

Trois questions, tirées du quiz de ta leçon.

Question 1. Si le delta est la vitesse, qu'est-ce que le gamma ? Et où est-il le plus fort ?

[pause 8]

Réponse : c'est l'accélération, la variation du delta quand l'indice bouge d'un point. Il est le plus fort près du prix actuel et près de l'échéance.

Question 2. Pourquoi un dealer long gamma vend-il quand le marché monte ?

[pause 8]

Réponse : parce que le delta de ses options augmente quand l'indice monte. Pour rester neutre, il doit vendre davantage d'indice.

Question 3. Pourquoi la position des dealers affichée par l'outil peut-elle être fausse ?

[pause 8]

Réponse : parce qu'elle n'est publiée nulle part. L'outil suppose que le public achète des puts et vend des calls. Un jour d'euphorie où le public achète des calls, la convention se trompe de signe.

## Fin

C'est la fin de la deuxième partie. Dans l'épisode 6 : l'onglet Gamma de ton dashboard, élément par élément, et ses limites. La note complète est dans ton coffre, leçon 7, et le lien est dans la description. À bientôt.
