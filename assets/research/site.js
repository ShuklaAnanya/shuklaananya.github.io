(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector('.theme-toggle');
  function updateThemeButton() {
    const dark = root.dataset.theme === 'dark';
    const label = `Switch to ${dark ? 'light' : 'dark'} theme`;
    themeButton.setAttribute('aria-label', label);
    themeButton.title = label;
    document.querySelector('meta[name="theme-color"]').content = dark ? '#101715' : '#ffffff';
  }
  themeButton.hidden = false;
  updateThemeButton();
  themeButton.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('ananya-theme', next); } catch (e) {}
    updateThemeButton();
  });
  const nav = document.querySelector('.navigation');
  const menu = document.querySelector('.menu-toggle');
  const links = [...document.querySelectorAll('[data-section]')];
  nav.classList.add('enhanced');
  menu.hidden = false;
  function closeMenu() {
    nav.classList.remove('menu-open');
    menu.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-label', 'Open navigation');
  }
  menu.addEventListener('click', () => {
    const open = nav.classList.toggle('menu-open');
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('menu-open')) {
      closeMenu();
      menu.focus();
    }
  });
  document.addEventListener('click', event => {
    if (!nav.contains(event.target)) closeMenu();
  });
  links.forEach(link => link.addEventListener('click', closeMenu));
  window.matchMedia('(min-width: 801px)').addEventListener('change', closeMenu);
  const sections = links.map(link => document.getElementById(link.dataset.section)).filter(Boolean);
  let pending = false;
  function updateActiveSection() {
    let active = null;
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= 140) active = section.id;
    }
    links.forEach(link => {
      if (link.dataset.section === active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    pending = false;
  }
  window.addEventListener('scroll', () => {
    if (!pending) { pending = true; requestAnimationFrame(updateActiveSection); }
  }, { passive: true });
  window.addEventListener('resize', updateActiveSection);
  updateActiveSection();
})();
