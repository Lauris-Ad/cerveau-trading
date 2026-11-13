---
type: lecon
date: 2026-11-13
semaine: Dashboard
theme: Contrats perpétuels
maitrise: 
---
# 📖 Funding rate et open interest des contrats perpétuels

## 🧩 L'idée en une phrase
Sur Binance, des milliers de traders parient sur BTC avec des **contrats perpétuels**. Le **funding rate** dit qui paie qui pour que ce contrat reste collé au vrai prix (donc quel camp est le plus pressé), et l'**open interest** dit combien de paris sont encore ouverts.

## 1. Le contrat perpétuel
- C'est un **future sans date de fin** : on parie sur la hausse (*long*) ou la baisse (*short*) de BTC, souvent avec effet de levier, sans jamais posséder de BTC.
- Problème : sans date de fin, rien ne force son prix à rester égal au prix réel. La solution, c'est le funding.

## 2. Le funding rate
- Toutes les **8 heures** (00 h, 08 h, 16 h UTC, donc 1 h, 9 h, 17 h à Paris en hiver), les longs et les shorts **s'échangent un paiement**. Binance ne prend rien : c'est de trader à trader.
- **Taux positif** : les **longs paient les shorts**. Le contrat est plus cher que le vrai prix, trop de monde veut acheter.
- **Taux négatif** : les **shorts paient les longs**.
- Montant = valeur de la position × taux. Exemple : position de 1 000 $ et taux de 0,01 % → 0,10 $ toutes les 8 h.
- La base de calcul inclut un « taux d'intérêt » fixé à **0,01 % par période**. Tant que l'écart de prix reste petit, le funding vaut **0,01 %** : c'est la valeur « calme ».
- Analogie : une balançoire. Si trop d'enfants s'assoient du côté « hausse », ceux-là paient pour que d'autres viennent de l'autre côté.

**Nos chiffres (BTCUSDT, 7 864 relevés, 10/09/2019 → 13/11/2026)**
| Mesure | Valeur |
|---|---|
| Moyenne | 0,0104 % par 8 h |
| Taux positif | 85,8 % du temps |
| Record | +0,30 % (12/02/2020) et −0,30 % (13/03/2020, krach du Covid) |
| Moyenne annuelle (× 3 × 365) | 30,6 % en 2021 (euphorie), 4,2 % en 2022 (marché baissier), 3,3 % en 2026 jusqu'ici |
| 30 derniers jours | 0,0067 % par 8 h, sous la valeur calme |

Lecture : un funding très haut et longtemps positif = beaucoup d'acheteurs à levier. Ce n'est **pas** un signal de vente en soi : c'est une mesure de foule, à tester avant d'y croire.

## 3. L'open interest (OI)
- C'est le **nombre de contrats encore ouverts** à un instant donné. Ce n'est pas le volume : le volume compte tout ce qui s'échange (ouvertures et fermetures) et repart de zéro à chaque période ; l'OI s'additionne tant que les positions restent ouvertes.
- Un nouvel acheteur + un nouveau vendeur ouvrent → **l'OI monte**. Deux anciens ferment → **l'OI baisse**. L'un ferme, l'autre ouvre (le contrat change de main) → **l'OI ne bouge pas**.
- Sur nos données : 92 296 BTC le 23/10 à 20 h UTC, 99 705 BTC le 13/11 à 15 h UTC, soit **+8 %** en 3 semaines.
- Limite : Binance ne donne l'historique de l'OI que sur **le dernier mois**. Notre fichier `donnees/BTC-USDT_oi_1h.csv` grossit donc seulement si on relance `telecharger_funding.py` régulièrement.

## 4. Lire les deux ensemble (grille de lecture, pas une stratégie)
| Prix | OI | Lecture habituelle |
|---|---|---|
| ↑ | ↑ | De nouveaux acheteurs entrent |
| ↑ | ↓ | Des vendeurs ferment (rachat de shorts) |
| ↓ | ↑ | De nouveaux vendeurs entrent |
| ↓ | ↓ | Des acheteurs ferment ou sont liquidés |

> Ces lectures sont des **hypothèses**. Avant de s'en servir, il faudra une fiche d'idée, des critères figés et un backtest (voir `CRITERES.md`).

## 🧠 Quiz (mes réponses)
1. Pourquoi un contrat perpétuel a-t-il besoin d'un funding rate ?
2. Le funding est à +0,05 %. Qui paie qui ? Combien paie une position de 2 000 $ en une journée ?
3. Quelle est la valeur « calme » du funding sur Binance, et d'où vient-elle ?
4. À quelles heures de Paris tombe le funding en hiver ?
5. Différence entre volume et open interest, avec un exemple.
6. Le prix monte et l'OI baisse. Quelle est la lecture habituelle ?
7. Pourquoi notre historique d'OI ne remonte-t-il qu'à un mois ?
8. Le funding est très positif depuis 2 semaines. Est-ce un signal de vente ? Pourquoi ?

## 📚 Sources
- Binance, *Introduction to Binance Futures Funding Rates* : [FAQ officielle](https://www.binance.com/en/support/faq/introduction-to-binance-futures-funding-rates-360033525031) (intervalle 8 h, qui paie qui, 0,01 % par période, pas de frais Binance).
- Binance Academy, *What Is Open Interest?* : [article](https://www.binance.com/id/academy/articles/what-is-open-interest).
- Binance, documentation API *Open Interest Statistics* : [« Only the data of the latest 1 month is available »](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Open-Interest-Statistics).
- Nos chiffres : `Outil/donnees/BTC-USDT_funding.csv` et `BTC-USDT_oi_1h.csv`, téléchargés le 13/11/2026.

## 📒 Mots à ajouter au [[Glossaire]]
Contrat perpétuel · Long · Short · Effet de levier · Funding rate · Open interest · Liquidation
