---
type: lecon
date: 2026-11-19
semaine: Discord Dualis Flow
theme: Order flow
maitrise: 
---
# 📖 Le DOM et le spoofing : pourquoi le carnet affiché ment

## 🧩 L'idée en une phrase
Le **DOM** montre les ordres **en attente**, qui peuvent disparaître à tout moment. Les **trades exécutés** ne s'effacent pas. Quand les deux se contredisent, on croit ce qui a été exécuté.

> Durée : 15 min. Prérequis : [[15 - Delta, absorption et footprint]]. Contexte : synthèse du Discord Dualis Flow (17/11), section 2.3.

---

## 1. Ce qu'est le DOM
DOM veut dire *depth of market* : le **carnet d'ordres** en direct. On y voit, prix par prix, les ordres d'achat en attente (**bid**) et de vente en attente (**ask**).

- Un ordre dans le carnet est une **intention**. Son auteur peut l'annuler en une fraction de seconde.
- Un trade exécuté est un **fait** : quelqu'un a vraiment acheté et quelqu'un a vraiment vendu.

C'est pour ça que Dualis Flow dit : pour lire une absorption, **le footprint (trades exécutés) vaut mieux que le DOM**. Le DOM sert surtout de **confirmation en scalping**.

## 2. L'absorption vue au DOM
Ce que Dualis Flow regarde :
- du volume agressif qui **s'empile** sur un prix **sans que le niveau casse** ;
- une liquidité affichée qui **se recharge** au lieu de fondre (on parle d'ordre « iceberg » quand un gros ordre ne montre qu'une petite partie de sa taille).

Ils ne donnent **pas de seuil précis**. Un membre cite « 2,5 fois plus de contrepartie, 2 ticks de baisse », sans preuve.

## 3. Le spoofing : un ordre fait pour tromper
**Spoofer**, c'est poser un gros ordre qu'on **n'a pas l'intention d'exécuter**, pour faire croire à de l'offre ou de la demande, puis l'annuler avant qu'il soit touché.

C'est **interdit** aux États-Unis depuis la loi **Dodd-Frank** (2010), qui l'a ajouté au Commodity Exchange Act. Deux affaires connues :
- **Navinder Sarao**, trader britannique, a utilisé des ordres de vente géants sur le future E-mini S&P 500, notamment le jour du *flash crash* du 6 mai 2010. Arrêté en 2015, il a plaidé coupable en 2016.
- **JPMorgan** a payé environ **920 millions de dollars** en septembre 2020 pour du spoofing de ses traders sur les métaux précieux et les obligations d'État américaines (CFTC, ministère de la Justice, SEC).

Si de grandes banques se sont fait prendre, des ordres affichés trompeurs existent forcément ailleurs, et la crypto est bien moins surveillée.

## 4. Exemple fictif
*Chiffres inventés.* Le BTC est à 65 000 $. Le DOM affiche un mur de **400 BTC** à l'achat à 64 900 $. Beaucoup de traders achètent en pensant « ça va rebondir dessus ».

Le prix descend vers 64 900 $… et le mur **disparaît** à 64 920 $. Personne ne l'a touché. Le prix traverse 64 900 $.

Ce que montrait le footprint pendant ce temps : un delta **négatif** à chaque bougie, des ventes agressives exécutées. Le fait (les ventes) disait l'inverse de l'affichage (le mur).

## 5. Ce qu'on en fait chez nous
- On n'a **pas** de DOM historique gratuit pour faire un backtest : rien de ce qui précède n'est mesuré chez nous.
- On a en revanche les **trades exécutés** gratuits de Binance (aggTrades). C'est notre source pour le delta et le CVD (tâche 34 du backlog).
- Mesure récente : au cycle 34, la divergence du CVD (idée H8) en bougies de 1 h sur BTC a **perdu même avant frais** (383 trades). Les trades exécutés sont des faits, mais un fait n'est pas forcément un signal.

---

## 🧠 Quiz (mes réponses)
1. Quelle est la différence entre un ordre dans le DOM et un trade exécuté ?
2. Pour lire une absorption, Dualis Flow préfère-t-il le DOM ou le footprint, et pourquoi ?
3. Qu'est-ce que le spoofing ?
4. Quelle loi l'a interdit explicitement aux États-Unis, et en quelle année ?
5. Un mur de 400 BTC disparaît juste avant d'être touché : qu'est-ce que ça peut être, et que regardes-tu à la place ?
6. Pourquoi ne peut-on pas backtester une règle de DOM chez nous, alors qu'on peut tester le CVD ?

## 📚 Sources
- Dodd-Frank Wall Street Reform and Consumer Protection Act (2010), section 747, qui ajoute l'interdiction du spoofing au Commodity Exchange Act, section 4c(a)(5)(C).
- CFTC et ministère de la Justice américain : affaire Navinder Singh Sarao (plainte 2015, plaidoyer de culpabilité 2016).
- CFTC, communiqué de septembre 2020 : JPMorgan, environ 920 millions de dollars pour spoofing (métaux précieux, Treasuries).
- Synthèse Dualis Flow : `Stratégies Discord - Dualis Flow.md`, section 2.3. Résultat H8 : `JOURNAL.md`, cycle 34.

## 🎧 Écouter
Épisode 36 du podcast *Cerveau trading* : débloqué quand la leçon 35 sera validée.

## 📒 Mots à ajouter au [[Glossaire]]
DOM · Bid, ask · Ordre iceberg · Spoofing
