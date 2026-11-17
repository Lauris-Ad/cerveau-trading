---
type: lecon
date: 2026-11-17
semaine: Veille du 17/11
theme: Liquidité et niveaux
maitrise: 
---
# 📖 La liquidité : version ICT et version recherche

## 🧩 L'idée en une phrase
Au-dessus des plus hauts visibles dorment des **ordres d'achat en attente** (stops des vendeurs, entrées sur cassure) : c'est la **liquidité côté acheteur**. Sous les plus bas, la **liquidité côté vendeur**. Le prix va souvent les chercher, et la recherche montre que ces ordres se **regroupent** autour de prix ronds.

> Durée : 40 min. Prérequis : leçons 02 (stop-loss) et 04 (carnet d'ordres). Sources de la veille : @tctrades_tyler, @limit.nq1 (TikTok, 17/11).

---

## 1. Le vocabulaire ICT
- **Buy-side liquidity (BSL)** : ordres d'achat en attente **au-dessus** d'un plus haut visible (stops des vendeurs, achats sur cassure). Lieux typiques : anciens plus hauts, **plus hauts égaux**, plus haut de la veille ou de la semaine.
- **Sell-side liquidity (SSL)** : le miroir, **sous** les plus bas.
- **Sweep (« balayage »)** : le prix traverse le niveau, déclenche les stops, **ne tient pas** et revient dans le range. S'il tient de l'autre côté, c'est une vraie cassure, pas un sweep.
- Message de @limit.nq1 : ICT donne **la zone**, l'orderflow (leçon 15) **confirme l'entrée**.

## 2. Ce que dit la recherche
Osler (2003, *Journal of Finance*), avec les premières données réelles d'ordres de change d'une banque :
- les ordres de **prise de profit** se regroupent fortement **sur** les chiffres ronds → explique les **rebonds** sur ces niveaux ;
- les **stop-loss** se regroupent juste **au-delà** des chiffres ronds → explique les **accélérations** une fois le niveau franchi.
C'est une base solide à l'idée de « liquidité » : les stops existent et se regroupent. En revanche, l'idée ICT qu'une « main invisible » va **chercher** ces stops exprès n'est pas démontrée.

## 3. Prudence
- Les vidéos ICT et TTrades sont de la **matière brute** : définitions utiles, mais aucune statistique publiée.
- Notre seule idée ICT testée, le **fair value gap**, a perdu **−0,36 %** par trade (archivée au cycle 10).
- Une idée « sweep du plus bas de la veille » serait à **pré-enregistrer** avant tout test (c'est proche de H3).

---

## 🧠 Quiz (mes réponses)
1. Où se trouve la buy-side liquidity, et de quoi est-elle faite ?
2. Quelle différence entre un sweep et une cassure ?
3. Qu'a trouvé Osler (2003) sur les prises de profit et les stop-loss ?
4. Quelle partie de l'idée ICT n'est pas démontrée ?

## 📚 Sources
- Osler, C. L. (2003), *Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis*, **Journal of Finance** 58(5), 1791-1819 : [fiche RePEc](https://ideas.repec.org/a/bla/jfinan/v58y2003i5p1791-1819.html) · [version Fed de New York](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.pdf).
- Définitions BSL / SSL / sweep : LuxAlgo, *Buy-side liquidity* : [luxalgo.com](https://www.luxalgo.com/library/concept/buy-side-liquidity/) (source secondaire).
- Vidéos citées par la veille : TTrades, *What is Liquidity? – ICT Concepts* ; The Inner Circle Trader, *2022 ICT Mentorship Episode 2* (YouTube, non vérifiées ici).

## 🎧 Écouter
Épisode 18 du podcast *Cerveau trading* : [écouter sur le téléphone](https://lauris-ad.github.io/cerveau-trading/index.html#e18).

## 📒 Mots à ajouter au [[Glossaire]]
Buy-side liquidity · Sell-side liquidity · Sweep · Plus hauts égaux · ICT
