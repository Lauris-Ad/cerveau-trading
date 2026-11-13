---
type: lecon
date: 2026-11-13
semaine: Stratégies
theme: Coûts de transaction
maitrise: 
---
# 📖 Les coûts : le vrai adversaire

## 🧩 L'idée en une phrase
Chaque trade paie des **frais** et du **slippage**. Sur des petits mouvements, ces coûts sont plus gros que ce que le marché peut te donner : c'est ce qui a fait échouer nos idées sur BTC 1 h.

## 1. Les frais : maker et taker
- **Taker** (preneur) : ton ordre est exécuté **tout de suite** contre un ordre déjà présent dans le carnet. C'est le cas d'un **ordre au marché**. Tu « prends » de la liquidité.
- **Maker** (faiseur) : ton ordre **attend** dans le carnet, à un prix choisi : c'est un **ordre limite** qui n'est pas exécuté immédiatement. Tu « fais » le marché pour les autres.
- Chez Binance au comptant, compte normal : **0,10 % maker et 0,10 % taker**, **0,075 %** avec la réduction de 25 % en payant en BNB (source secondaire, voir plus bas).
- Notre règle de backtest prend **0,10 % par côté**, le taux plein (`CRITERES.md`).

## 2. Le slippage et le spread
- **Spread** : l'écart entre le meilleur acheteur et le meilleur vendeur. On l'a mesuré ensemble le 01-02/10 : environ **0,012 %** sur BTC/USDT.
- **Slippage** : l'écart entre le prix voulu et le prix obtenu, surtout avec un ordre au marché quand ça bouge vite.
- Notre règle : **0,05 % par côté**, environ 4 fois le spread mesuré, par prudence.
- Total : 2 × (0,10 + 0,05) = **0,30 % par aller-retour**.

## 3. La mesure qui change tout (BTC, 14/11/2022 → 01/09/2025)
| Horizon | Mouvement médian | Le coût en représente | Mouvements plus petits que le coût |
|---|---|---|---|
| 1 h | 0,20 % | **154 %** | 66 % |
| 4 h | 0,38 % | 79 % | 42 % |
| 1 jour | 1,13 % | 27 % | 18 % |
| 3 jours | 2,08 % | 14 % | 9 % |
| 1 semaine | 3,35 % | 9 % | 5 % |
| 1 mois | 8,58 % | 3 % | 2 % |

Lecture : sur 1 h, le mouvement « normal » est **plus petit** que ce qu'on paie pour entrer et sortir. Pour gagner sur 1 h, il faudrait deviner le sens bien mieux que le hasard **et** battre 0,30 %. Sur 1 semaine, le coût ne pèse plus que 9 % du mouvement typique.

Analogie : vendre des sandwichs à 3 € quand la livraison en coûte 4,60 €. Plus tu vends, plus tu perds. Vendre des plateaux-repas à 30 € avec la même livraison, c'est jouable.

## 4. Ce que nos tests ont montré
- Pic de volatilité, fair value gap (1 h) : résultat **brut ≈ 0**, net ≈ **−0,33 %** par trade. Les coûts font toute la perte.
- Cassure de canal 4 h : la seule idée **positive après coûts** (+0,12 %), mais pas assez solide pour passer (t = 0,53).
- Conclusion de travail : les prochaines idées viseront des horizons de **plusieurs jours**, ou des entrées en **ordre limite** (maker) pour réduire le coût (à tester, sans le supposer gagné d'avance : un ordre limite peut ne jamais être exécuté).

## 🧠 Quiz (mes réponses)
1. Différence entre maker et taker ? Quel type d'ordre est en général taker ?
2. Combien coûte un aller-retour dans nos backtests, et d'où vient chaque morceau ?
3. Sur BTC 1 h, le mouvement médian est de 0,20 %. Pourquoi est-ce un problème ?
4. À partir de quel horizon le coût pèse-t-il moins de 15 % du mouvement médian ?
5. Pourquoi un ordre limite n'est-il pas une solution « gratuite » ?
6. Une idée a un résultat brut de +0,25 % par trade. Est-elle rentable chez nous ?

## 📚 Sources
- Maker et taker : [Binance.US, What are maker and taker fees?](https://support.binance.us/en/articles/9842914-what-are-maker-and-taker-fees) (« Market orders are usually takers »).
- Taux Binance au comptant (0,10 % / 0,10 %, 0,075 % avec BNB) : [BitDegree, mis à jour le 28/07/2026](https://www.bitdegree.org/crypto/tutorials/binance-fees). Source secondaire : la page officielle des frais n'a pas pu être lue.
- Spread mesuré : séance du 01-02/10/2026 (`etat-du-parcours.md`).
- Tableau des mouvements : `Outil/mesure_mouvements.py`, données `donnees/BTC-USDT_1h.csv` (70 % d'apprentissage).

## 📒 Mots à ajouter au [[Glossaire]]
Maker · Taker · Ordre au marché · Ordre limite · Spread · Slippage · Coût aller-retour
