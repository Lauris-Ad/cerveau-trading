---
type: guide
---
# 🧭 Mode d'emploi du coffre

## 1. Installation (15 minutes, une seule fois)
1. Télécharge **Obsidian** sur obsidian.md et installe-le.
2. Décompresse le fichier `Trading-Vault.zip` dans un dossier facile à retrouver (par exemple `Documents`).
3. Ouvre Obsidian → **« Open folder as vault »** (Ouvrir un dossier comme coffre) → choisis le dossier `Trading-Vault`.
4. Si Obsidian demande s'il faut faire confiance à l'auteur du coffre, accepte : c'est toi qui l'as importé.
5. Mets Obsidian en français si tu veux : ⚙️ Paramètres → **About / À propos** → Language.
6. Installe **Dataview** :
   - ⚙️ Paramètres → **Plugins communautaires** → « Activer les plugins communautaires »
   - **Parcourir** → cherche `Dataview` → **Installer** → **Activer**
   - Dans les options de Dataview, active **« Enable JavaScript Queries »**
7. Ouvre le [[Dashboard]] : il doit afficher des tableaux, pas des blocs de code.

## 2. Organisation des dossiers
| Dossier | Contenu |
|---|---|
| `00 - Accueil` | Dashboard et ce mode d'emploi |
| `01 - Programme` | Le programme global et une note par semaine, avec des cases à cocher |
| `02 - Leçons` | Une note par leçon (modèle **Leçon**) |
| `03 - Glossaire` | Tous les mots appris |
| `04 - Journal` | Une note par jour d'étude |
| `05 - Wallets` | Une fiche par wallet analysé |
| `06 - Tokens` | Une fiche par token analysé |
| `07 - Trades papier` | Une fiche par trade fictif |
| `08 - Code` | Notes sur mes scripts Python (le code lui-même viendra en semaine 3) |
| `09 - Idées de stratégies` | Les idées vues ailleurs (vidéos, articles), triées avant tout test (modèle **Idée de stratégie**) |
| `Templates` | Les modèles de notes |

## 3. Créer une note à partir d'un modèle
1. Crée une nouvelle note dans le bon dossier (clic droit sur le dossier → Nouvelle note) et donne-lui un nom.
2. `Ctrl + P` → tape **« modèle »** (ou « template ») → choisis **Insérer un modèle**.
3. Choisis le modèle : **Wallet**, **Token**, **Trade papier**, **Leçon** ou **Idée de stratégie**.
4. Remplis les champs en haut (entre les `---`) : c'est ce que lit le Dashboard.

**Note du jour :** clique sur l'icône calendrier dans la barre de gauche (ou `Ctrl + P` → « note quotidienne »). Elle se crée automatiquement dans `04 - Journal` avec le bon modèle.

## 4. Les champs du haut (propriétés)
Le bloc entre `---` en haut d'une note s'appelle le **frontmatter** (ou propriétés). Le Dashboard s'en sert pour faire ses tableaux et ses calculs. Règles simples :
- Les nombres sans unité : `duree: 60`, pas `duree: 60 min`.
- Les dates au format `2026-10-19`.
- Pour vrai/faux : `true` ou `false` (ou `oui` / `non` pour `regles_respectees`).

En semaine 4, ce sont tes **scripts Python** qui rempliront certains de ces champs automatiquement.

## 5. Ma routine
1. Ouvrir le Dashboard → voir la semaine en cours.
2. Créer la note du jour.
3. Demander à Claude la leçon du jour, la coller dans une note **Leçon**, la résumer avec mes mots.
4. Faire la pratique, cocher les tâches dans la note de la semaine.
5. Remplir `duree`, `theme` et `humeur` dans le journal.

## 6. Sécurité
- Ce coffre ne doit **jamais** contenir de seed phrase, de clé privée ou de mot de passe.
- Les clés API iront dans un fichier `.env` **en dehors** du coffre (on verra ça en semaine 4).
- Si tu synchronises ce coffre (OneDrive, Google Drive…), c'est encore plus important.
