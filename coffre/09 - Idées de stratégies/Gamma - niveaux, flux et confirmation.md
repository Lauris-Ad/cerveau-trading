---
type: idee
date: 2026-11-16
source: Vidéo TikTok (captures envoyées par Lauris le 16/11/2026) « Not every level is valid / GEX alone ≠ edge / Confirmation is a must »
source_type: tiktok
famille: gamma
marche: SPX et NDX (indices), photos du collecteur toutes les 15 min pendant la séance US
statut: idée (attend les données)
variantes_declarees: 1
resultat: 
verdict: 
---
# 💡 Gamma : niveaux valides, flux de primes et confirmation

> Règles écrites le 16/11/2026 **avant** tout test. Critères : `CRITERES.md` v1, inchangés. Leçon associée : [[10 - Gamma, niveaux, flux et confirmation]].
> C'est une idée **distincte** de « Niveaux gamma SPX/NDX » (réaction au zéro gamma, call wall, put wall), qui garde son propre compteur de variantes.

## 🔗 Source
- Vidéo TikTok, 3 règles : garder les niveaux à plus fort open interest ; ne pas trader contre le flux de primes ; attendre une confirmation du prix. Aucun résultat chiffré dans la vidéo.

## 📏 Les règles, écrites précisément
**Données** : photos `Outil/archives_gamma/<jour>/<SYM>_HHMM.csv.gz` (spot, chaîne d'options, volume, bid, ask). Prix = spot de chaque photo (différé ~15 min).
1. **Niveaux du jour** : à la **première photo** de la séance, `gamma.niveaux_valides(zone=5 %, n=5, quantile_oi=80 %)` sur toutes les échéances. Les niveaux restent fixes toute la journée (l'open interest ne change qu'une fois par jour).
2. **Contact** : une photo où le spot est à **±0,10 %** d'un niveau valide.
3. **Confirmation** : à la photo **suivante** (15 min après), le spot s'est éloigné du niveau d'**au moins 0,10 %**. Au-dessus → sens **achat** ; en dessous → sens **vente**. Sinon, pas de trade.
4. **Filtre flux** (à la photo de confirmation, `gamma.flux_primes`) : pas d'achat si le penchant est « puts », pas de vente si le penchant est « calls ».
5. **Entrée** : au spot de la photo **d'après la confirmation** (15 min de plus, pour compter le retard des données gratuites).
6. **Stop** : de l'autre côté du niveau, à **0,15 %** du niveau. **Objectif** : **2 R**. **Sortie forcée** : dernière photo de la séance (pas de position la nuit).
7. Un seul trade à la fois par indice ; SPX et NDX jugés ensemble. Un niveau ne sert qu'une fois par jour.
8. 1 % de risque par trade, coûts **0,30 % aller-retour** (`CRITERES.md` v1, sans exception pour les futures).

## 🧪 Test
- 1 variante déclarée → t exigé **2,0**. Il faut **≥ 100 trades** : on lance le backtest quand les archives contiennent au moins 21 séances, puis on le relance une seule fois à 100 trades si besoin. Pas avant.
- Découpage 70 / 30 chronologique comme les autres idées.
- Backtest 70 % : (à remplir)

## ⚠️ Ce qui peut fausser le test
- Spot différé de 15 min, photos espacées de 15 min : on mesure une version **lente** de la méthode.
- Le flux est une **approximation** (primes échangées, sans savoir qui achète).
- Les coûts de 0,30 % sont lourds pour des mouvements intrajournaliers d'indice : une règle qui gagne un peu peut échouer pour cette raison. On ne change pas les critères pour autant.

## 🧾 Verdict
-
