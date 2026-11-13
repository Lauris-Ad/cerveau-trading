---
type: semaine
semaine: 6
theme: Historique d'un wallet en Python
---
# Semaine 06 : Historique d'un wallet en Python

## 🎯 Objectifs
- Récupérer les transactions d'un wallet (ETH et tokens) avec l'API.
- Les présenter proprement dans la fiche wallet.
- Détecter automatiquement les gros transferts.

## 📅 Planning
| Jour | 📚 Connaissances | 🛠️ Pratique / 🏗️ Construction |
|---|---|---|
| J1 | Les listes de transactions dans l'API | Script : 10 dernières transactions ETH |
| J2 | Unités : wei → ETH, décimales des tokens | Convertir les montants correctement |
| J3 | Les dates (timestamp) | Afficher des dates lisibles |
| J4 | Transferts de tokens ERC-20 | Script : 10 derniers transferts de tokens |
| J5 | Construire un tableau Markdown en Python | Écrire l'historique dans la fiche wallet |
| J6 | Seuils et filtres | Signaler les transferts au-dessus de X ETH (🚨 dans la note) |
| J7 | Quiz + révision | Vérifier 3 transactions à la main sur Etherscan |

## ✅ Tâches
- [ ] Script `historique.py` fonctionnel
- [ ] Montants en ETH (pas en wei) et dates lisibles
- [ ] Transferts de tokens inclus
- [ ] Gros transferts signalés automatiquement
- [ ] 3 transactions vérifiées à la main (le script dit vrai)
- [ ] Quiz de la semaine fait

## 📦 Livrable
Fiches wallets avec un tableau d'activité récente généré automatiquement.
