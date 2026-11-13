---
id: e03
numero: 3
titre: "Wallets, clés et address poisoning"
description: "Leçons 05 et 06 : ce que contient vraiment un wallet, custodial ou non, et l'arnaque de l'empoisonnement d'adresse."
date: 2026-11-13
sources:
  - "02 - Leçons/05 - Wallets et clés.md"
  - "02 - Leçons/06 - Sécurité et address poisoning.md"
---

## Accroche

Bienvenue dans le cerveau trading. Épisode 3 : les wallets, les clés, et la sécurité.

Sur la blockchain, une erreur est définitive. Il n'y a pas de banque pour annuler un virement. Alors la sécurité, c'est d'abord des réflexes, avant toute technique. Dans cet épisode, tu vas comprendre ce que contient vraiment un wallet, et comment fonctionne une arnaque que tu as déjà vue de tes propres yeux sur le wallet de Vitalik : l'address poisoning.

Cet épisode reprend la leçon 5, « Wallets et clés », et la leçon 6, « Sécurité et address poisoning ».

## Idée 1

Première idée clé : un wallet ne contient pas tes cryptos. Elles sont sur la blockchain. Le wallet contient les clés qui prouvent qu'elles t'appartiennent.

Ta leçon utilise l'image d'une boîte aux lettres vitrée. L'adresse, qui commence par zéro x, c'est le numéro de la boîte : elle est publique, tu peux la partager. La clé privée, c'est la clé de la boîte : elle est secrète, et celui qui l'a contrôle les fonds. La seed phrase, ces 12 ou 24 mots, c'est le double de toutes les clés : elle est ultra secrète. Et la vitre, c'est le fait que tout le monde voit l'intérieur : les soldes et les transactions sont publics.

C'est pour ça que la blockchain est pseudonyme, pas anonyme. Et c'est justement ce qui rend l'analyse de wallets possible. Pour regarder, on utilise des explorateurs : Etherscan pour Ethereum, Solscan pour Solana, BscScan pour la BNB Chain.

## Idée 2

Deuxième idée clé : custodial ou non-custodial, qui garde la clé ?

Custodial, c'est par exemple un compte Binance ou Coinbase : la plateforme a la clé privée. Si tu oublies ton mot de passe, le support peut t'aider. Le risque principal, c'est la faillite ou le piratage de la plateforme, comme FTX en 2022. C'est adapté à un débutant, pour de petits montants.

Non-custodial, c'est MetaMask ou Phantom : toi seul as la clé. Si tu oublies ton mot de passe, seule ta seed phrase peut te sauver. Le risque principal, c'est de perdre ta seed phrase ou de te la faire voler.

L'analogie de ta leçon : custodial, c'est un coffre à la banque, la banque a une clé. Non-custodial, c'est un coffre chez toi : personne ne peut te le bloquer, mais si tu perds la clé, personne ne peut l'ouvrir. D'où la phrase connue : « Not your keys, not your coins. »

Et un point rassurant : pendant le programme, tu n'as besoin d'aucun wallet. Tu regardes ceux des autres sur Etherscan. Regarder ne coûte rien et ne risque rien.

## Idée 3

Troisième idée clé : l'address poisoning, l'empoisonnement d'adresse. Voici comment l'arnaque fonctionne, en quatre temps.

Un : tu fais un vrai envoi à un ami.

Deux : un bot repère la transaction et crée une fausse adresse qui commence et finit exactement pareil que celle de ton ami. Seul le milieu est différent.

Trois : le bot t'envoie zéro, ou 0 virgule 0001 ether, depuis cette fausse adresse. Elle apparaît maintenant dans ton historique.

Quatre : la fois suivante, tu copies l'adresse « de ton ami » depuis ton historique, et tu copies la fausse. Ton argent part chez l'arnaqueur. Définitivement.

Pourquoi ça marche ? Parce que les wallets et Etherscan abrègent les adresses. On ne vérifie que le début et la fin.

Il existe d'autres cadeaux empoisonnés. Un token inconnu dans ton wallet, souvent avec un site dans son nom : n'y touche pas, ne visite pas le site. Un NFT gratuit : même chose, c'est un appât, ignore-le. Et un site qui te demande de connecter ton wallet pour réclamer quelque chose : il veut te faire signer une autorisation qui vide ton wallet. Ferme la page.

La règle d'or de ta leçon : ce qui arrive sans que tu l'aies demandé est un piège jusqu'à preuve du contraire.

## Exemple concret

L'exemple concret, c'est celui que tu as vu toi-même sur vitalik point eth : des envois minuscules, 0 virgule 0001 ether ou zéro token, venant d'inconnus. Ce sont des tentatives d'address poisoning.

Ta leçon te propose un exercice de 20 minutes : sur Etherscan, ouvre vitalik point eth, onglet Token Transfers. Trouve trois transferts suspects : un token inconnu, un nom bizarre ou qui contient un site web, ou un montant étrange. Et en bonus, dans l'onglet Transactions, cherche deux adresses d'expéditeur qui commencent et finissent pareil. Si tu en trouves, c'est de l'address poisoning en direct. Et surtout : ne clique sur aucun site qui apparaît dans le nom d'un token.

## Récap

On récapitule avec tes sept règles de sécurité.

Un : je ne donne jamais ma seed phrase, à personne, même au « support ».

Deux : ma seed phrase est sur papier. Jamais en photo, jamais dans le cloud, jamais dans Obsidian.

Trois : je ne connecte jamais mon wallet à un site inconnu.

Quatre : je ne signe jamais une transaction que je ne comprends pas.

Cinq : je ne copie jamais une adresse depuis l'historique. Je garde mes adresses de confiance dans un carnet d'adresses, je vérifie l'adresse en entier, et pour un gros montant, j'envoie d'abord un petit test.

Six : je n'interagis jamais avec un token ou un NFT reçu sans l'avoir demandé.

Sept : je me méfie de tout message privé qui propose aide ou gain.

## Questions

Trois questions pour te tester.

Question 1. Où sont réellement stockées tes cryptos ?

[pause 6]

Réponse : sur la blockchain. Ton wallet contient seulement les clés qui prouvent qu'elles t'appartiennent.

Question 2. Comment l'address poisoning peut-il te faire envoyer ton argent à un arnaqueur ?

[pause 8]

Réponse : un bot place dans ton historique une fausse adresse qui commence et finit comme une vraie. Si tu la copies depuis ton historique, tu envoies ton argent à l'arnaqueur.

Question 3. Un token « FREE-ETH-CLAIM point com » apparaît dans ton wallet. Que fais-tu ?

[pause 6]

Réponse : rien. Tu n'y touches pas et tu ne visites pas le site. Ce qui arrive sans que tu l'aies demandé est un piège.

## Fin

C'est la fin de l'épisode 3. Les notes complètes sont dans ton coffre, leçons 5 et 6, et le lien est dans la description. Passe le quiz sur ton téléphone. À bientôt.
