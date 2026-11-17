---
type: guide
tags: [agent]
---

# Rituels de l'Équipe

Le but : que chaque agent enrichisse un projet **régulièrement**, sans que tu aies à le demander. Il n'y a pas de deuxième boucle : la boucle du chef d'orchestre (Head of Markets) existe déjà, et c'est elle qui fait passer les agents à tour de rôle.

L'organigramme te montre si ça marche : un agent qui pulse a travaillé récemment, et un agent marqué 💤 « en sommeil » n'a rien fait depuis 7 jours (ni dans les 10 derniers cycles). Le bouton **💤 En sommeil** te donne la liste.

## À chaque cycle de la boucle trading

| Étape | Agent | Ce qu'il fait |
|---|---|---|
| 1 | [[chief-of-staff]] | Lit les nouvelles idées (tour de contrôle et IDEES.md) et les envoie à la bonne direction. |
| 2 | [[markets-prompt-smith]] | Écrit la consigne du cycle (Contexte, Objectif mesurable, Étapes, Critère chiffré, Vérification, Sortie). |
| 3 | Le poste de l'axe | A → [[markets-data-dashboard]] · B → [[markets-pedagogue]] · C → [[markets-backtest]] (et [[markets-geopolitique]] pour le contrôle contexte). |
| 4 | [[avocat-du-diable]] | Seulement pour une **nouvelle idée** de stratégie ou une source qui promet des gains : 3 failles, puis GO, GO avec conditions ou NO-GO. |
| 5 | [[markets-gardien-backtest]] | Seulement quand une idée **change de marche** (backtest → hors échantillon → paper trade → candidate). |
| 6 | [[hocs]] | Toujours, avant d'écrire « À dire » : ouvre le vrai livrable et rend GO ou NO-GO. Un NO-GO = le cycle n'est pas annoncé comme fini. |
| 7 | [[knowledge-keeper]] | Toujours : ce qui a été appris va dans le coffre (leçon, fiche d'idée, lien), sans doublon. |

Dans JOURNAL.md, chaque cycle garde son titre `## Cycle N · A · titre` et ajoute deux lignes :

```
- **Date** : 2026-11-17
- **Agents** : markets-backtest, avocat-du-diable (GO avec conditions), hocs (GO), knowledge-keeper
```

Le premier agent de la liste est celui qui a fait le travail. Le Laurisverse lit ces lignes et met l'organigramme à jour tout seul.

## Pour que personne ne dorme

- Le chef d'orchestre alterne déjà les axes A, B et C. En plus, au début de chaque cycle, s'il reste un agent Marchés ou board en sommeil, il choisit de préférence une tâche du BACKLOG qui le fait travailler.
- [[markets-bot-dev]] travaille quand le moteur de paper trading a besoin d'un correctif, ou quand une idée atteint le paper trade.
- [[cto-infra]] et [[cto-outils]] : une vérification par semaine (les tâches planifiées tournent-elles ? journaux d'erreurs dans Outil\logs), notée dans [[Passages]].
- Tous les 5 cycles, le point d'étape cite les agents en sommeil et dit pourquoi.

## Les autres projets

- **Croq** (branché le 17/11) : un cycle Croq tourne tout seul **lundi, mercredi et vendredi vers 8 h** : [[croq-ceo]] choisit la tâche, un poste ([[croq-produit]], [[croq-dev]], [[croq-growth]]) la fait, [[hocs]] vérifie, et une pull request attend Lauris. Rien n'est mis en ligne sans sa fusion.
- **Études** : leurs fiches sont des brouillons. Leurs fiches passent en « actif » quand Lauris donne les dates de contrôles et les intitulés des cours.

## Noter un passage hors de la boucle

Une ligne de plus dans le tableau de [[Passages]] : `| 2026-11-17 | hocs | Mise à jour du dashboard | GO | Capture vérifiée |`.
