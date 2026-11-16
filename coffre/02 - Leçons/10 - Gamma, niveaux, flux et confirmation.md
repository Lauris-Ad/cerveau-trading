---
type: lecon
date: 2026-11-16
semaine: Terminal ES/NQ
theme: Options et gamma
maitrise: 
---
# 📖 Gamma : niveaux, flux et confirmation

## 🧩 L'idée en une phrase
Une vidéo TikTok que tu m'as envoyée dit : **1)** tous les niveaux gamma ne se valent pas, garde ceux où l'open interest est le plus fort ; **2)** le GEX seul ne suffit pas, regarde dans quel sens va l'argent des options ; **3)** attends que le prix confirme avant d'entrer. Ces trois règles sont **raisonnables**, mais la vidéo ne montre **aucun résultat mesuré**. On les a donc ajoutées au dashboard et écrites comme une idée à tester, sans y croire d'avance.

> Prérequis : la leçon 07 (*Options et gamma, les bases*). Durée : 1 séance d'une heure.

---

## 1. Ce que montre la vidéo
| Règle | Ce qu'on voit à l'écran | Notre lecture |
|---|---|---|
| « Not every level is valid » | GEX net par strike sur QQQ ; le présentateur ne garde que les strikes « with the highest open interest » | Filtrer les niveaux par open interest |
| « GEX alone ≠ edge » | Courbes *Net Drift* des primes calls et puts sur QQQ et NDX, classement des tickers par primes haussières et baissières ; « don't fight the flow » | Ne pas trader contre le sens de l'argent |
| « Confirmation is a must » | Graphique du future NQ avec des zones et un ordre limite | Attendre que le prix réagisse avant d'entrer |

Ce que la vidéo **ne montre pas** : combien de trades, quel taux de réussite, quel gain moyen après frais. Sans ça, impossible de dire si la méthode est efficace. C'est exactement ce que notre échelle (idée → backtest → hors échantillon → paper → candidate) va mesurer.

---

## 2. Règle 1 : les niveaux « valides »
**Pourquoi l'open interest compte.** Le GEX d'un strike vaut gamma × open interest × 100 × prix² × 1 %. Un strike avec peu de contrats ouverts peut avoir un gros gamma (s'il est tout proche du prix et expire bientôt), mais très peu de couverture réelle derrière. Un strike avec beaucoup de contrats, c'est beaucoup de couverture à ajuster quand le prix s'en approche.

**Ce que dit la recherche.** Ni, Pearson et Poteshman (2005) montrent que, **les jours d'expiration**, les actions qui ont des options cotées clôturent plus souvent près d'un strike, avec un déplacement moyen d'au moins **0,165 %** du rendement. Ils l'attribuent à la couverture des teneurs de marché et à des manipulations de traders pour compte propre. C'est un effet **mesuré**, mais sur les jours d'expiration et sur des actions, pas une preuve que chaque grand strike arrête le SPX.

**Ce qu'on a codé (onglet Options, carte « Niveaux valides »).**
- Zone : ±5 % autour du prix.
- On garde les strikes dont l'open interest (calls + puts) est dans les **20 % les plus forts** de la zone.
- Parmi eux, les **5 plus gros GEX nets**, avec leur part dans tout le GEX de la zone.
- **Frein** = GEX net positif (en théorie, les dealers freinent le prix). **Accélérateur** = GEX net négatif (en théorie, ils amplifient).

**Exemple réel, SPX le 13/11/2026 à 16 h 45 (Paris).** Prix 7 520,6. Les 5 niveaux valides étaient tous des accélérateurs : 7 500 (−9,0 Md$, 8,2 % du GEX de la zone), 7 400, 7 300, 7 450 et 7 250. Le GEX total était de −75 Md$ : régime négatif.

---

## 3. Règle 2 : le flux de primes
**La prime**, c'est le prix d'une option, payé par l'acheteur au vendeur. Un contrat SPX porte sur **100 fois l'indice** (spécifications Cboe). Prime échangée = volume × prix × 100.

**Ce que font les outils payants.** Ils regardent chaque transaction en direct et la classent : achetée au prix vendeur (*ask*) = « haussière » pour un call, vendue au prix acheteur (*bid*) = l'inverse. Ça demande le flux de toutes les transactions en temps réel, qui est **payant**.

**Ce que dit la recherche.** Pan et Poteshman (2006) ont utilisé des données Cboe **non publiques** qui disent qui **achète pour ouvrir** une position. Les actions dont ce ratio puts/calls est bas ont battu celles où il est haut de plus de **0,40 % le lendemain** et de plus de **1 % sur la semaine**. Mais ils concluent que l'effet vient surtout d'**informations privées** des acheteurs d'options, et que la partie observable publiquement en contient beaucoup moins. Leçon : le *sens* de l'initiative (qui achète) est ce qui contient l'information, et c'est justement ce que les données gratuites ne donnent pas.

**Ce qu'on a codé (carte « Flux de primes depuis l'ouverture »).**
- Prime échangée = volume du jour × prix milieu (bid + ask) / 2 × 100, pour chaque option de la chaîne Cboe gratuite (différée d'environ 15 min).
- On compare les primes des **calls hors de la monnaie** (strike au-dessus du prix) à celles des **puts hors de la monnaie** (strike en dessous). Plus de 1,2 fois plus de calls → « penchant calls » ; l'inverse → « penchant puts » ; sinon « équilibré ».
- Une courbe par photo du collecteur (toutes les 15 min).
- **Limite majeure** : on ne sait pas qui a acheté. Une grosse prime de puts peut venir d'un fonds qui **achète** une protection, ou d'un autre qui **vend** des puts pour encaisser la prime. Ce n'est **pas** le flux haussier/baissier de la vidéo.

**Exemple réel, SPX le 13/11 à 16 h 45.** Puts hors de la monnaie 774 M$ contre calls 378 M$ : penchant puts (ratio 0,49), 56 % des primes en 0DTE.

---

## 4. Règle 3 : la confirmation
**L'idée.** Ne pas acheter « parce que le prix touche un niveau », mais attendre qu'il **reparte** du niveau. On rate une partie du mouvement, mais on évite d'entrer quand le niveau ne tient pas.

**Ce que dit la recherche.**
- Baltussen, Da, Lammers et Martens (2021, *Journal of Financial Economics*) : sur plus de 60 futures (actions, obligations, matières premières, devises) de 1974 à 2020, le rendement de la journée prédit celui de la **dernière demi-heure**. Ils relient cet « élan de fin de journée » à la couverture des teneurs de marché quand ils sont **courts en gamma** (ils doivent acheter quand ça monte, vendre quand ça baisse).
- Barbon et Buraschi (2021, *Gamma Fragility*, document de travail) : quand les dealers sont courts en gamma et que le marché est peu liquide, le prix a tendance à **continuer** dans la journée ; quand ils sont longs en gamma, il a tendance à **revenir**.
- Ensemble : un **frein** pourrait plutôt faire rebondir le prix, un **accélérateur** plutôt le laisser passer. La confirmation sert à voir lequel des deux se produit **aujourd'hui**.

**Ce qu'on ne peut pas faire gratuitement.** La vidéo confirme sur le future NQ en direct. Nous n'avons pas de prix gratuit et en direct du future : on confirmera sur les photos de l'indice (toutes les 15 min, différées de 15 min). C'est plus lent et moins précis, et ce retard sera compté dans le test.

---

## 5. Gratuit ou payant : le tableau honnête
| Élément de la vidéo | Chez nous (0 €/mois) | Ce qui manque |
|---|---|---|
| GEX net par strike | ✅ Oui, chaîne Cboe différée | Position réelle des dealers inconnue (convention) |
| Niveaux à fort open interest | ✅ Oui, carte « Niveaux valides » | Open interest de la veille seulement |
| Flux de primes haussier / baissier | ⚠️ Approximation : primes échangées calls vs puts | Qui a acheté ou vendu (flux en temps réel, payant) |
| Classement des tickers par primes | ❌ Non | Il faudrait les chaînes de toutes les actions en direct |
| Confirmation sur NQ en direct | ⚠️ Sur l'indice, photos toutes les 15 min | Prix gratuit et en direct du future |

---

## 6. La règle pré-enregistrée et le test
La règle complète est écrite **avant tout test** dans `09 - Idées de stratégies/Gamma - niveaux, flux et confirmation.md` : niveau valide touché, flux pas contraire, confirmation 15 min plus tard, stop de l'autre côté du niveau, objectif 2 R, sortie avant la clôture. **1 variante**, critères de `CRITERES.md` v1 (au moins 100 trades, coûts 0,30 % aller-retour). Le collecteur a assez de photos vers **mi-décembre 2026** ; avant ça, aucun verdict.

**Mon avis à ce stade.** Les trois règles sont du bon sens de gestion du risque, et la recherche confirme que la couverture des dealers déplace bien les prix à certains moments. Mais « bon sens + effet réel dans la recherche » ne veut pas dire « méthode rentable après frais ». La seule réponse qui compte viendra du backtest.

---

## 🧠 Quiz (mes réponses)
1. Quelles sont les trois règles de la vidéo ?
2. Pourquoi un strike avec un gros gamma mais peu d'open interest est-il un niveau « faible » ?
3. Que mesure l'étude de Ni, Pearson et Poteshman, et sur quels jours ?
4. Que veut dire « penchant puts » dans notre dashboard, et pourquoi n'est-ce pas forcément baissier ?
5. Pourquoi les données de Pan et Poteshman contenaient-elles plus d'information que notre flux gratuit ?
6. Selon Baltussen et ses co-auteurs, que se passe-t-il quand les dealers sont courts en gamma ?
7. Pourquoi notre confirmation est-elle plus lente que celle de la vidéo ?
8. La vidéo prouve-t-elle que la méthode gagne de l'argent ? Que faudrait-il ?

## 📚 Sources
- **Vidéo TikTok** (captures envoyées par Lauris le 16/11/2026) : règles et écrans décrits en partie 1. Aucun chiffre de performance.
- **Investopedia**, définition de *Option Premium* (montrée dans la vidéo) : prix d'un contrat d'option, revenu du vendeur.
- **OCC**, *Characteristics and Risks of Standardized Options* (document officiel remis avant de trader des options) : [page de l'OCC](https://www.theocc.com/Company-Information/Documents-and-Archives/Options-Disclosure-Document).
- **Cboe**, *SPX Options Product Specification* (multiplicateur 100 $, options européennes réglées en cash) : [cboe.com](https://www.cboe.com/tradable_products/sp_500/spx_options/specifications).
- **CME Group**, *E-mini Nasdaq-100 contract specs* : [cmegroup.com](https://cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html).
- **SqueezeMetrics**, *Gamma Exposure (GEX): Quantifying hedge rebalancing in SPX options* (2016, révisé 2017) : origine de la formule GEX et de la convention « dealers longs des calls, courts des puts » ; GEX positif = volatilité freinée, négatif = amplifiée (affirmation de l'auteur, pas une étude publiée dans une revue). [PDF](https://slopeofhope.com/wp-content/uploads/2020/11/GEX-white_paper.pdf).
- Ni, S. X., Pearson, N. D., Poteshman, A. M. (2005), *Stock price clustering on option expiration dates*, **Journal of Financial Economics** 78(1), 49-87. [Fiche RePEc](https://ideas.repec.org/a/eee/jfinec/v78y2005i1p49-87.html) · [résumé](https://scholars.hkbu.edu.hk/en/publications/stock-price-clustering-on-option-expiration-dates-3/).
- Pan, J., Poteshman, A. M. (2006), *The Information in Option Volume for Future Stock Prices*, **Review of Financial Studies** 19(3), 871-908. [Document de travail NBER w10925](https://www.nber.org/papers/w10925).
- Baltussen, G., Da, Z., Lammers, S., Martens, M. (2021), *Hedging demand and market intraday momentum*, **Journal of Financial Economics** 142(1), 377-403. [Université Erasmus](https://pure.eur.nl/en/publications/hedging-demand-and-market-intraday-momentum/).
- Barbon, A., Buraschi, A. (2021), *Gamma Fragility*, document de travail (SSRN). [Page de l'auteur](https://abarbon.com/papers/gamma-fragility).
- Nos chiffres : photos du collecteur `Outil/archives_gamma/2026-11-13/SPX_1046.csv.gz` et `NDX_1046.csv.gz`, calculs `gamma.niveaux_valides` et `gamma.flux_primes`.

## 🎧 Écouter
Épisodes 9 et 10 du podcast *Cerveau trading* : [écouter sur le téléphone](https://lauris-ad.github.io/cerveau-trading/index.html#e09).

## 📒 Mots à ajouter au [[Glossaire]]
Niveau valide · Prime d'option · Flux de primes · Hors de la monnaie · Confirmation · Courts en gamma · Pinning
