---
type: lecon
date: 2026-11-17
semaine: Veille du 17/11
theme: Orderflow
maitrise: 
---
# 📖 Delta, absorption et footprint

## 🧩 L'idée en une phrase
Derrière chaque bougie, il y a des **agressifs** (ils acceptent le prix, ordre au marché) et des **passifs** (ils attendent, ordre limite). Le **delta** compte qui a frappé le plus fort ; l'**absorption**, c'est quand les agressifs frappent fort **et que le prix ne bouge pas** : quelqu'un d'invisible encaisse.

> Durée : 45 min. Prérequis : leçon 04 (carnet d'ordres). Source de la veille : Dualis Flow (TikTok, 17/11).

---

## 1. Agressif ou passif
- **Agressif (*taker*)** : envoie un ordre au marché, prend ce qui est dans le carnet. Paie le spread.
- **Passif (*maker*)** : laisse un ordre limite dans le carnet, attend d'être servi.
Chaque transaction a un acheteur et un vendeur ; ce qui compte, c'est **lequel des deux était agressif**.

## 2. Le delta
**Delta = volume acheté agressivement − volume vendu agressivement.**
- Delta très négatif : les vendeurs ont frappé.
- Delta positif : les acheteurs reprennent la main.
La recherche confirme que ce déséquilibre pousse le prix à court terme : Cont, Kukanov et Stoikov (2014) trouvent que le **déséquilibre des ordres** au sommet du carnet explique l'essentiel des variations de prix sur de courtes périodes, avec une relation à peu près linéaire.

## 3. L'absorption
Si le déséquilibre pousse normalement le prix, alors **un gros delta négatif sans baisse** est anormal : des acheteurs passifs (ordres limites, parfois cachés ou renouvelés) **absorbent** les ventes. Exemple de la vidéo : sur un plus bas de séance, les vendeurs agressifs frappent, le prix ne descend plus, puis le delta repasse positif.

## 4. Le footprint
Le **footprint** découpe chaque bougie **par niveau de prix** et affiche, à chaque niveau, les achats et les ventes agressifs. Il montre **où** dans la bougie l'absorption a eu lieu.

## 5. Ce que ça coûte (et ce qu'on fait à 0 €)
| Marché | Delta par bougie | Footprint par niveau | Prix |
|---|---|---|---|
| **Crypto (Binance)** | oui : « taker buy volume » dans les fichiers publics | oui : transactions agrégées avec le côté agressif | **gratuit** |
| **NQ (CME)** | non | non | **payant** (flux CME ; Databento offre 125 $ de crédit mais demande une carte) |

Donc nos tests d'absorption (H1, H3) se font **sur BTC**, avec le delta par bougie de 5 minutes.

---

## 🧠 Quiz (mes réponses)
1. Quelle différence entre un ordre agressif et un ordre passif ?
2. Comment calcule-t-on le delta d'une bougie ?
3. Qu'est-ce que l'absorption, et pourquoi est-ce un signal « anormal » ?
4. Pourquoi testons-nous l'absorption sur BTC et pas sur le NQ ?

## 📚 Sources
- Cont, R., Kukanov, A., Stoikov, S. (2014), *The Price Impact of Order Book Events*, **Journal of Financial Econometrics** 12(1), 47-88 : [arXiv 1011.6402](https://arxiv.org/abs/1011.6402).
- **Binance**, documentation des données publiques (colonnes « taker buy volume » et « was the buyer the maker ») : [github.com/binance/binance-public-data](https://github.com/binance/binance-public-data/).
- **Databento**, crédits offerts aux nouveaux comptes : [databento.com](https://databento.com/docs/knowledge-base/new-users/usage-based-pricing-and-data-credits).
- Veille TikTok du 17/11 (Dualis Flow, « absorption ») : `Veille TikTok - 17-11-2026.md`.

## 🎧 Écouter
Épisode 15 du podcast *Cerveau trading* : [écouter sur le téléphone](https://lauris-ad.github.io/cerveau-trading/index.html#e15).

## 📒 Mots à ajouter au [[Glossaire]]
Taker · Maker · Delta · Absorption · Footprint · Orderflow
