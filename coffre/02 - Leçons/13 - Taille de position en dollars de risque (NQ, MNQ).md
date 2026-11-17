---
type: lecon
date: 2026-11-17
semaine: Veille du 17/11
theme: Gestion du risque sur futures
maitrise: 
---
# 📖 Taille de position en dollars de risque (NQ, MNQ)

## 🧩 L'idée en une phrase
On ne choisit pas un nombre de contrats : on choisit **combien de dollars on accepte de perdre**, on place le stop là où l'idée est fausse, et **le nombre de contrats se déduit** des deux.

> Durée : 30 min. Prérequis : leçon 03 (amplitude et taille de position). Source de la veille : Dualis Flow (TikTok, 17/11).

---

## 1. La formule
**contrats = risque en $ ÷ (distance du stop en points × valeur d'un point)**

On arrondit **toujours vers le bas** : 4,7 contrats, c'est 4.

## 2. Les deux contrats du Nasdaq-100 (chiffres officiels CME)
| Contrat | Valeur d'un point | Plus petit pas (tick) | Valeur d'un tick |
|---|---|---|---|
| **NQ** (E-mini Nasdaq-100) | **20 $** | 0,25 point | 5 $ |
| **MNQ** (Micro E-mini Nasdaq-100) | **2 $** | 0,25 point | 0,50 $ |

Un MNQ, c'est **un dixième** d'un NQ. Exemple pour fixer les idées (chiffre inventé pour l'exemple) : avec l'indice à 20 000 points, un NQ « pèse » 400 000 $ et un MNQ 40 000 $. C'est pour ça qu'un petit compte ne peut travailler qu'en MNQ.

## 3. Exemples
- Risque **150 $**, stop à **15 points**, **MNQ** : 15 × 2 = 30 $ par contrat → 150 ÷ 30 = **5 MNQ**.
- Même risque, même stop, **NQ** : 15 × 20 = 300 $ par contrat, plus que 150 $ → **0 NQ**. On passe au MNQ ou on ne prend pas le trade.
- Risque 150 $, stop à **30 points**, MNQ : 30 × 2 = 60 $ → **2 MNQ** (2,5 arrondi vers le bas).

**Stop plus large = moins de contrats pour le même risque.** Le stop se place d'abord, là où l'idée devient fausse ; jamais resserré juste pour « rentrer » plus gros.

## 4. Dans nos outils
- Dashboard, carte **Taille de position** : boutons **Crypto / NQ / MNQ**. En mode NQ ou MNQ, tu entres le risque en $ et le stop en points ; la carte donne le nombre de contrats et le risque réel après arrondi.
- Astuce de la vidéo, sur TradingView : enregistrer des modèles de l'outil *Long/Short Position* (taille du compte, risque en cash) pour ne jamais recalculer à la main.

## 5. Ce qu'on en retient
- Le risque se décide **avant** le trade, en $, et reste le même d'un trade à l'autre.
- On ne trade toujours **pas d'argent réel** : cette leçon sert au paper trading et à lire correctement les vidéos.

---

## 🧠 Quiz (mes réponses)
1. Risque de 150 $, stop de 15 points sur MNQ : combien de contrats ?
2. Combien vaut un point de NQ ? Et un tick de MNQ ?
3. Pourquoi arrondit-on vers le bas ?
4. Ton stop s'élargit de 15 à 30 points, risque inchangé : que devient la taille ?

## 📚 Sources
- **CME Group**, spécifications du Micro E-mini Nasdaq-100 (MNQ) : [cmegroup.com](https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.html). Détail relayé par MetroTrade : « $2 × Nasdaq-100 Index », tick 0,25 = 0,50 $ : [help.metrotrade.com](https://help.metrotrade.com/kb/micro-e-mini-nasdaq-100-futures-mnq-contract-specifications). Le NQ vaut 10 fois le MNQ, soit 20 $ par point.
- Veille TikTok du 17/11 (Dualis Flow, « taille de position ») : `Veille TikTok - 17-11-2026.md`.

## 🎧 Écouter
Épisode 13 du podcast *Cerveau trading* : [écouter sur le téléphone](https://lauris-ad.github.io/cerveau-trading/index.html#e13) (débloqué quand tu y arrives).

## 📒 Mots à ajouter au [[Glossaire]]
Contrat future · NQ · MNQ · Point · Tick · Risque en dollars
