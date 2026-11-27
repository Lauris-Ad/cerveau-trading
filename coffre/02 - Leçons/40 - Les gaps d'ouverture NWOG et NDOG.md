---
type: lecon
date: 2026-11-27
semaine: Stratégies
theme: Gaps d'ouverture (ICT)
maitrise: 
---
# 📖 Les gaps d'ouverture : NWOG et NDOG

## 🧩 L'idée en une phrase
Les futures américains (ES, NQ) s'arrêtent une heure chaque soir et tout le week-end : le prix de la reprise n'est presque jamais celui de l'arrêt, et l'écart entre les deux s'appelle un **gap d'ouverture**. La méthode ICT dit que ces gaps attirent le prix ; nous, on le mesure.

## 1. Pourquoi il y a un trou
- Les futures CME sur indices cotent presque 24 h sur 24, **sauf** une pause chaque jour de semaine de **17h00 à 18h00, heure de New York** (23h00 à 0h00 à Paris la plupart de l'année), et du **vendredi 17h00 au dimanche 18h00**.
- Pendant la pause, le monde continue : nouvelles, Asie, ordres qui s'accumulent. À 18h00, le premier prix tient compte de tout ça. Le saut entre la dernière cotation et la première, c'est le gap.
- Le bitcoin cote 24 h sur 24 chez Binance : il n'a pas ces gaps. Les futures bitcoin du CME, eux, en ont (le fameux « gap du CME »).

## 2. Les deux gaps
| Nom | De | À | Combien en garder |
|---|---|---|---|
| **NDOG** (New Day Opening Gap) | dernière cotation avant 17h00 | première cotation à 18h00 | celui du jour et quelques récents |
| **NWOG** (New Week Opening Gap) | clôture du vendredi 17h00 | ouverture du dimanche 18h00 | les 5 derniers, par convention |

Chaque gap se lit avec **trois prix** : son haut, son bas, et son milieu, appelé **CE** (*consequent encroachment*, « l'empiètement conséquent » : juste le 50 %).

Attention, les sources ne sont pas toutes d'accord sur la seconde exacte de la clôture (16h59, 17h00, parfois 16h30). Nous prenons la dernière cotation avant 17h00.

## 3. Ce que la méthode affirme
- Le gap est une **zone vide** : personne n'a pu y échanger. Le prix aurait tendance à **revenir le combler**, au moins en partie.
- Le **CE** servirait de point de réaction : le prix y rebondit ou le traverse franchement.
- Les NWOG des semaines passées serviraient de **supports et résistances** pendant plusieurs semaines.
- Des chiffres circulent (par exemple « 60 à 75 % de NDOG comblés »), mais **aucune source ne montre de calcul**. Une page de référence le dit elle-même : aucune statistique publique vérifiée.

## 4. Comment on le teste, honnêtement
Règles écrites le 27/11 **avant** de voir les données (`09 - Idées de stratégies/NWOG NDOG - pré-enregistrement 27-11.md`) :
- **Le piège à éviter** : un gap petit est souvent « comblé » juste parce que le prix bouge. Il faut donc un **témoin** : le même écart, mais placé de l'autre côté de l'ouverture. Si le prix touche le gap aussi souvent que le témoin, le gap n'attire rien.
- On mesure : combien de NDOG et de NWOG sont comblés, combien de fois le CE est touché, et ce qui se passe au premier contact, contre le témoin.
- Une seule stratégie testée : à 18h00, partir vers le comblement, objectif la clôture de 17h00, stop d'une taille de gap.
- Les frais : 0,30 % pour le verdict (nos critères), 0,02 % à titre d'information, car un future coûte bien moins cher que le bitcoin au comptant. Les gaps de l'ES et du NQ font souvent moins de 0,3 % : la question des frais du cycle 44 revient.

## 5. Ce que nos mesures ont montré
*En cours (NQ et ES, environ deux ans en 1 h). Cette partie sera remplie avec les chiffres réels.*

## 6. Le tester à la main sur TradingView
1. Ouvre **NQ1!** ou **ES1!** en 5 min ou 15 min, **avec les heures étendues** activées (sinon les gaps n'apparaissent pas comme tels).
2. Ajoute un indicateur public « NWOG/NDOG » (il en existe plusieurs en code ouvert), ou trace-les à la main : une ligne au prix de 17h00, une à 18h00, une au milieu.
3. Chaque soir pendant deux semaines, note dans ton journal : taille du gap, sens, comblé ou non avant 17h00 le lendemain, CE touché ou non, et ce que le prix a fait au premier contact.
4. Compare tes notes à nos mesures. Tu n'en tires aucun trade : tu vérifies si ce que tu vois ressemble à ce que disent les chiffres.

## 🧠 Quiz (mes réponses)
1. Pourquoi le NQ a-t-il un gap chaque soir, et pas le bitcoin chez Binance ?
2. Entre quels deux prix se mesure un NWOG ?
3. Qu'est-ce que le CE d'un gap ?
4. Pourquoi faut-il un témoin de l'autre côté pour savoir si un gap « attire » le prix ?
5. Un NDOG fait 0,08 % sur le NQ. Que pèsent nos frais de 0,30 % face à lui ?

## 📚 Sources
- Définitions NDOG, NWOG, CE et « cinq NWOG gardés » : [LuxAlgo, New Day Opening Gap](https://www.luxalgo.com/library/concept/new-day-opening-gap.md) (aucune statistique publique vérifiée, selon la page elle-même).
- Heures 16h59 / 18h00 et chiffres de comblement non sourcés : [Aron Groups, ICT NWOG](https://arongroups.co/technical-analyze/ict-nwog-new-week-opening-gap/) ; indicateurs publics : [TradingView, scripts NDOG](https://www.tradingview.com/scripts/ndog/).
- Pause quotidienne des futures CME de 17h à 18h (heure de New York) : rappelée par les mêmes sources ; nos données Yahoo NQ=F et ES=F la montrent (voir le README de `Outil/donnees/gaps_ouverture/`).

## 📒 Mots à ajouter au [[Glossaire]]
Gap d'ouverture · NDOG · NWOG · CE (consequent encroachment) · Heures étendues · Témoin

## 🔗 Liens
[[37 - L'opening range américain]] · [[38 - Battre le hasard]] · [[09 - Les coûts, le vrai adversaire]] · [[Glossaire]]
