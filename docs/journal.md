TP1 : 

Q1. Combien de temps s'est écoulé entre votre premier commit et sa fusion sur main ?

Sur le premier commit, il s'est déroulé à 13h49 au niveau de GitHub et la fusion a été fait sur main a été fait à 14h50. Il y a eu donc 1H environ entre les commits fait par Yakup et l'approbation / fusion par Timmy. 

Q2. Qu'est-ce qui, dans ce TP, ne dépend pas de GitHub ?
Les commandes Git : les branches, les commits, les tags et les hooks pre-commit fonctionnent indépendamment de GitHub. Ils seraient utilisables sur GitLab, Gitea ou Forgejo sans modification majeure.
En revanche, les commandes gh, l'interface des Pull Requests, les règles de protection de branches et les workflows GitHub Actions sont spécifiques à GitHub. Sur une autre forge, il faudrait adapter ces outils et leur configuration.

Q3. Pourquoi signer les commits si la forge vérifie déjà qui pousse ?

La forge vérifie seulement qui a poussé, pas qui a écrit le commit : n'importe qui peut mettre le nom et l'e-mail d'un autre. 
La signature est attachée au commit : elle prouve l'auteur et reste vrai si le dépôt est cloné et poussé par quelqu'un d'autre. 
