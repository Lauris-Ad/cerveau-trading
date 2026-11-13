---
type: semaine
semaine: 4
theme: Python et API Etherscan
---
# Semaine 04 : Python et API Etherscan

## 🎯 Objectifs
- Comprendre ce qu'est une API et une clé API.
- Récupérer le solde d'un wallet avec Python.
- **Étape clé :** un script qui met à jour une fiche wallet d'Obsidian tout seul.

## 📅 Planning
| Jour | 📚 Connaissances | 🛠️ Pratique / 🏗️ Construction |
|---|---|---|
| J1 | Qu'est-ce qu'une API ? Format JSON | Créer un compte Etherscan + une clé API gratuite |
| J2 | Sécurité : clés API, fichier `.env`, ne jamais partager | Créer `.env` et le charger en Python |
| J3 | La librairie `requests` | Script : solde ETH de vitalik.eth |
| J4 | Lire et écrire un fichier en Python | Script : écrire le résultat dans une note `.md` |
| J5 | Le frontmatter (YAML) | Script : mettre à jour `solde_eth` et `derniere_maj` d'une fiche |
| J6 | Gérer les erreurs (try / except) | Faire tourner le script sur mes 3 fiches |
| J7 | Quiz + révision | Le Dashboard affiche des soldes à jour |

## ✅ Tâches
- [ ] Clé API Etherscan créée (lecture seule par nature : elle ne donne accès à aucun fonds)
- [ ] Fichier `.env` créé et **jamais** partagé ni envoyé à qui que ce soit
- [ ] Script `solde.py` qui affiche un solde
- [ ] Script `maj_wallets.py` qui met à jour les fiches dans `05 - Wallets`
- [ ] Le Dashboard affiche les soldes à jour
- [ ] Quiz de la semaine fait

## 📦 Livrable
Je lance un script, et mon Dashboard Obsidian se met à jour. C'est la première brique de mon bot.

## 💬 À demander à Claude
- « Semaine 4, jour 1 : explique-moi ce qu'est une API, puis guide-moi pour créer ma clé Etherscan »
