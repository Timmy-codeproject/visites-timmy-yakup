TP1 :

Q1. Combien de temps s'est écoulé entre votre premier commit et sa fusion sur main ?

Sur le premier commit, il s'est déroulé à 13h49 au niveau de GitHub et la fusion a été fait sur main a été fait à 14h50. Il y a eu donc 1H environ entre les commits fait par Yakup et l'approbation / fusion par Timmy.

Q2. Qu'est-ce qui, dans ce TP, ne dépend pas de GitHub ?
Les commandes Git : les branches, les commits, les tags et les hooks pre-commit fonctionnent indépendamment de GitHub. Ils seraient utilisables sur GitLab, Gitea ou Forgejo.
En revanche, les commandes gh, l'interface des Pull Requests, les règles de protection de branches sont spécifiques à GitHub. Sur une autre forge, il faudrait adapter ces outils et leur configuration.

Q3. Pourquoi signer les commits si la forge vérifie déjà qui pousse ?

La forge vérifie seulement qui a poussé, pas qui a écrit le commit : n'importe qui peut mettre le nom et l'e-mail d'un autre.
La signature est attachée au commit : elle prouve l'auteur et reste vrai si le dépôt est cloné et poussé par quelqu'un d'autre.

TP2 :

<img width="1378" height="250" alt="image" src="https://github.com/user-attachments/assets/75adfb6c-66cd-47da-a4a8-1f99d5dd44bb" />

On a lancé gitleaks sur tout l'historique : 35 commits scannés, aucun secret trouvé. La commande git log --all --oneline -- app/old_settings.py ne renvoie rien : ce fichier n'a jamais existé dans notre dépôt. Notre dépôt a été créé avec le zip du TP01 et pas à partir du dépôt modèle, donc il n'a pas l'historique où le formateur avait caché le faux jeton, que le formateur avait oublié d'inclure. Il n'y a donc pas de commit fautif à identifier ni de .gitleaksignore à écrire.

Q1. Quelles règles auraient empêché le secret d'arriver sur main ?

Plusieurs protections auraient pu empêcher l'introduction du secret : Pull request obligatoire, REquire revieiew from Owner .... La meilleure protection serait toutefois un gitleaks exécuté dans une pipeline CI/CD poiur éviter les erreurs humaines de relecture

Q2. Gitleaks en pre-commit protège-t-il un collègue qui n'a pas installé pre-commit ?
Les hooks pre-commit sont exécutés localement, sur l'ordinateur du développeur. Un collègue qui n'a pas installé les hooks peut donc créer un commit et pousser son code sans exécuter Gitleaks.

Q3. Combien de temps un secret poussé sur une forge publique reste-t-il privé ?
Un secret public est potentiellement compromis dès sa publication. Il faut le révoquer et le remplacer immédiatement car des robots scannent continuellement les dépôts publiques à la recherche de token.
