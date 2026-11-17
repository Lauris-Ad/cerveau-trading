---
type: lecon
date: 2026-11-17
semaine: Veille du 17/11
theme: Gamma et régimes
maitrise: 
---
# 📖 Régimes de gamma : le flip, la Call Wall et la Put Wall

## 🧩 L'idée en une phrase
Au-dessus du **gamma flip** (zéro gamma, appelé **HVL** dans certains outils), les teneurs de marché sont en général **longs gamma** et leurs couvertures **amortissent** les mouvements ; en dessous, ils sont **courts gamma** et leurs couvertures **amplifient** les mouvements. Les **walls** sont les strikes où se concentre le plus de gamma.

> Durée : 40 min. Prérequis : leçons 07 et 10 (options, gamma, niveaux). Source de la veille : Dualis Flow, @nam.journal_ (TikTok, 17/11).

---

## 1. Rappel en une ligne
Le **GEX** (*gamma exposure*) estime, strike par strike, combien les teneurs de marché devront acheter ou vendre l'actif pour rester couverts quand le prix bouge (leçon 07).

## 2. Les trois niveaux
| Niveau | Définition (SpotGamma) | Lecture habituelle |
|---|---|---|
| **Zéro gamma / gamma flip** (≈ HVL) | le prix où le gamma total des teneurs de marché **passe par zéro** | au-dessus : mouvements amortis, plutôt du range ; en dessous : mouvements amplifiés, plutôt de la volatilité |
| **Call Wall** | le strike avec la plus forte concentration de calls au-dessus | souvent une résistance, borne haute du range attendu |
| **Put Wall** | le strike avec la plus forte concentration de puts en dessous | souvent un support, borne basse |
Attention : chaque fournisseur calcule un peu différemment (la vidéo le dit aussi). SpotGamma distingue par exemple son *Volatility Trigger* du zéro gamma. Notre dashboard calcule le **zéro gamma** et les walls à partir de la chaîne Cboe gratuite (différée de 15 min).

## 3. Ce que dit la recherche
Ni, Pearson, Poteshman et White (2021, *Review of Financial Studies*) montrent un canal **sans information** par lequel le **rééquilibrage des couvertures** des teneurs de marché d'options modifie la **volatilité** des actions et la probabilité de grands mouvements. C'est la base sérieuse de l'idée « régime de gamma ».

## 4. Ce qu'on va mesurer
- **H2** : la séance du Nasdaq-100 est-elle plus calme quand elle ouvre au-dessus du flip ? (≥ 20 séances de chaque côté, au mieux mi-janvier 2027).
- **H4** : le prix réagit-il plus souvent sur les walls que sur un niveau témoin à la même distance ? (≥ 30 contacts).
Tant que ces tests ne sont pas faits, le badge « régime gamma » du dashboard est **une hypothèse affichée**, pas un signal.

---

## 🧠 Quiz (mes réponses)
1. Que se passe-t-il en général pour la volatilité quand le prix passe sous le gamma flip ?
2. Définis la Call Wall et la Put Wall.
3. Pourquoi deux outils peuvent-ils afficher des niveaux gamma différents ?
4. Que teste H2 ?

## 📚 Sources
- **SpotGamma**, *Options key levels explained* (zéro gamma, Call Wall, Put Wall, Volatility Trigger) : [spotgamma.com](https://spotgamma.com/options-key-levels-explained/).
- Ni, S. X., Pearson, N. D., Poteshman, A. M., White, J. (2021), *Does Option Trading Have a Pervasive Impact on Underlying Stock Prices?*, **Review of Financial Studies** 34(4), 1952-1986 : [fiche RePEc](https://ideas.repec.org/a/oup/rfinst/v34y2021i4p1952-1986..html).
- Fiches `H2 - Range du NDX selon le gamma flip.md` et `H4 - Réaction sur les walls gamma.md`.

## 🎧 Écouter
Épisode 17 du podcast *Cerveau trading* : [écouter sur le téléphone](https://lauris-ad.github.io/cerveau-trading/index.html#e17).

## 📒 Mots à ajouter au [[Glossaire]]
Gamma flip · Zéro gamma · HVL · Call Wall · Put Wall · Régime de gamma
