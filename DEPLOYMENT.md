# Publication GitHub et GitHub Pages

Exécuter depuis le dossier du projet. Le dépôt Git local et son premier commit sont préparés.

```sh
gh auth login -h github.com -p https -w
gh repo create Site-VKConcept --public --source=. --remote=origin --push --description "Site vitrine VK CONCEPT — France · Vietnam"
```

Récupérer l’identité du dépôt et activer GitHub Pages avec GitHub Actions :

```sh
VK_REPO=$(gh repo view --json nameWithOwner --jq .nameWithOwner)
gh api --method POST "repos/$VK_REPO/pages" -f build_type=workflow
gh workflow run pages.yml --ref main
gh run list --workflow pages.yml --limit 5
```

Si Pages est déjà activé, remplacer la commande POST par :

```sh
gh api --method PUT "repos/$VK_REPO/pages" -f build_type=workflow
```

Attendre la réussite du déploiement, puis obtenir les URLs réelles :

```sh
gh repo view --json url --jq .url
gh api "repos/$VK_REPO/pages" --jq .html_url
```

Dans GitHub, la même configuration se trouve sous Settings → Pages → Source → GitHub Actions. L’URL du site doit être testée après le déploiement ; sa présence dans la configuration ne suffit pas à confirmer que le site est prêt.

Pour les mises à jour suivantes :

```sh
git add index.html css js assets
git commit -m "Update VK CONCEPT website"
git push
```

Ne jamais ajouter de secrets au dépôt. Les fichiers `.env`, certificats, caches et sorties générées sont exclus par `.gitignore`.
