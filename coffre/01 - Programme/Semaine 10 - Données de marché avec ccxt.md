---
type: semaine
semaine: 10
theme: Données de marché avec ccxt
---
# Semaine 10 : Données de marché avec ccxt

## 🎯 Objectifs
- Récupérer des bougies (OHLC) depuis un exchange avec la librairie `ccxt`, sans compte.
- Calculer en Python l'amplitude moyenne et l'ATR (ce que j'ai déjà fait à la main au début).
- Ajouter une note « Marché » mise à jour automatiquement, et une alerte volatilité.

## 📅 Planning
| Jour | 📚 Connaissances | 🛠️ Pratique / 🏗️ Construction |
|---|---|---|
| J1 | Données publiques vs données privées d'un exchange | Installer `ccxt` et `pandas` |
| J2 | Le format OHLCV | Script : 30 dernières bougies journalières BTC/USDT |
| J3 | `pandas` : tableaux de données | Calculer l'amplitude de chaque bougie |
| J4 | L'ATR | Calculer l'ATR 14 et le comparer à mon calcul à la main |
| J5 | — | Note `Marché BTC.md` générée : prix, amplitude, ATR, stop suggéré |
| J6 | — | Alerte Telegram si l'amplitude du jour dépasse 2 × la moyenne |
| J7 | Quiz + révision | Vérifier 2 bougies à la main sur TradingView |

## ✅ Tâches
- [ ] `ccxt` et `pandas` installés
- [ ] Script de bougies fonctionnel
- [ ] Amplitude moyenne et ATR calculés et vérifiés
- [ ] Note « Marché BTC » générée automatiquement
- [ ] Alerte de volatilité branchée sur le bot
- [ ] Quiz de la semaine fait

## 📦 Livrable
Mon bot surveille maintenant les wallets **et** le marché.
