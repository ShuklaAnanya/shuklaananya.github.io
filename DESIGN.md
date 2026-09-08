# Research website redesign

Approved direction: a compact, single-page research website informed by Amol Harsh's typography, section rhythm, and publication lists. Jekyll remains the static generator; this site uses a dedicated Liquid layout within the existing al-folio repository.

- Order: Profile, News, Experience, Publications, Talks & Presentations, Services, Education.
- Deep green-teal (#087f73) complements the existing portrait. Dark mode uses #71d4bf on #101715. Light mode is the first-visit default.
- The name uses a locally served Google Sans Bold subset. Body text uses Inter, served locally as a Latin subset under its SIL Open Font License. The original font remains in source; only the subset ships. SVG icons need no icon font or library.
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

Publication fields: `title`, `author`, `booktitle` (or `journal`), `year`. Optional `html`, `doi`, `arxiv`, or `pdf` supply the Paper link; `website` supplies Project Page; `code` supplies GitHub. Missing links are omitted. The renderer highlights Ananya Shukla automatically. Keep existing abstracts and other BibTeX metadata in source for future use.

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

## Final verification — September 8, 2026

- Strict Jekyll build succeeds; five HTML pages, internal assets, anchors, sitemap, and required content pass checks.
- Browser checks pass at 1440, 768, 390, and 320px in light and dark modes. No horizontal overflow, failed assets, or JavaScript errors. Theme persistence, mobile menu/Escape, anchor positioning, news expansion, no-JavaScript content, and reduced motion verified.
- Rendered desktop and mobile screenshots reviewed for hierarchy, portrait framing, typography, and all sections.
- Axe 4.10.3: zero violations across five pages in both themes (WCAG 2 A/AA, WCAG 2.1 AA, and best-practice rules).
- Local Lighthouse mobile audit: Performance 96, Accessibility 100, Best Practices 100, SEO 100. These are localhost lab results, not measurements of the deployed site. The largest remaining asset is the unchanged original portrait; GitHub Pages controls HTTP compression and cache headers.
- External links: 14 returned HTTP 200. IEEE Xplore returned 418 and LinkedIn 999 to the automated checker; user-provided URLs remain intact.
- Formatting and JavaScript syntax checks pass. The optional published-site Lighthouse workflow now audits the correct site without committing report files.

Screenshots and machine-readable audit reports from this run are in `/tmp/ananya-site-review`. The local preview is served at `http://127.0.0.1:4000` while its server process is running. Publishing requires pushing the commits to GitHub; this implementation does not push automatically.

## Requested refinements — September 8, 2026

Removed the header wordmark, the repeated Microsoft eyebrow, and News from navigation. The name now uses Google Sans Bold (700), with a 1.8KB local WOFF2 subset and its OFL license. The original 960×1280 portrait is framed as a face-focused circle using CSS; no image pixels were changed.

News uses sentence case while retaining proper names and acronyms; ReXGroundingCT Challenge is linked. Experience has institution marks on the right, with one Microsoft mark and an indented line joining its two roles. Logo source details are in `assets/research/logos/SOURCES.txt`; white backgrounds keep dark marks legible in either theme, and the Plaksha white mark uses charcoal.

Added all three supplied GitHub links, labeling GuideAI as private, and Brenda Rubenstein's profile. Talks now place title first, followed by date/time, session/topic, and poster/location. Services immediately follows Talks, uses review/organization icons, and uses ordinary hyphens in committee descriptions. Education includes the Plaksha mark. A two-pixel scroll progress indicator updates on scroll, resize, and news expansion.

Rebuilt and visually checked desktop, tablet, and mobile in both themes. Updated browser regression checks pass at 1440, 768, 390, and 320px, including progress completion, logo presence, grouped roles, private-repository labeling, and section order. Axe reports zero violations across all five pages in both themes. The earlier Lighthouse score records the first redesign milestone, before these refinements.

### Review adjustment (approved design)

Restored the original title-style capitalization in news, including Cognition-Aware Adaptive Learning and Spatial Prior-Guided Neonatal HIE Lesion Segmentation. Narrowed the centered reading column from 860px to 780px. Institution logos now lead Experience and Education entries on the left, aligned beside the text, with compact institution headings and the existing grouped Microsoft roles. This supersedes the earlier right-aligned logo and sentence-case choices.

### Margin and dark-theme adjustment (approved design)

The reading column is now 720px wide, matching the reference's effective text width and increasing horizontal whitespace (360px on each side of a 1440px screen). Small-screen gutters remain usable at 20px. Dark mode uses neutral #0a0a0a with neutral gray text, borders, and surfaces; teal remains the accent. Education uses Plaksha's official coloured logo on a white backing in both themes. These choices supersede earlier widths, tinted dark surfaces, and the white Plaksha mark.

Brown now uses the complete official university logo, exported from its SVG sprite with the original viewBox and paths intact, replacing the shield-only favicon.
