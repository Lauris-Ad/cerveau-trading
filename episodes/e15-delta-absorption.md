---
id: e15
numero: 15
titre: "Delta, absorption et footprint"
description: "Leçon 15 : les agressifs et les passifs, le delta, l'absorption, le footprint, et pourquoi on teste ça sur la crypto."
date: 2026-11-17
sources:
  - "02 - Leçons/15 - Delta, absorption et footprint.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 15.

Derrière chaque bougie, deux camps : ceux qui frappent, et ceux qui attendent. Lire qui frappe le plus fort, c'est l'orderflow.

## Idée 1

Agressif ou passif. L'agressif envoie un ordre au marché : il accepte le prix et paie l'écart. Le passif laisse un ordre limite dans le carnet et attend. Chaque transaction a un acheteur et un vendeur : ce qui compte, c'est lequel des deux était agressif.

## Idée 2

Le delta : volume acheté agressivement moins volume vendu agressivement. Très négatif, les vendeurs ont frappé. Positif, les acheteurs reprennent la main.

## Ce que dit la recherche

Cont, Kukanov et Stoikov, en 2014, montrent que le déséquilibre entre ordres d'achat et de vente explique l'essentiel des variations de prix sur de courtes périodes, de façon presque proportionnelle.

## Idée 3

L'absorption. Si les vendeurs frappent fort et que le prix ne baisse plus, c'est anormal : quelqu'un achète en face, en passif, et encaisse tout. Le footprint montre où, prix par prix, dans la bougie.

Ces données sont gratuites sur la crypto : Binance publie le volume des achats agressifs. Sur le Nasdaq, elles sont payantes. C'est pour ça que nos tests d'absorption se font sur le bitcoin.

## Questions

Question 1. Comment calcule-t-on le delta ?

[pause 8]

Réponse : achats agressifs moins ventes agressives.

Question 2. Qu'est-ce que l'absorption ?

[pause 8]

Réponse : des ventes agressives fortes, sans que le prix baisse. Des acheteurs passifs encaissent.

Question 3. Pourquoi tester l'absorption sur le bitcoin ?

[pause 8]

Réponse : parce que ces données y sont gratuites, alors qu'elles sont payantes sur le Nasdaq.

## Fin

La note complète est dans ton coffre, leçon 15. À bientôt.
