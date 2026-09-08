"""Browser checks and review screenshots. Requires Python Playwright + Chromium."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
import os

URL = os.environ.get('SITE_URL', 'http://127.0.0.1:4000')
OUT = Path('/tmp/ananya-site-review')
OUT.mkdir(exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch()
    summary = []
    for width, height in [(1440, 1000), (768, 1024), (390, 844), (320, 740)]:
        context = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=1)
        page = context.new_page()
        errors = []
        failed = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('response', lambda response: failed.append(response.url) if response.status >= 400 else None)
        page.goto(URL, wait_until='networkidle')
        page.evaluate('document.fonts.ready')
        assert page.locator('h1').inner_text() == 'Ananya Shukla'
        assert page.locator('.publication').count() == 4
        assert page.locator('.self-author').count() == 4
        assert page.locator('.news-row:visible').count() == 4
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'Overflow at {width}'
        assert page.locator('.portrait').evaluate('(img) => img.complete && img.naturalWidth > 0')
        page.screenshot(path=str(OUT / f'light-{width}.png'), full_page=True)
        page.locator('.news-archive summary').click()
        assert page.locator('.news-row:visible').count() == 7
        page.locator('.news-archive summary').click()
        if width <= 800:
            page.locator('.menu-toggle').click()
            assert page.locator('.menu-toggle').get_attribute('aria-expanded') == 'true'
            page.locator('[data-section="publications"]').click()
            assert page.locator('.menu-toggle').get_attribute('aria-expanded') == 'false'
            page.wait_for_timeout(400)
            assert page.locator('#publications').bounding_box()['y'] >= 55
            page.locator('.menu-toggle').click()
            page.keyboard.press('Escape')
            assert page.locator('.menu-toggle').get_attribute('aria-expanded') == 'false'
        page.locator('.theme-toggle').click()
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        page.reload(wait_until='networkidle')
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        page.evaluate('window.scrollTo({top: 0, behavior: "instant"})')
        page.screenshot(path=str(OUT / f'dark-{width}.png'), full_page=True)
        if width == 1440:
            for section in ['experience', 'publications', 'talks', 'education', 'services']:
                page.locator(f'#{section}').scroll_into_view_if_needed()
                page.screenshot(path=str(OUT / f'dark-{section}.png'))
            page.locator('.theme-toggle').click()
            for section in ['experience', 'publications', 'talks', 'education', 'services']:
                page.locator(f'#{section}').scroll_into_view_if_needed()
                page.screenshot(path=str(OUT / f'light-{section}.png'))
            for route in ['/publications/', '/news/', '/cv/', '/404.html']:
                page.goto(URL + route, wait_until='networkidle')
                assert page.locator('main').inner_text().strip()
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        assert not errors, errors
        assert not failed, failed
        summary.append({'width': width, 'passed': True, 'console_errors': errors, 'failed_assets': failed})
        context.close()
    # Progressive enhancement: all research content and navigation remain available.
    context = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 844})
    page = context.new_page()
    page.goto(URL)
    assert page.locator('.publication').count() == 4
    assert page.locator('[data-section="publications"]').is_visible()
    page.locator('.news-archive summary').click()
    assert page.locator('.news-row:visible').count() == 7
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    context.close()
    context = browser.new_context(reduced_motion='reduce')
    page = context.new_page()
    page.goto(URL)
    assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior') == 'auto'
    context.close()
    browser.close()
    (OUT / 'checks.json').write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))
    print(f'PASS: no-JavaScript and reduced-motion checks. Screenshots: {OUT}')
