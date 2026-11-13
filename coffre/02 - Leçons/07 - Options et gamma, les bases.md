---
type: lecon
date: 2026-11-13
semaine: Terminal ES/NQ
theme: Options et gamma
maitrise: 
---
# 📖 Options et gamma : les notions fondamentales

## 🧩 L'idée en une phrase
Des banques (les **teneurs de marché**) vendent et achètent des millions d'**options** sur la Bourse américaine. Pour ne pas parier, elles se **couvrent** en achetant ou vendant l'indice. Le **gamma** mesure à quel point cette couverture va les obliger à acheter ou vendre quand le prix bouge. L'onglet *Gamma SPX / NDX* essaie d'estimer où ces achats et ventes forcés pourraient se produire.

> Cette leçon est longue. Découpe-la en 3 séances d'une heure : parties 1 à 3, puis 4 à 6, puis 7 à 9 avec l'exercice.

---

## 📚 1. Indice, ETF, future : qui est qui ?
**Un indice**, c'est une **moyenne** : un seul nombre qui résume le prix d'un panier d'actions. On ne peut pas l'acheter directement, comme on ne peut pas acheter « la température moyenne de la France ».

| Nom | Ce que c'est | Ordre de grandeur |
|---|---|---|
| **SPX** | L'indice **S&P 500** : les 500 plus grosses entreprises américaines | Quelques milliers de points |
| **NDX** | L'indice **Nasdaq-100** : 100 grosses entreprises, surtout tech (Apple, Nvidia, Microsoft…) | Environ 3 à 4 fois le SPX |
| **SPY** | Un **ETF** : une action qu'on peut acheter et qui copie le S&P 500 | ≈ SPX ÷ 10 |
| **QQQ** | Un ETF qui copie le Nasdaq-100 | ≈ NDX ÷ 40 |
| **ES** | Le **future** (contrat à terme) sur le S&P 500, à la bourse CME de Chicago | 1 point = **50 $** (version mini : MES, 1 point = 5 $) |
| **NQ** | Le future sur le Nasdaq-100 | 1 point = **20 $** (version mini : MNQ, 1 point = 2 $) |

**Un future**, c'est un contrat qui dit : « on se met d'accord aujourd'hui sur un prix pour une date future ». En pratique, presque personne n'attend la date : on l'achète et on le revend pour profiter du mouvement, comme une action.

**Pourquoi les traders aiment ES et NQ :**
- Ils s'échangent **presque 24 h sur 24**, 5 jours sur 7 (l'indice SPX, lui, ne bouge que pendant la séance de New York, **15 h 30 → 22 h** heure de Paris).
- Ils ont un **effet de levier** : on bouge beaucoup d'argent avec une petite mise. C'est puissant… et très dangereux. 10 points d'ES contre toi, c'est 500 $ de perte sur 1 seul contrat.

**ES n'est pas exactement SPX.** Il y a un petit écart de quelques points (la **base**), qui fond jusqu'à l'échéance du future (mars, juin, septembre, décembre). C'est pour ça que l'outil affiche les niveaux en points **SPX** et que la conversion en points ES viendra plus tard.

**Analogie :** le SPX est le **thermomètre**. Le SPY est une **photo du thermomètre** qu'on peut acheter. L'ES est un **pari sur ce que dira le thermomètre**, avec un levier.

---

## 📚 2. Une option, c'est quoi ?
Une option est un **droit, pas une obligation**, d'acheter ou de vendre quelque chose à un prix fixé, jusqu'à une date fixée. Ce droit se paie.

| Mot | Sens | Analogie |
|---|---|---|
| **Call** | Le droit d'**acheter** à un prix fixé. On l'achète si on pense que ça va **monter**. | Verser des **arrhes** pour réserver un appartement au prix d'aujourd'hui |
| **Put** | Le droit de **vendre** à un prix fixé. On l'achète si on pense que ça va **baisser**, ou pour **s'assurer**. | Une **assurance auto** : on paie, et si l'accident arrive, l'assurance rembourse |
| **Strike** (prix d'exercice) | Le prix fixé dans le contrat | Le prix de l'appartement écrit sur la réservation |
| **Échéance** | La date où le droit expire | La date limite de la réservation |
| **Prime** | Le prix payé pour acheter l'option | Le montant des arrhes, ou la cotisation d'assurance |
| **Multiplicateur** | Une option SPX porte sur **100 fois** l'indice | Une prime de 20 points coûte donc 20 × 100 = **2 000 $** |

### Exemple chiffré d'un call (chiffres inventés)
Le SPX est à **6 000**. J'achète un **call strike 6 050**, échéance vendredi, pour une prime de **20 points** (= 2 000 $).

| SPX vendredi à la clôture | Ce que vaut mon call | Mon résultat |
|---|---|---|
| 5 950 | 0 (je n'ai aucun intérêt à « acheter » à 6 050) | **− 2 000 $** (je perds la prime, pas plus) |
| 6 050 | 0 | − 2 000 $ |
| 6 070 | 20 points | 0 $ (je récupère juste la prime) |
| 6 100 | 50 points = 5 000 $ | **+ 3 000 $** |

**Ce qu'il faut retenir :**
- L'**acheteur** d'option risque au maximum sa prime. Il gagne gros seulement si le mouvement est grand **et** rapide.
- Le **vendeur** d'option encaisse la prime, mais son risque peut être énorme. C'est lui qui joue le rôle de l'assureur.
- La plupart des options achetées **finissent à zéro**. Comme la plupart des assurances ne servent jamais.

### Dans, à, hors de la monnaie
- **À la monnaie** (ATM) : le strike est tout près du prix actuel.
- **Dans la monnaie** (ITM) : l'option vaudrait déjà quelque chose si elle expirait maintenant (un call 5 900 quand le SPX est à 6 000).
- **Hors de la monnaie** (OTM) : elle ne vaudrait rien maintenant (un call 6 100 quand le SPX est à 6 000).

---

## 📚 3. Open interest et 0DTE
**L'open interest** (OI), c'est le **nombre de contrats encore ouverts** sur un strike et une échéance. Le **volume**, c'est le nombre de contrats échangés **aujourd'hui**.

**Analogie :** pour un concert, le volume, c'est le nombre de billets vendus aujourd'hui au guichet. L'open interest, c'est le nombre de billets **encore valides** dans la poche des gens. Un billet revendu entre deux fans compte dans le volume, mais ne change pas l'OI.

⚠️ **Point clé pour l'outil :** l'open interest est publié **une seule fois par jour**, le matin, pour la veille. Toute la journée, notre calcul utilise donc des positions **d'hier**.

**0DTE** veut dire *zero days to expiration* : des options qui **expirent aujourd'hui**. Le SPX a des échéances **tous les jours** de la semaine, et les 0DTE représentent aujourd'hui une très grosse part du volume des options SPX (souvent autour de la moitié, voire plus).

Le problème : un 0DTE acheté à 16 h et revendu à 19 h n'apparaît **jamais** dans l'open interest. Une partie importante de l'activité du jour est donc **invisible** pour nous. C'est pour ça que l'onglet a un filtre **0DTE seul / Sans 0DTE** : pour voir quelle part du gamma vient de ces options très courtes.

---

## 📚 4. Delta : la vitesse
**Le delta** répond à la question : *si l'indice monte de 1 point, de combien bouge le prix de mon option ?*

| Option | Delta | Lecture |
|---|---|---|
| Call très hors de la monnaie | ≈ 0,05 | L'indice monte de 1 point, l'option gagne 0,05 point. Elle réagit à peine. |
| Call à la monnaie | ≈ 0,50 | Elle bouge moitié moins vite que l'indice |
| Call très dans la monnaie | ≈ 0,95 | Elle bouge presque comme l'indice |
| Put | entre 0 et **− 1** | Négatif : le put **gagne** quand l'indice **baisse** |

**Bonus :** le delta d'un call donne aussi une idée grossière de la **probabilité** qu'il finisse dans la monnaie. Delta 0,20 ≈ 20 % de chances.

**Analogie :** le delta, c'est la **vitesse** de l'option par rapport à l'indice.

---

## 📚 5. Gamma : l'accélération
Le delta **ne reste pas fixe**. Si l'indice monte, mon call à 0,50 devient un call à 0,60, puis 0,70… **Le gamma mesure de combien le delta change quand l'indice bouge de 1 point.**

**Analogie :** si le delta est la **vitesse**, le gamma est la **pédale d'accélérateur**. Un gros gamma, c'est une voiture nerveuse : la vitesse change brutalement au moindre mouvement.

**Où le gamma est-il le plus fort ?**
1. **Près du prix actuel** (options à la monnaie). Une option très loin du prix a un gamma presque nul.
2. **Près de l'échéance.** Une option qui expire dans 2 heures et dont le strike est juste à côté du prix passe très vite de « vaut zéro » à « vaut beaucoup ». C'est pour ça que les **0DTE ont un gamma énorme**.

---

## 📚 6. Les dealers et la couverture : pourquoi le prix pourrait réagir
**Les teneurs de marché** (*market makers*, ou *dealers*) sont de grosses sociétés qui sont toujours prêtes à acheter ou vendre des options. Leur métier n'est pas de parier sur la direction : il est de gagner un peu sur l'écart entre prix d'achat et prix de vente (le **spread**, vu en [[04 - Le carnet d'ordres]]).

**Analogie :** un **bureau de change** à l'aéroport. Il ne veut pas parier sur le dollar. Il veut juste gagner sa commission. S'il a trop de dollars, il s'en débarrasse.

Pour ne pas parier, le dealer **neutralise son delta** : il achète ou vend des futures ES (ou du SPY) pour que ses gains et pertes s'annulent. C'est la **couverture en delta** (*delta hedging*). Et comme le delta change avec le prix (c'est le gamma), il doit **ajuster en permanence**.

### Cas A : le dealer est « long gamma » (il a **acheté** des options)
1. Il a acheté un call à delta 0,50. Pour être neutre, il **vend** 0,50 unité d'indice.
2. L'indice **monte**. Le delta passe à 0,60. Il doit **vendre encore** 0,10.
3. L'indice **baisse**. Le delta retombe à 0,40. Il **rachète** 0,10.

Il **vend quand ça monte** et **achète quand ça baisse** : il freine le marché. **Analogie : un thermostat** qui coupe le chauffage quand il fait trop chaud.

### Cas B : le dealer est « short gamma » (il a **vendu** des options)
Tout s'inverse : il doit **acheter quand ça monte** et **vendre quand ça baisse**. Il pousse dans le sens du mouvement. **Analogie : une boule de neige** qui grossit en dévalant la pente.

### La grande convention (et sa faiblesse)
Personne ne publie la vraie position des dealers. L'outil, comme la plupart des sites de gamma, fait une **hypothèse** :
- Le public **achète des puts** pour s'assurer → les dealers les ont **vendus** → **gamma négatif** sur les puts.
- Le public **vend des calls** (pour toucher la prime sur ses actions) → les dealers les ont **achetés** → **gamma positif** sur les calls.

C'est souvent à peu près vrai, mais **pas toujours**. Un jour où le public achète massivement des calls (euphorie), la convention se trompe de signe.

---

## 📚 7. L'onglet *Gamma SPX / NDX*, élément par élément

### La formule de base
Pour chaque option : **GEX = gamma × open interest × 100 × prix² × 1 %**, positif pour les calls, négatif pour les puts.

En français : **combien de dollars d'indice les dealers devraient acheter ou vendre si l'indice bougeait de 1 %.** L'outil l'affiche en milliards de dollars.

| Ce que tu vois | Ce que ça veut dire | Comment le lire |
|---|---|---|
| **SPX (pour ES) / NDX (pour NQ)** | L'indice dont on regarde les options | NDX plutôt que QQQ : c'est l'indice qui colle au NQ |
| **Toutes échéances / 0DTE seul / Sans 0DTE** | Filtre sur les options prises en compte | Compare les deux : si presque tout le gamma vient des 0DTE, les niveaux peuvent changer vite dans la journée |
| **Prix de l'indice** | Le prix du SPX ou du NDX, **différé d'environ 15 min** | Ce n'est pas un prix pour trader |
| **GEX par strike** (barres vertes et rouges) | La force des calls (vert) et des puts (rouge) à chaque strike, à ± 4 % du prix | Les grandes barres sont les endroits où la couverture des dealers pèse le plus |
| **Call wall** | Le strike où les **calls** pèsent le plus, à ± 5 % | Souvent vu comme un **plafond** possible : en montant vers lui, les dealers vendent de plus en plus |
| **Put wall** | Le strike où les **puts** pèsent le plus, à ± 5 % | Souvent vu comme un **plancher** possible. Mais s'il casse, la baisse peut **accélérer** (on passe dans la zone short gamma) |
| **Profil gamma selon le prix** | Le GEX total **recalculé** comme si l'indice était à un autre prix | Une seule courbe qui montre où le marché serait « calme » et où il serait « nerveux » |
| **Zéro gamma** | Le prix où cette courbe **passe par zéro** | La **frontière** entre les deux régimes. Au-dessus : plutôt calme. En dessous : plutôt nerveux |
| **Régime positif / négatif** | Le signe du GEX total au prix actuel | Positif : les dealers **freinent** (thermostat). Négatif : ils **amplifient** (boule de neige) |
| **Niveaux clés : pics et creux** | Les strikes au GEX net le plus positif (pics) et le plus négatif (creux) | Des zones à surveiller, pas des ordres à placer |
| **Hypothèses** | Les 5 limites du calcul | À relire à chaque fois (partie 8) |

### Exemple de lecture (chiffres inventés)
> SPX à **6 000**. Zéro gamma à **5 950**. Call wall **6 100**. Put wall **5 900**. Régime **positif**.

Lecture : *« Le prix est au-dessus du zéro gamma, donc en théorie les dealers freinent les mouvements. On s'attendrait plutôt à une journée qui oscille entre 5 900 et 6 100. Si le prix passe sous 5 950, on change de régime, et les mouvements pourraient devenir plus amples. »*

Remarque le vocabulaire : **« en théorie »**, **« plutôt »**, **« pourraient »**. C'est voulu.

---

## ⚠️ 8. Les limites : ce que l'outil ne dit **pas**
1. **La position des dealers est supposée**, pas connue (partie 6).
2. **L'open interest date d'hier.** Les 0DTE ouverts et fermés dans la journée sont invisibles.
3. **Les données sont différées d'environ 15 min** (source gratuite Cboe).
4. **La volatilité implicite est figée** quand on simule d'autres prix pour le profil : en vrai, elle change quand le marché bouge.
5. **SPX n'est pas ES** : il faudra convertir avec l'écart (la base), qui varie.

Et surtout : **aucun de ces niveaux n'est une règle de trading.** Il existe beaucoup de discours sur Internet (et sur TikTok) qui présentent le gamma comme une boule de cristal. On ne le croira **que si notre propre backtest** le montre, avec environ **un mois d'archives** du collecteur. D'ici là : on **observe**, on **note**, on ne trade pas. Règle d'or : **objectif n°1 ne pas perdre**.

---

## 🛠️ Exercice (15 min par jour, 5 jours de bourse)
**But :** apprendre à lire l'onglet et commencer à se faire son propre avis, avant le backtest.

1. Avant **15 h 30**, lance `Lancer-collecteur-gamma.bat` puis `Lancer-dashboard.bat`.
2. Vers **16 h**, ouvre l'onglet *Gamma SPX / NDX*, sur **SPX**, **Toutes échéances**. Note dans ta note du jour (dossier 04 - Journal) :
   - le prix, le zéro gamma, le call wall, le put wall, le régime ;
   - en cliquant sur **0DTE seul** : le GEX 0DTE est-il grand ou petit par rapport au total ?
   - ta **prévision en une phrase** (« journée plutôt calme entre X et Y » ou « journée nerveuse »).
3. Le soir (ou le lendemain matin), note le **plus haut** et le **plus bas** du SPX de la journée (sur TradingView par exemple, symbole `SPX`).
4. Réponds à : **ma prévision était-elle juste ? Le prix a-t-il touché un wall ? Que s'est-il passé là ?**

Au bout de 5 jours, on regarde ensemble tes notes. Ce n'est pas un backtest (5 jours, c'est beaucoup trop peu), c'est un **entraînement de l'œil**.

### Mini-exercice de calcul (sur papier)
Le SPX est à 6 000. Tu achètes un **put strike 5 950** pour **15 points**.
- a) Combien coûte ce put en dollars ?
- b) Que vaut-il, et quel est ton résultat, si le SPX finit à 5 900 ? À 5 940 ? À 6 050 ?
- c) À quel prix du SPX ne gagnes-tu ni ne perds-tu rien ?

---

## 🧠 Quiz (mes réponses)
1. Quelle est la différence entre le SPX, le SPY et l'ES ?
2. Combien gagnes-tu ou perds-tu si l'ES bouge de 8 points sur 1 contrat ? Et sur 1 contrat MES ?
3. Explique avec tes mots la différence entre un call et un put, avec une analogie.
4. Pourquoi l'open interest affiché le matin ne voit-il pas les 0DTE du jour ?
5. Si le delta est la vitesse, qu'est-ce que le gamma ? Où est-il le plus fort ?
6. Pourquoi un dealer long gamma vend-il quand le marché monte ?
7. Que veut dire « régime négatif », et pourquoi le marché pourrait-il y être plus nerveux ?
8. Cite 3 limites de l'onglet gamma.
9. Le SPX passe sous le zéro gamma. Est-ce un signal de vente ? Pourquoi ?

## 📒 Mots à ajouter au [[Glossaire]]
Indice · ETF · Future · Base · Option · Call · Put · Strike · Échéance · Prime · Multiplicateur · ATM / ITM / OTM · Open interest · 0DTE · Delta · Gamma · Teneur de marché (dealer) · Couverture en delta · GEX · Call wall · Put wall · Zéro gamma · Régime gamma

## 🔗 Liens
[[04 - Le carnet d'ordres]] · [[03 - Amplitude et taille de position]] · [[Audit terminal ES-NQ]] · [[Glossaire]]
