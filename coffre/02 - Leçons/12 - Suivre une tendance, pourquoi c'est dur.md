---
type: lecon
date: 2026-11-16
semaine: Stratégies
theme: Suivi de tendance
maitrise: 
---
# 📖 Suivre une tendance : pourquoi c'est dur

## 🧩 L'idée en une phrase
Suivre une tendance (acheter ce qui monte, vendre ce qui baisse) est l'une des stratégies **les mieux documentées** de la finance, sur plus d'un siècle. Mais elle perd **plus souvent qu'elle ne gagne**, traverse de **longues périodes creuses**, et ne marche bien qu'avec **beaucoup de marchés** et des horizons de **plusieurs mois**. Nos deux cassures l'ont appris à leurs dépens.

> Durée : 1 séance. Prérequis : leçons 09 (coûts) et 11 (contexte macro).

---

## 1. Ce que veut dire « suivre une tendance »
- **Momentum de série temporelle** (*time series momentum*) : si un marché a monté sur les 12 derniers mois, on l'achète ; s'il a baissé, on le vend. On regarde chaque marché **par rapport à son propre passé**.
- **Cassure de canal** : on achète quand le prix sort au-dessus du plus haut des N dernières bougies. C'est la version de nos idées *cassure 4 h* et *cassure journalière*.
- Les deux misent sur la même chose : un mouvement commencé a tendance à **continuer un moment**.

## 2. Ce que dit la recherche
- **Moskowitz, Ooi et Pedersen (2012, *Journal of Financial Economics*)** : sur **58 marchés à terme liquides** (indices d'actions, devises, matières premières, obligations), les rendements **persistent de 1 à 12 mois**, puis s'inversent en partie sur des horizons plus longs. Un portefeuille diversifié sur toutes ces classes d'actifs obtient des rendements anormaux importants, et fait **le mieux pendant les marchés extrêmes**.
- **Hurst, Ooi et Pedersen (2017, *Journal of Portfolio Management*)** : en reconstruisant la stratégie jusqu'en **1880**, elle a été « constamment rentable sur les 110 années suivantes ».
- **Lempérière, Deremble, Seager, Potters et Bouchaud (2014, *Journal of Investment Strategies*)** : sur des données depuis **1800**, la statistique t des tendances vaut environ **10** (environ **5** depuis 1960). Mais : les **tendances longues** ne faiblissent pas, alors que les **tendances courtes ont nettement faibli**.

## 3. Pourquoi c'est dur quand même
1. **On perd souvent.** Une cassure coupe vite ses pertes et laisse courir ses gains : beaucoup de petites pertes, quelques gros gains. Notre cassure journalière n'a gagné que **42 %** de ses trades.
2. **Les périodes creuses sont longues.** Résumé de l'étude d'AQR par Alpha Architect : jusqu'à **25 % de pertes** sur des périodes prolongées, et la pire décennie (à partir de 1910) n'a rapporté que **1,6 %** par an. Entre janvier 2009 et juin 2013, l'indice *SG CTA Trend* a fait **−0,8 %** par an.
3. **Après une crise, c'est souvent faible.** Hutchinson et O'Brien (2014), cités par Alpha Architect : dans les 24 mois qui suivent le début d'une crise, **4,0 %** par an en moyenne contre **13,6 %** hors crise.
4. **Il faut beaucoup de marchés.** Les études utilisent des dizaines de marchés de classes différentes. Nous avions **1** marché (cassure 4 h), puis **3** cryptos très liées entre elles (cassure journalière). Quand BTC, ETH et SOL tombent ensemble, la diversification ne protège pas.
5. **Les tendances courtes ont faibli** (Lempérière et al.). Une tendance sur 4 heures est très courte, et les coûts (0,30 % aller-retour) pèsent lourd sur un petit mouvement (leçon 09).
6. **Elle ne marche que quand il y a une tendance.** Logique, mais ça veut dire perdre pendant tout le temps où le marché est calme ou en panique.

## 4. Ce que nos tests ont montré
| Idée | Trades | Espérance / trade | Statistique t | Selon le contexte (leçon 11) |
|---|---|---|---|---|
| Cassure 4 h (BTC) | 259 | +0,12 % | 0,53 | Gain seulement pendant les annonces et en marché calme |
| Cassure journalière (BTC, ETH, SOL) | 156 | +0,38 % | 0,38 | **+2,31 %** en tendance, −0,67 % en calme, −5,16 % en panique |

Lecture : passer de 4 heures à 1 jour a amélioré l'espérance, comme la recherche le laisse attendre (tendances plus longues, coûts moins lourds). Mais **3 marchés** et **3 ans** ne suffisent pas pour distinguer un vrai effet du hasard (t très loin de 2,0).

## 5. Ce qu'on en retient pour la suite
- Viser des horizons **longs** (semaines à mois), là où la recherche trouve l'effet et où les coûts pèsent moins de 10 % du mouvement.
- Accepter qu'une stratégie de tendance **perde souvent** : juger sur l'espérance et le drawdown, pas sur le taux de réussite.
- Toute idée « seulement en tendance » ou « plus long » doit être écrite **comme une nouvelle idée, avant le test**, et compter ses variantes. Pas de retouche des idées archivées.

---

## 🧠 Quiz (mes réponses)
1. Quelle différence entre momentum de série temporelle et cassure de canal ?
2. Sur combien de marchés et quels horizons Moskowitz, Ooi et Pedersen trouvent-ils la persistance ?
3. Qu'ont trouvé Lempérière et al. sur les tendances courtes et longues ?
4. Pourquoi une stratégie de tendance peut-elle être bonne avec seulement 42 % de trades gagnants ?
5. Pourquoi 3 cryptos ne suffisent-elles pas à diversifier une stratégie de tendance ?
6. Pourquoi notre cassure 4 h partait-elle avec un handicap ?

## 📚 Sources
- Moskowitz, T. J., Ooi, Y. H., Pedersen, L. H. (2012), *Time Series Momentum*, **Journal of Financial Economics** 104(2), 228-250. [SSRN 2089463](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463).
- Hurst, B., Ooi, Y. H., Pedersen, L. H. (2017), *A Century of Evidence on Trend-Following Investing*, **Journal of Portfolio Management** (automne 2017). [AQR](https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing).
- Lempérière, Y., Deremble, C., Seager, P., Potters, M., Bouchaud, J.-P. (2014), *Two centuries of trend following*, **Journal of Investment Strategies**. [Fiche RePEc](https://ideas.repec.org/a/rsk/journ6/2349968.html) · [version arXiv](https://ar5iv.arxiv.org/html/1404.3274).
- Alpha Architect, *Time Series Momentum (aka Trend-Following): The Historical Evidence* (résumé de l'étude AQR, chiffres de drawdown, de la pire décennie, de l'indice SG CTA Trend et de Hutchinson et O'Brien 2014) : [article](https://alphaarchitect.com/time-series-momentum-aka-trend-following-the-historical-evidence/). Source secondaire.
- Nos chiffres : registre `Outil/registre_variantes.json`, rapports `Outil/rapports_backtest/cassure_*` et `contexte_cassure_*`.

## 🎧 Écouter
Épisode 12 du podcast *Cerveau trading* : [écouter sur le téléphone](https://lauris-ad.github.io/cerveau-trading/index.html#e12).

## 📒 Mots à ajouter au [[Glossaire]]
Momentum de série temporelle · Cassure de canal · Taux de réussite · Période creuse · CTA · Diversification
