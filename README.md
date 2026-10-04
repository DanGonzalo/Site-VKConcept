# VK CONCEPT

Site de présentation de VK CONCEPT, partenaire IT entre la France et le Vietnam : développement logiciel, intelligence artificielle et renfort d’équipes.

## Technologies

HTML, CSS et JavaScript natifs ; Three.js r160 pour le monogramme en verre et les animations. Les bibliothèques, polices et assets sont inclus localement. Python 3 prépare la version publique, sans dépendances supplémentaires.

## Aperçu local

```sh
python3 -B serve.py 5180
```

Ouvrir http://127.0.0.1:5180. Le formulaire prépare un e-mail dans la messagerie du visiteur ; il ne transmet pas de message à un serveur.

## Publication

```sh
python3 -B build_public.py
python3 -m http.server 5181 --bind 127.0.0.1 --directory dist
```

La sortie `dist/` contient uniquement les fichiers nécessaires au site et les licences tierces. Le build refuse une destination déjà existante : utiliser `--out` avec un nouveau dossier pour refaire un build sans effacement.

GitHub Pages publie cette sortie à chaque mise à jour de `main`. Voir [DEPLOYMENT.md](DEPLOYMENT.md) pour la configuration initiale.

## Maintenance

Modifier `index.html`, `css/styles.css` et `js/app.js`. L’export autonome facultatif se régénère avec `python3 -B build_monofichier.py` et reste exclu du dépôt. Le brief JSON historique est exclu et n’est pas la source de la version actuelle.

## Licences

Les licences de Three.js et Space Grotesk figurent dans `licenses/`. L’identité VK CONCEPT et les contenus du site ne sont pas placés sous une licence libre par la publication du dépôt.
