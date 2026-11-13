---
type: lecon
date: 2026-10-29
semaine: 1
theme: Sécurité
maitrise: 
---
# 📖 Sécurité des wallets et address poisoning

## 🧩 L'idée en une phrase
Sur la blockchain, une erreur est **définitive** : pas de banque pour annuler un virement. La sécurité, c'est donc d'abord des **réflexes**, avant toute technique.

## 📚 1. Custodial ou non-custodial : qui garde la clé ?
| | Custodial (Binance, Coinbase…) | Non-custodial (MetaMask, Phantom…) |
|---|---|---|
| Qui a la clé privée ? | La plateforme | **Moi seul** |
| Si j'oublie mon mot de passe | Le support peut m'aider | Seule ma **seed phrase** peut me sauver |
| Risque principal | Faillite ou piratage de la plateforme (ex. FTX en 2022) | Je perds ou je me fais voler ma seed phrase |
| Pour qui ? | Débutant, petits montants | Utilisateur qui maîtrise la sécurité |

**Analogie :** custodial, c'est un **coffre à la banque** (la banque a une clé). Non-custodial, c'est un **coffre chez moi** : personne ne peut me le bloquer, mais si je perds la clé, personne ne peut l'ouvrir.

> Pendant le programme, je n'ai **besoin d'aucun wallet** : je regarde ceux des autres sur Etherscan. Regarder ne coûte rien et ne risque rien.

## 🎣 2. L'address poisoning (empoisonnement d'adresse)
C'est ce que j'ai vu sur vitalik.eth : des **envois minuscules** (0,0001 ETH ou 0 token) venant d'inconnus.

**Comment l'arnaque fonctionne :**
1. Je fais un vrai envoi à mon ami : `0x52a1…8F3c`.
2. Un bot repère la transaction et crée une **fausse adresse** qui commence et finit pareil : `0x52a1…8F3c` (le milieu est différent).
3. Le bot m'envoie 0 ou 0,0001 ETH depuis cette fausse adresse : elle apparaît maintenant **dans mon historique**.
4. La fois suivante, je copie l'adresse « de mon ami » depuis mon historique… et je copie la **fausse**. Mon argent part chez l'arnaqueur. Définitivement.

**Pourquoi ça marche :** les wallets et Etherscan **abrègent** les adresses (`0x52a1…8F3c`). On ne vérifie que le début et la fin.

**Comment l'éviter :**
- [ ] Je ne copie **jamais** une adresse depuis mon historique de transactions
- [ ] Je garde mes adresses de confiance dans un **carnet d'adresses** (ou une note Obsidian)
- [ ] Je vérifie l'adresse **en entier**, pas seulement le début et la fin
- [ ] Pour un gros montant, j'envoie d'abord un **petit test**

## 🗑️ 3. Les autres « cadeaux » empoisonnés
| Ce que je vois | Ce que c'est | Que faire |
|---|---|---|
| Un token inconnu dans mon wallet | Spam, souvent avec un **site** dans son nom (« Claim at xyz.com ») | **Ne pas y toucher**, ne pas visiter le site |
| Un NFT « gratuit » | Même chose : appât vers un site piégé | Ignorer |
| Un site qui demande de « connecter » mon wallet pour réclamer | Il veut me faire **signer une autorisation** qui vide mon wallet | Fermer la page |

> **Règle d'or :** ce qui arrive sans que je l'aie demandé est un **piège** jusqu'à preuve du contraire.

## 🔐 4. Mes 7 règles de sécurité (version complète)
1. Je ne donne **jamais** ma seed phrase, à personne, même au « support ».
2. Ma seed phrase est sur **papier**, jamais en photo, jamais dans le cloud, **jamais dans Obsidian**.
3. Je ne connecte **jamais** mon wallet à un site inconnu.
4. Je ne signe **jamais** une transaction que je ne comprends pas.
5. Je ne copie **jamais** une adresse depuis l'historique.
6. Je n'interagis **jamais** avec un token ou NFT reçu sans l'avoir demandé.
7. Je me méfie de **tout** message privé qui propose aide ou gain.

## 🛠️ Exercice (20 min) : chasseur de spam sur vitalik.eth
1. Sur Etherscan, ouvre vitalik.eth, onglet **Token Transfers (ERC-20)**.
2. Trouve **3 transferts suspects** : token inconnu, nom bizarre ou contenant un site web, montant étrange.
3. Pour chacun, note dans [[Exemple - vitalik.eth]] (section « Tokens suspects ») : le **nom du token**, l'**expéditeur** en abrégé, et **pourquoi** il te semble suspect.
4. Bonus : dans l'onglet **Transactions**, cherche deux adresses **From** qui commencent et finissent pareil. Si tu en trouves, c'est de l'address poisoning en direct.

⚠️ **Ne clique sur aucun site** qui apparaît dans le nom d'un token.

## 🧠 Quiz (mes réponses)
1. Quelle est la différence entre custodial et non-custodial, en une phrase ?
2. Pourquoi Vitalik reçoit-il des envois de 0,0001 ETH d'inconnus ?
3. Comment l'address poisoning peut-il me faire envoyer mon argent à un arnaqueur ?
4. Où dois-je garder ma seed phrase ? Où ne dois-je jamais la garder ?
5. Un token « FREE-ETH-CLAIM.COM » apparaît dans mon wallet. Que fais-je ?

## 🔗 Liens
[[05 - Wallets et clés]] · [[Glossaire]] · [[Exemple - vitalik.eth]]
