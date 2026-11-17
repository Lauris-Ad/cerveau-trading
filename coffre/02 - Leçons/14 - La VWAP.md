---
type: lecon
date: 2026-11-17
semaine: Veille du 17/11
theme: Prix moyen pondéré par les volumes
maitrise: 
---
# 📖 La VWAP : le prix moyen payé par le marché

## 🧩 L'idée en une phrase
La **VWAP** (*volume-weighted average price*) est le **prix moyen payé** par tous les acheteurs depuis un point de départ, chaque transaction pesant selon son volume. Prix au-dessus : ceux qui ont acheté depuis ce point sont **en moyenne en profit** ; en dessous, ce sont les vendeurs.

> Durée : 40 min. Prérequis : leçon 01 (bougies). Source de la veille : Dualis Flow (TikTok, 17/11).

---

## 1. Le calcul
**VWAP = Σ (prix × volume) ÷ Σ volume**, en cumulant depuis un **point d'ancrage**.
- Définition des professionnels (Madhavan, 2002) : la valeur en dollars des transactions divisée par le volume échangé sur la période.
- Sur un graphique en bougies, les logiciels prennent souvent le **prix typique** de chaque bougie, (haut + bas + clôture) ÷ 3, comme « prix ». C'est ce que fait notre dashboard.

Exemple : 100 BTC échangés à 60 000 $ puis 300 BTC à 61 000 $ → VWAP = (100 × 60 000 + 300 × 61 000) ÷ 400 = **60 750 $** (plus près de 61 000 parce que plus de volume s'y est échangé).

## 2. D'où ça vient
Les gérants de fonds jugent leurs courtiers sur la VWAP depuis la fin des années 1980 : Berkowitz, Logue et Noser (1988, *Journal of Finance*) la présentent comme une bonne approximation du prix obtenu par un acheteur « passif ». Madhavan (2002) note qu'elle **reste un repère très utilisé** pour mesurer les coûts de transaction. C'est pour ça que beaucoup de monde la regarde : des ordres d'institutions s'organisent autour d'elle.

## 3. L'ancrage change tout
| VWAP | Point de départ | Pour qui |
|---|---|---|
| **Daily** | minuit (pour la crypto : 00 h UTC, soit 01 h à Paris en hiver) | vision de la journée entière |
| **Séance de New York** | 9 h 30 à New York = **15 h 30 à Paris** | traders actions et Nasdaq |
| **Ancrée** sur un événement | une annonce, un plus bas… | analyse d'un mouvement précis |

Deux ancrages = deux niveaux différents, parce que ce ne sont pas les mêmes transactions qui sont moyennées.

## 4. Ce qu'on peut et ne peut pas en dire
- La vidéo affirme qu'un niveau VWAP « peut tenir 3 fois » parce que beaucoup de gens regardent la même ligne. C'est **une observation, pas une preuve** : notre hypothèse **H1** va le mesurer.
- La VWAP **ne prédit rien seule** : elle dit qui est en profit, pas où le prix va.

## 5. Dans nos outils
Dashboard, graphique des bougies : **ligne bleue = VWAP du jour**, **pointillés = VWAP de la séance de New York**. Calcul sur bougies de 1 h, donc approché.

---

## 🧠 Quiz (mes réponses)
1. Prix sous la VWAP de la séance : qui est en profit ?
2. Pourquoi une VWAP ancrée à 15 h 30 et une autre ancrée à minuit ne donnent-elles pas le même niveau ?
3. Donne la formule de la VWAP.
4. Pourquoi les institutions regardent-elles la VWAP ?

## 📚 Sources
- Madhavan, A. (2002), *VWAP Strategies*, **Transaction Performance** (Institutional Investor Journals), printemps 2002 : [PDF](https://www.smallake.kr/wp-content/uploads/2014/07/TP_Spring_2002_Madhavan.pdf).
- Berkowitz, S., Logue, D., Noser, E. (1988), *The Total Cost of Transactions on the NYSE*, **Journal of Finance**, p. 97-112 (cité par Madhavan).
- Veille TikTok du 17/11 (Dualis Flow, « VWAP ») : `Veille TikTok - 17-11-2026.md`.

## 🎧 Écouter
Épisode 14 du podcast *Cerveau trading* : [écouter sur le téléphone](https://lauris-ad.github.io/cerveau-trading/index.html#e14).

## 📒 Mots à ajouter au [[Glossaire]]
VWAP · Prix typique · Ancrage · Benchmark
