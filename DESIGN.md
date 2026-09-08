# Research website redesign

Approved direction: a compact, single-page research website informed by Amol Harsh's typography, section rhythm, and publication lists. Jekyll remains the static generator; this site uses a dedicated Liquid layout within the existing al-folio repository.

- Order: Profile, News, Experience, Publications, Talks & Presentations, Education, Services.
- Deep green-teal (#087f73) complements the existing portrait. Dark mode uses #71d4bf on #101715. Light mode is the first-visit default.
- Inter is served locally under its SIL Open Font License. SVG icons need no icon font or library.
- Content remains visible without JavaScript. JavaScript adds the theme switch, mobile menu, and active section indicator. Native details/summary expands older news.
- No fabricated interests, publication metadata, or links. Papers come from the existing bibliography, and FastConformation is labeled as a preprint.
- Existing /publications/, /news/, and /cv/ URLs use the same components. Template demos stay in source and are excluded from publication.
- The GitHub Pages artifact workflow is the single deployment path. No application server or frontend framework is needed.

## Content editing

- Biography: `_pages/about.md`
- Contact links and future interests: `_data/profile.yml`
- News (month precision): `_data/news.yml`
- Positions and supervisors: `_data/experience.yml`
- Talks, education, services: `_data/academic.yml`
- Papers: `_bibliography/papers.bib`

Publication fields: `title`, `author`, `booktitle` (or `journal`), `year`. Optional `doi`, `arxiv`, or `pdf` supply the Paper link; `website` supplies Project Page; `code` supplies GitHub. Missing links are omitted. The renderer highlights Ananya Shukla automatically. Keep existing abstracts and other BibTeX metadata in source for future use.

## Local verification

Use Ruby 3.2+ and Bundler 2.7.2:

```sh
bundle install
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
bundle exec jekyll serve --host 127.0.0.1
```

For browser verification, install Python Playwright and Chromium, then run:

```sh
python3 scripts/inspect_site.py
```

This checks light/dark, mobile/desktop, navigation, disclosure, theme persistence, no-JavaScript rendering, and captures screenshots in `/tmp/ananya-site-review`. Inspect the screenshots as part of every design review.
