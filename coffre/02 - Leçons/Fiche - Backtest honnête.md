---
type: fiche
date: 2026-11-13
theme: Backtest
maitrise: 
---
# 🧪 Fiche modèle : le backtest honnête

## 🧩 L'idée en une phrase
Un backtest rejoue une stratégie sur le passé. Il est **honnête** s'il compte tous les coûts, ne regarde jamais le futur, garde des données jamais vues pour le juge final, et avoue combien d'essais ont été faits.

## 1. Les coûts : le premier tueur
- Chaque trade paie des **frais** (0,10 % par côté chez Binance au comptant, taux de base) et du **slippage** (l'écart entre le prix voulu et le prix obtenu). Notre règle : 0,30 % par aller-retour.
- **Exemple réel (13/11/2026)** : nos 3 premiers tests sur BTC 1 h avaient un résultat **brut proche de zéro** (−0,02 % à −0,06 % par trade). Une fois les 0,30 % retirés : **−0,32 % à −0,36 % par trade**. Sans coûts, on aurait cru à « presque rentable ».
- Analogie : un vendeur qui gagne 0 € de marge par article et paie 30 centimes de livraison à chaque vente. Plus il vend, plus il perd.

## 2. Ne jamais regarder le futur
- Un signal n'est connu qu'à la **clôture** de la bougie. On entre donc à l'**ouverture suivante**, jamais au prix de la bougie du signal.
- Si le stop et l'objectif sont touchés dans la même bougie, on ne sait pas lequel est venu en premier : on compte **le stop** (hypothèse prudente).
- Les moyennes et médianes se calculent avec **les bougies passées seulement**.

## 3. Le hors échantillon : le juge qu'on ne soudoie pas
- On coupe l'historique : **70 % les plus anciens** pour chercher, **30 % les plus récents** pour juger. Les 30 % ne sont **jamais regardés** avant le test final, et ne servent **qu'une fois**.
- Analogie : réviser avec les annales, puis passer l'examen avec un sujet jamais vu. Si on a vu le sujet, la note ne veut plus rien dire.

## 4. Le piège des essais multiples (sur-ajustement)
- Essayer 20 réglages et garder le meilleur, c'est presque sûr de trouver un « gagnant » par **pure chance**.
- Bailey, Borwein, López de Prado et Zhu montrent qu'avec assez d'essais on peut obtenir un très bon backtest qui ne vaut rien hors échantillon (*Pseudo-Mathematics and Financial Charlatanism*, Notices of the AMS, 2014).
- Harvey, Liu et Zhu recommandent d'exiger une **statistique t supérieure à 3**, et non 2, quand beaucoup de chercheurs ont fouillé les mêmes données (*… and the Cross-Section of Expected Returns*, Review of Financial Studies 29(1), 2016).
- Bailey et López de Prado proposent de « dégonfler » le ratio de Sharpe selon le nombre d'essais (*The Deflated Sharpe Ratio*, Journal of Portfolio Management, 2014).
- **Chez nous** : chaque réglage = 1 variante, comptée pour toujours. Plus il y en a, plus le seuil t monte (2,0 → 3,3). Voir `CRITERES.md`.

## 5. Lire un rapport de backtest
| Chiffre | Question qu'il répond | Notre seuil (70 %) |
|---|---|---|
| Nombre de trades | Est-ce assez pour ne pas être de la chance ? | ≥ 100 |
| Espérance par trade (net) | Combien je gagne en moyenne, coûts payés ? | > +0,05 % |
| Statistique t | Le gain moyen est-il grand par rapport au bruit ? | selon les variantes |
| Profit factor | Gains totaux ÷ pertes totales | ≥ 1,20 |
| Drawdown max | Pire chute depuis un sommet | ≤ 20 % |
| Taux de réussite | % de trades gagnants. **Seul, il ne veut rien dire** | aucun |

> Le fair value gap promettait « comblé 71 % du temps ». Sur BTC 1 h, il l'a été **41 %** du temps sous 20 bougies, et l'espérance nette était de −0,36 %. Un pourcentage de réussite n'est pas un gain.

## 6. Ce qui ne s'invente pas
Un backtest qui passe ne promet rien : il reste le hors échantillon, puis le paper trade. Une idée qui échoue est **archivée**, jamais retouchée jusqu'à ce qu'elle passe.

## 🧠 Quiz (mes réponses)
1. Pourquoi entre-t-on à l'ouverture de la bougie suivante, et pas à la clôture du signal ?
2. Un test donne +0,20 % brut par trade. Avec nos coûts, que vaut-il net ?
3. Stop et objectif touchés dans la même bougie : que compte-t-on, et pourquoi ?
4. À quoi servent les 30 % hors échantillon, et combien de fois a-t-on le droit de les utiliser ?
5. J'ai testé 12 réglages d'une idée. Quel t minimal exige notre règle ?
6. Une stratégie gagne 80 % de ses trades. Est-elle forcément rentable ? Donne un exemple.
7. Que dit Harvey, Liu et Zhu (2016) sur le seuil de t ?
8. Une idée échoue au hors échantillon. Que fait-on ?

## 📚 Sources
- Harvey, Liu, Zhu (2016), *… and the Cross-Section of Expected Returns*, RFS 29(1) : [NBER w20592](https://nber.org/papers/w20592) (lu : « t-ratio greater than 3.0 »).
- Bailey, López de Prado (2014), *The Deflated Sharpe Ratio* : [SSRN 2460551](https://papers.ssrn.com/abstract=2460551).
- Bailey, Borwein, López de Prado, Zhu (2014), *Pseudo-Mathematics and Financial Charlatanism*, Notices of the AMS : [PDF](https://carmamaths.org/jon/backtest.pdf).
- Frais Binance (source secondaire, page officielle non lue) : [BitDegree](https://www.bitdegree.org/crypto/tutorials/binance-fees).
- Nos résultats : `Outil/rapports_backtest/` et `JOURNAL.md`, cycles 8 et 10.

## 📒 Mots à ajouter au [[Glossaire]]
Backtest · Hors échantillon · Slippage · Espérance · Statistique t · Profit factor · Drawdown · Sur-ajustement · Variante
