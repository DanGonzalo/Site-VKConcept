"""Create an isolated static release, without changing the site's sources."""
from pathlib import Path
from html.parser import HTMLParser
import argparse
import re
import shutil

ROOT = Path(__file__).resolve().parent

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and value and value.startswith('./'):
                self.paths.append(value.split('?')[0])

def build(output):
    output = output.resolve()
    if output.exists():
        raise SystemExit('Destination already exists. Choose a new --out directory; no files were changed.')
    # Validate the actual browser entry point and every local CSS dependency.
    html = (ROOT / 'index.html').read_text()
    refs = References()
    refs.feed(html)
    for ref in refs.paths:
        if not (ROOT / ref).is_file():
            raise SystemExit(f'Missing asset: {ref}')
    for css in (ROOT / 'css').glob('*.css'):
        for ref in re.findall(r'url\([\"\']?([^\)\"\']+)', css.read_text()):
            if ref.startswith(('data:', 'https:', 'http:')):
                continue
            if not (css.parent / ref.split('?')[0]).resolve().is_file():
                raise SystemExit(f'Missing CSS asset: {ref}')
    app = (ROOT / 'js/app.js').read_text()
    for ref in re.findall(r'[\"\'](\./assets/[^\"\']+)[\"\']', app):
        if not (ROOT / ref).is_file():
            raise SystemExit(f'Missing script asset: {ref}')
    output.mkdir(parents=True)
    shutil.copy2(ROOT / 'index.html', output / 'index.html')
    for folder in ('css', 'js', 'vendor', 'licenses'):
        shutil.copytree(ROOT / folder, output / folder, ignore=shutil.ignore_patterns('.DS_Store', '__pycache__', '*.pyc'))
    for folder in ('brand', 'shapes', 'fonts'):
        shutil.copytree(ROOT / 'assets' / folder, output / 'assets' / folder, ignore=shutil.ignore_patterns('.DS_Store'))
    (output / '.nojekyll').touch()
    print(f'Static release ready: {output}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=ROOT / 'dist')
    build(parser.parse_args().out)
