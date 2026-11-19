---
type: lecon
date: 2026-11-19
semaine: Discord Dualis Flow
theme: Order flow
maitrise: 
---
# 📖 Auction market theory : balances, value area, POC, single prints

## 🧩 L'idée en une phrase
Le marché est une **enchère** : le prix monte ou descend pour **chercher** des acheteurs et des vendeurs, puis il **tourne en rond** là où les deux sont d'accord. Ces zones d'accord, appelées **balances**, servent de repères, pas de promesses.

> Durée : 20 min. Prérequis : [[14 - La VWAP]] et [[15 - Delta, absorption et footprint]]. Contexte : synthèse du Discord Dualis Flow (17/11), section 2.7.

---

## 1. D'où vient l'idée
J. Peter Steidlmayer, trader au **Chicago Board of Trade**, a créé le **Market Profile** dans les années 1980. Le CBOT l'a diffusé, et le livre *Markets and Market Logic* (Steidlmayer et Koy, 1986) l'a popularisé. James Dalton l'a ensuite expliqué dans *Mind Over Markets* (1990). On appelle aujourd'hui ce cadre **auction market theory** (AMT).

L'idée de base : le prix fait deux choses, **chercher** (il avance vite vers une nouvelle zone) ou **équilibrer** (il oscille dans une zone où l'échange se fait).

## 2. Les mots à connaître
| Mot | Ce que c'est |
|---|---|
| **Balance** | Zone où le prix a tourné en range assez longtemps : acheteurs et vendeurs y sont d'accord. |
| **Déséquilibre** | Sortie de la balance : un camp prend le dessus, le prix cherche plus loin. |
| **TPO** | *Time price opportunity* : une lettre par tranche de 30 min à chaque prix touché. Plus il y a de lettres à un prix, plus le marché y a passé de temps. |
| **POC** | *Point of control* : le prix où le plus d'échanges (ou de temps) s'est fait. |
| **Value area** | Zone autour du POC qui contient environ **70 %** de l'activité. Bornes : **VAH** (haut) et **VAL** (bas). |
| **Single prints** | Prix traversés **une seule fois**, sur une seule tranche de 30 min : le prix y est passé vite. |
| **LVN / HVN** | Nœud de faible ou fort volume dans un volume profile. |

Le chiffre de 70 % est une **convention** reprise d'un écart-type d'une loi normale (environ 68 %). Ce n'est pas une loi du marché.

## 3. Ce que dit Dualis Flow
- Une balance ne devient **pas invalide** quand le prix la retraverse, mais elle réagit **un peu moins à chaque retour**. *« Le premier retour est toujours le meilleur. »*
- Le prix réagit d'abord à **ce qui est juste à côté** de lui.
- Quand une balance casse, on **laisse le prix choisir sa direction**, puis on cherche la zone suivante.
- Le footprint sert à **entrer** sur une de ces zones, pas à les trouver.

Ce sont des **affirmations de traders**, pas des résultats mesurés. Pour nous, « le premier retour est le meilleur » est l'hypothèse **H5**, pré-enregistrée le 17/11, pas encore testée.

## 4. Pourquoi ça peut marcher, et pourquoi c'est fragile
- **Pour** : beaucoup de gens regardent la value area de la veille et le POC. Des ordres s'y posent, donc le prix y hésite parfois. C'est le même raisonnement que pour les chiffres ronds : Osler (2003) a montré que les ordres stop et take-profit se regroupent près des chiffres ronds sur le marché des changes ([[18 - La liquidité, version ICT et version recherche]]).
- **Contre** : il y a toujours une balance, un POC ou un VAH quelque part près du prix. Après coup, on trouvera toujours un niveau qui « a marché ». Seul un test sur **tous** les retours, écrits **avant**, dit si la réaction est plus forte que le hasard.

## 5. Exemple fictif, pour lire un profil
*Chiffres inventés pour la lecture.* Hier, le BTC a passé la journée entre 64 000 $ et 65 200 $. POC à 64 600 $, VAH à 64 900 $, VAL à 64 300 $. Le matin, il a monté très vite de 64 900 $ à 65 200 $ (single prints).

Ce matin, le prix ouvre à 65 100 $.
- Il est **au-dessus** de la value area : les acheteurs ont la main pour l'instant.
- Les single prints entre 64 900 $ et 65 200 $ sont une zone que le prix « n'a pas vraiment échangée » : beaucoup de traders s'attendent à ce qu'il y revienne.
- Un retour au VAH (64 900 $) serait le **premier retour** sur la balance d'hier.

Rien de tout ça n'est un signal. C'est une **carte** pour savoir où regarder, puis attendre le flux ([[15 - Delta, absorption et footprint]]).

## 6. Ce qu'on en fait chez nous
1. Repères : POC, VAH, VAL de la veille, et les single prints.
2. Hypothèse H5 : mesurer si le **premier retour** sur une balance réagit mieux que les suivants, sur BTC, ETH et SOL en 1 h.
3. Tant que H5 n'a pas passé le backtest et le hors échantillon, ces niveaux restent **des endroits où regarder**, pas des endroits où acheter.

---

## 🧠 Quiz (mes réponses)
1. Que fait le prix dans une balance, et que fait-il dans un déséquilibre ?
2. Qu'est-ce que le POC ?
3. Que contient la value area, et pourquoi le chiffre de 70 % n'est-il qu'une convention ?
4. Que sont des single prints, et pourquoi beaucoup de traders s'attendent-ils à ce que le prix y revienne ?
5. Selon Dualis Flow, quel retour sur une balance réagit le mieux ?
6. Pourquoi trouve-t-on toujours, après coup, un niveau qui « a marché » ?

## 📚 Sources
- J. Peter Steidlmayer et Kevin Koy, *Markets and Market Logic*, Porcupine Press, 1986.
- James F. Dalton, Eric T. Jones et Robert B. Dalton, *Mind Over Markets*, Probus, 1990.
- Carol Osler, « Currency orders and exchange rate dynamics: an explanation for the predictive success of technical analysis », *Journal of Finance*, 2003.
- Synthèse Dualis Flow : `Stratégies Discord - Dualis Flow.md`, section 2.7 ; hypothèse H5 dans `09 - Idées de stratégies`.

## 🎧 Écouter
Épisode 35 du podcast *Cerveau trading* : débloqué quand la leçon 34 sera validée.

## 📒 Mots à ajouter au [[Glossaire]]
Balance · Déséquilibre · TPO · POC · Value area (VAH, VAL) · Single prints · LVN, HVN
