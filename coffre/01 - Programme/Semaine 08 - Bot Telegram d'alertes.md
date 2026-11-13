---
type: semaine
semaine: 8
theme: Bot Telegram d'alertes
---
# Semaine 08 : Bot Telegram d'alertes

## 🎯 Objectifs
- Créer mon bot Telegram et lui faire envoyer des messages.
- Brancher la watchlist : alerte quand un wallet surveillé fait un mouvement important.
- Le faire tourner automatiquement.

## 📅 Planning
| Jour | 📚 Connaissances | 🛠️ Pratique / 🏗️ Construction |
|---|---|---|
| J1 | Comment marche un bot Telegram | Créer le bot avec @BotFather, récupérer le token |
| J2 | Sécurité : token du bot dans `.env` | Script : envoyer « Bonjour » sur mon téléphone |
| J3 | Formater un message clair | Message d'alerte : wallet, montant, lien Etherscan |
| J4 | — | Brancher `watchlist.py` → alerte Telegram |
| J5 | Éviter le spam d'alertes (seuils, doublons) | Ne pas renvoyer deux fois la même alerte |
| J6 | Lancer un script automatiquement | Planificateur de tâches Windows : toutes les 15 min |
| J7 | Quiz + révision | Laisser tourner 24 h et noter ce qui se passe |

## ✅ Tâches
- [ ] Bot créé, token rangé dans `.env`
- [ ] Message de test reçu sur mon téléphone
- [ ] Alerte réelle reçue pour un mouvement de wallet
- [ ] Pas de doublons d'alertes
- [ ] Script lancé automatiquement
- [ ] Quiz de la semaine fait

## ⚠️ Règle
Ce bot **observe et alerte**. Il ne passe **aucun** ordre et n'a accès à **aucun** fonds.

## 📦 Livrable
Mon premier bot : une alerte Telegram quand un wallet de ma watchlist bouge.
