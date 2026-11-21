---
type: lecon
date: 2026-11-21
semaine: Méthode
theme: Backtest honnête
maitrise: 
---
# 📖 Battre le hasard : le contrôle témoin

## 🧩 L'idée en une phrase
Une stratégie qui gagne n'a pas forcément un avantage : elle a peut-être juste acheté pendant que **tout** montait. Pour le savoir, on la compare à **les mêmes trades placés au hasard**.

> Durée : 15 min. Prérequis : [[Fiche - Backtest honnête]] et [[09 - Les coûts, le vrai adversaire]]. Fichier : `CONTROLE-TEMOIN.md` (cycle 38).

---

## 1. Le piège du marché qui monte
Entre fin 2022 et l'été 2025, le BTC est passé d'environ 16 000 $ à plus de 100 000 $. Sur une telle période, presque **n'importe quel achat** tenu quelques semaines gagne. Une stratégie acheteuse peut donc afficher de beaux chiffres sans rien savoir faire.

## 2. Le contrôle témoin
On garde les trades de la stratégie **tels quels** : même marché, même sens (achat ou vente), même durée. On change une seule chose : la **date d'entrée**, tirée au hasard. On recommence **2 000 fois**.
- Si la stratégie fait mieux que **95 %** des tirages, son choix de dates apporte quelque chose.
- Sinon, son gain s'explique aussi bien par le hasard et la tendance du marché.

## 3. Ce que ça a donné chez nous (cycle 38)
| Idée | Gain moyen | Mêmes trades au hasard | Verdict du contrôle |
|---|---|---|---|
| Cassure hebdomadaire (8 cryptos) | +7,31 % | +2,05 % | **passe** (bat 97,6 % des tirages) |
| Cassure journalière en tendance | +1,31 % | +0,19 % | échoue (12 % des tirages font mieux) |
| Cassure journalière | +0,38 % | +0,14 % | échoue |

La cassure hebdomadaire reste **archivée** : elle n'avait que 93 trades au lieu des 100 exigés. Un contrôle réussi ne rattrape pas un critère raté.

## 4. Le deuxième piège : essayer beaucoup d'idées
Si on teste 20 idées sans valeur, l'une d'elles finira par sortir un beau chiffre **par chance**. C'est le « data snooping ».
- Halbert White (2000) a proposé un test pour corriger ce biais quand on a essayé beaucoup de règles.
- Harvey, Liu et Zhu (2016) recommandent d'exiger une statistique t d'au moins **3** plutôt que 2 pour une nouvelle découverte.
- Bailey et López de Prado (2014) proposent de « dégonfler » le ratio de Sharpe selon le nombre d'essais.

Chez nous, c'est pourquoi on **compte les variantes** : le t exigé monte de 2,0 à 3,3 avec le nombre d'essais (`CRITERES.md`).

## 5. Ce qu'il faut retenir
1. Un gain doit battre le **hasard à exposition égale**, pas zéro.
2. Plus on a essayé d'idées, plus la barre doit être haute.
3. Les règles s'écrivent **avant** le test, sinon on finit toujours par trouver ce qu'on cherche.

---

## 🧠 Quiz (mes réponses)
1. Pourquoi une stratégie acheteuse peut-elle gagner sans avoir d'avantage ?
2. Que change le contrôle témoin, et que garde-t-il identique ?
3. Quand dit-on qu'une idée passe le contrôle témoin ?
4. La cassure hebdomadaire passe le contrôle : pourquoi reste-t-elle archivée ?
5. Qu'est-ce que le data snooping ?
6. Pourquoi le t exigé monte-t-il avec le nombre de variantes ?

## 📚 Sources
- Halbert White, « A Reality Check for Data Snooping », *Econometrica*, 2000.
- Campbell Harvey, Yan Liu et Heqing Zhu, « … and the Cross-Section of Expected Returns », *Review of Financial Studies*, 2016.
- David Bailey et Marcos López de Prado, « The Deflated Sharpe Ratio », *Journal of Portfolio Management*, 2014.
- Nos chiffres : `CONTROLE-TEMOIN.md` et journal, cycles 36 et 38.

## 🎧 Écouter
Épisode 38 du podcast *Cerveau trading* : débloqué quand la leçon 37 sera validée.

## 📒 Mots à ajouter au [[Glossaire]]
Contrôle témoin · Data snooping · Statistique t
