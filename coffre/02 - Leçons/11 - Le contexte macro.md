---
type: lecon
date: 2026-11-16
semaine: Stratégies
theme: Contexte macro et régimes de marché
maitrise: 
---
# 📖 Le contexte macro

## 🧩 L'idée en une phrase
Les marchés ne bougent pas pareil tous les jours : certains jours, la **Fed**, l'**inflation** ou un **choc** (faillite, guerre) secouent tout ; et certaines périodes sont **calmes**, d'autres en **tendance**, d'autres en **panique**. Une stratégie qui ne gagne que dans **un seul** de ces contextes gagne peut-être **par hasard**, et peut s'arrêter du jour au lendemain.

> Durée : 1 séance d'une heure. Prérequis : leçon 09 et la fiche *Backtest honnête*.

---

## 1. Les rendez-vous qui font bouger les marchés
Ce sont des annonces **programmées à l'avance**, à heure fixe, publiées par des institutions officielles.

| Rendez-vous | Qui publie | Quand | Heure de Paris (hiver) |
|---|---|---|---|
| **Décision de taux de la Fed** (FOMC) | Réserve fédérale américaine | 8 fois par an, 2e jour de la réunion | 20 h 00 (14 h à New York) |
| **Inflation américaine** (CPI) | BLS, bureau des statistiques du travail | 1 fois par mois | 14 h 30 (8 h 30 à New York) |
| **Emploi américain** (Employment Situation, « NFP ») | BLS | En général le 1er vendredi du mois | 14 h 30 |
| **Décision de taux de la BCE** | Banque centrale européenne | Environ toutes les 6 semaines | 14 h 15 |

**Pourquoi ça compte.** Le taux de la Fed fixe le « prix de l'argent ». Si l'inflation surprend à la hausse, les marchés anticipent des taux plus hauts, et les actifs risqués (actions, crypto) baissent souvent. Le prix réagit **en quelques secondes**.

**Ce que dit la recherche.**
- Savor et Wilson (2013, *Journal of Financial and Quantitative Analysis*) : de 1958 à 2009, les jours d'annonce d'**inflation, de chômage ou de taux**, les actions américaines ont gagné en moyenne **0,114 %** de plus que le taux sans risque, contre **0,011 %** les autres jours. Plus de **60 %** de la prime annuelle des actions a été gagnée ces jours-là.
- Lucca et Moench (2015, *Journal of Finance*) : les actions américaines montent en moyenne fortement **avant** les décisions programmées de la Fed (le « pre-FOMC drift »). Les autres annonces ne produisent pas cet effet.

Conséquence pour nous : une stratégie peut sembler gagnante seulement parce qu'elle était, par chance, en position ces jours-là.

---

## 2. Les chocs
Ce sont des événements **non programmés**. Notre liste (2022-2025), chaque date avec sa source :
- 08-11/11/2022 : faillite de **FTX** (crypto).
- 10-13/03/2023 : fermeture de **Silicon Valley Bank**, l'USDC perd brièvement sa parité.
- 07/10/2023 : attaque du **Hamas** contre Israël.
- 10/01/2024 : feu vert de la SEC aux **ETF bitcoin** au comptant.
- 05/08/2024 : krach mondial, le Nikkei perd **12,4 %** en un jour (sortie du « carry trade » sur le yen).
- 02-09/04/2025 : **droits de douane** américains, puis pause de 90 jours.
- 13-23/06/2025 : guerre **Israël-Iran**, frappes américaines le 22/6.
- 10-11/10/2025 : menace de droits de douane sur la Chine, **19 Md$** de positions crypto liquidées, un record.

La liste est dans `Outil/evenements_macro.csv` (139 lignes : 34 décisions de la Fed, 49 publications d'inflation, 48 d'emploi, 8 chocs). Elle est **écrite à la main** : il manque forcément des chocs, et on l'enrichira.

---

## 3. Les régimes de marché
Un **régime**, c'est l'« humeur » du marché sur plusieurs semaines. On en compte trois, avec des règles simples, écrites **avant** de regarder les résultats :

| Régime | Règle (bougies journalières, la veille du trade) | Image |
|---|---|---|
| **Panique** | Volatilité sur 20 jours dans les 20 % les plus hautes **et** prix en baisse sur 20 jours | Tempête |
| **Tendance** | Le prix a bougé de plus d'un « écart normal » sur 20 jours | Rivière qui coule |
| **Calme** | Le reste | Lac |

Les chercheurs le constatent depuis longtemps : Ang et Bekaert (2002, *Review of Financial Studies*) trouvent un régime où **volatilité et corrélations augmentent** dans les mauvaises périodes. Quand tout baisse en même temps, la diversification protège moins.

**Analogie.** Un skieur qui ne réussit que sur neige fraîche n'est pas forcément bon : il faut le voir aussi sur glace et dans le brouillard.

---

## 4. Notre contrôle « contexte »
Il **s'ajoute** aux critères gelés de `CRITERES.md` (aucun seuil ne change). Une idée qui a passé le backtest doit en plus :
1. **Gagner hors événements** : espérance > 0 sur les trades qui ne touchent aucune fenêtre (2 h avant à 24 h après une annonce, ou les jours d'un choc).
2. **Gagner dans au moins 2 régimes** parmi ceux qui ont au moins 20 trades.

Outil : `py controle_contexte.py`. Détail des règles : `CONTROLE-CONTEXTE.md`.

---

## 5. Ce que ça change sur nos 5 idées archivées
| Idée | Tous les trades | Hors événements | Calme | Tendance | Panique |
|---|---|---|---|---|---|
| Cassure 4 h | +0,12 % (259) | **−0,08 %** | **+0,48 %** (155) | −0,35 % (85) | −0,68 % (14) |
| Cassure journalière BTC+ETH+SOL | +0,38 % (156) | +0,54 % | −0,67 % (81) | **+2,31 %** (67) | −5,16 % (8) |
| Funding extrême | −0,08 % (96) | −0,26 % | +0,52 % (40) | −0,58 % (39) | −0,36 % (16) |
| Fair value gap | −0,36 % | −0,35 % | −0,38 % | −0,34 % | −0,26 % |
| Pic de volatilité (suivre) | −0,32 % | −0,33 % | −0,31 % | −0,26 % | −0,72 % |

Espérance par trade après coûts (nombre de trades entre parenthèses).

**Lecture.**
- La **cassure 4 h**, notre première idée positive, **ne gagnait que grâce aux événements** (+0,67 % sur les 69 trades exposés, −0,08 % sur les autres) et seulement en marché **calme**. Même si elle avait passé le backtest, ce contrôle l'aurait arrêtée.
- La **cassure journalière** ne dépend pas des événements, mais **ne gagne qu'en tendance** : elle perd en marché calme et en panique. C'est logique pour une stratégie de cassure, et c'est une piste : une future idée pourrait **n'agir qu'en tendance**, à condition d'écrire cette règle **avant** le test, comme une nouvelle idée.
- Les trois autres perdent dans **tous** les contextes : les coûts dominent partout.
- Aucun verdict ne change (les 5 restent archivées), mais on comprend **pourquoi** elles ont échoué.

---

## 🧠 Quiz (mes réponses)
1. Cite trois rendez-vous programmés qui font bouger les marchés, et qui les publie.
2. À quelle heure de Paris tombent les chiffres d'inflation américains en hiver ?
3. Que montrent Savor et Wilson (2013) sur les jours d'annonce ?
4. Qu'est-ce que le « pre-FOMC drift » de Lucca et Moench (2015) ?
5. Quels sont nos trois régimes, et comment reconnaît-on la panique ?
6. Pourquoi une stratégie qui ne gagne qu'en régime calme est-elle fragile ?
7. Quelles sont les deux conditions du contrôle « contexte » ?
8. Pourquoi la cassure 4 h aurait-elle échoué au contrôle même si elle avait passé le backtest ?

## 📚 Sources
- **Réserve fédérale**, calendrier des réunions du FOMC : [federalreserve.gov](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm).
- **BLS**, archives des publications de l'inflation (CPI) : [bls.gov](https://www.bls.gov/bls/news-release/cpi.htm) et calendrier : [bls.gov](https://www.bls.gov/schedule/news_release/cpi.htm) (« All releases are scheduled for 08:30 AM »).
- **BLS**, archives de l'emploi (Employment Situation) : [bls.gov](https://www.bls.gov/bls/news-release/empsit.htm). Pas de rapport pour le mois d'octobre 2025 (interruption des financements fédéraux).
- **BCE**, calendrier des réunions du Conseil des gouverneurs : [ecb.europa.eu](https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.fr.html).
- Savor, P., Wilson, M. (2013), *How Much Do Investors Care About Macroeconomic Risk? Evidence from Scheduled Economic Announcements*, **Journal of Financial and Quantitative Analysis** 48(2), 343-375. [Fiche RePEc](https://ideas.repec.org/a/cup/jfinqa/v48y2013i02p343-375_00.html).
- Lucca, D., Moench, E. (2015), *The Pre-FOMC Announcement Drift*, **Journal of Finance** 70(1), 329-371. [Fiche RePEc](https://ideas.repec.org/a/bla/jfinan/v70y2015i1p329-371.html).
- Ang, A., Bekaert, G. (2002), *International Asset Allocation With Regime Shifts*, **Review of Financial Studies** 15(4), 1137-1187. [Fiche RePEc](https://ideas.repec.org/a/oup/rfinst/v15y2002i4p1137-1187.html).
- Chocs : [FDIC, fermeture de SVB](https://www.fdic.gov/news/press-releases/2023/pr23016.html) · [Al Jazeera, faillite de FTX](https://www.aljazeera.com/economy/2022/11/11/distressed-crypto-exchange-ftx-files-for-bankruptcy) · [Axios, ETF bitcoin](https://www.axios.com/2024/01/10/sec-approves-spot-bitcoin-etfs-after-much-hype) · [Fortune, krach du 5/8/2024](https://fortune.com/2024/08/05/5-reasons-stocks-down-global-stock-market-rout/) · [TT News, pause des droits de douane](https://www.ttnews.com/articles/trump-pauses-tariffs) · [PBS, guerre Israël-Iran](https://www.pbs.org/newshour/world/what-to-know-about-the-u-s-militarys-intervention-in-the-israel-iran-war) · [PYMNTS, liquidations du 10/10/2025](https://www.pymnts.com/cryptocurrency/2025/tariffs-trigger-record-19-billion-in-crypto-liquidations/) · [Wikipédia, attaque du 7 octobre](https://en.wikipedia.org/wiki/October_7_attacks).
- Nos chiffres : `Outil/rapports_backtest/contexte_*.md` et `contexte_resume.json`, calculés le 16/11/2026.

## 🎧 Écouter
Épisode 11 du podcast *Cerveau trading* : [écouter sur le téléphone](https://lauris-ad.github.io/cerveau-trading/index.html#e11).

## 📒 Mots à ajouter au [[Glossaire]]
FOMC · CPI · NFP · BCE · Choc · Régime de marché · Volatilité réalisée · Fenêtre d'événement
