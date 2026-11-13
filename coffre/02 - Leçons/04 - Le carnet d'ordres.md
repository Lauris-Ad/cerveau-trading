---
type: lecon
date: 2026-10-02
semaine: 0
theme: Fonctionnement du marché
maitrise: 
---
# 📖 Le carnet d'ordres

## 🧩 L'idée en une phrase
La liste des ordres limites **en attente** : vendeurs (ask, rouge) au-dessus, acheteurs (bid, vert) en dessous, le prix au milieu.

## 📚 L'essentiel
- **Prix = par unité** (pour 1 BTC). Quantité = combien est disponible à ce prix. Valeur = prix × quantité.
- **Meilleur ask** = en bas de la zone rouge ; **meilleur bid** = en haut de la zone verte. Tous deux collés au prix actuel.
- **Spread** = meilleur ask − meilleur bid. Ex. Binance 02/10 : 85 460 − 85 450 = 10 $ ≈ 0,012 % (avec regroupement par 10).
- Les asks sont toujours au-dessus des bids, car tout ordre compatible est **exécuté immédiatement** et disparaît.
- Un **ordre au marché « mange »** le carnet niveau par niveau → **slippage**, et fait bouger le prix.
- **Liquidité :** je regarde la **valeur en $** disponible et l'**écart entre les niveaux**, pas le nombre d'unités.
- **Maker** (ordre limite qui attend, ajoute de la liquidité) vs **taker** (ordre au marché, en retire). Frais ≈ 0,1 % par ordre.
- **Spoofing :** gros ordres placés pour influencer, puis retirés. Le carnet est une photo instantanée.

## 🔢 Mon exercice
Achat de 0,5 BTC au marché : entièrement servi à 85 460 $ (7,6 BTC disponibles) → 42 730 $.
Slippage ≈ 0 $, frais (0,1 %) ≈ **43 $**. Sur un actif liquide, le vrai coût, ce sont les frais.

## ✅ Règles pratiques
- Avant d'acheter, je regarde la liquidité : spread faible et carnet bien rempli.
- Je ne décide jamais sur la base d'un seul gros ordre.

## 🔗 Liens
[[Glossaire]]
