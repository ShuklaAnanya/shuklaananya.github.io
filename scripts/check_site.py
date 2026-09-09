"""Validate the generated site's internal targets without third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.errors = []
        self.h1 = 0
        self.text_parts = []
        self.feed(path.read_text())

    def handle_data(self, data):
        self.text_parts.append(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'img' and 'alt' not in attrs:
            self.errors.append('image missing alt')
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

files = list(ROOT.rglob('*.html'))
assert files, f'No HTML found in {ROOT}'
docs = {path: Document(path) for path in files}
errors = []
for path, doc in docs.items():
    errors.extend(f'{path.relative_to(ROOT)}: {e}' for e in doc.errors)
    for link in doc.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/') else (path.parent / unquote(url.path))
        if not url.path:
            target = path
        if target.is_dir():
            target /= 'index.html'
        target = target.resolve()
        if not target.exists():
            errors.append(f'{path.relative_to(ROOT)}: missing target {link}')
        elif url.fragment and target in docs and unquote(url.fragment) not in docs[target].ids:
            errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')

home = ROOT / 'index.html'
assert docs[home].h1 == 1, 'Homepage needs exactly one h1'
for section in ('top', 'news', 'experience', 'publications', 'talks', 'education', 'services'):
    assert section in docs[home].ids, f'Missing section: {section}'
text = ' '.join(''.join(docs[home].text_parts).split())
for content in ('shukla_ananya@outlook.com', 'MedCompose-CT', 'Self-Evolving Agents', 'Recursive Self-Improvement', 'Poster A227', 'ConfAI', 'Preprint'):
    assert content in text, f'Missing content: {content}'
for demo in ('Albert Einstein', 'My website is being developed', 'Paper Title'):
    assert all(demo not in path.read_text() for path in files), f'Template content published: {demo}'
for demo_path in ('blog', 'projects', 'books', 'people', 'assets/json/resume.json'):
    assert not (ROOT / demo_path).exists(), f'Template path published: {demo_path}'
assert (ROOT / 'sitemap.xml').exists(), 'Missing sitemap'
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(files)} HTML pages; internal links/assets/anchors, content, and demo exclusions verified.')
