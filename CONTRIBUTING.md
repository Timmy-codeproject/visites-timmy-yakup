# Contribuer à visites

## Flux de travail (GitHub Flow)
1. Partir de `main` à jour : `git switch main && git pull`.
2. Créer une branche courte : `git switch -c feat/ma-fonctionnalite`.
3. Faire de petits commits conventionnels et signés.
4. Pousser la branche et ouvrir une pull request : `gh pr create --base main`.
5. L'autre membre relit : lecture du diff, test en local (`gh pr checkout <num>`), au moins un commentaire.
6. L'auteur corrige par un nouveau commit (jamais `--amend` sur une branche partagée).
7. Après approbation, fusion par squash : `gh pr merge <num> --squash --delete-branch`.

## Convention de commits
Format : `type(zone): description`, au présent.

- `feat` : nouvelle fonctionnalité
- `fix` : correction
- `test` : ajout ou modification de tests
- `docs` : documentation
- `chore` : maintenance (outillage, configuration)

Exemple : `feat(api): ajouter l'endpoint POST /reset`.

## Lancer les tests
~~~bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
~~~

## Lancer pre-commit
~~~bash
pre-commit install
pre-commit run --all-files
~~~
