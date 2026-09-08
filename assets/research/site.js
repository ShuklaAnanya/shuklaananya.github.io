(() => {
  const root = document.documentElement;
  const themeButton = document.querySelector(".theme-toggle");
  function updateThemeButton() {
    const dark = root.dataset.theme === "dark";
    const label = `Switch to ${dark ? "light" : "dark"} theme`;
    themeButton.setAttribute("aria-label", label);
    themeButton.title = label;
    document.querySelector('meta[name="theme-color"]').content = dark ? "#0a0a0a" : "#ffffff";
  }
  themeButton.hidden = false;
  updateThemeButton();
  themeButton.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    try {
      localStorage.setItem("ananya-theme", next);
    } catch (e) {}
    updateThemeButton();
  });
  const nav = document.querySelector(".navigation");
  const menu = document.querySelector(".menu-toggle");
  const links = [...document.querySelectorAll("[data-section]")];
  nav.classList.add("enhanced");
  menu.hidden = false;
  function closeMenu() {
    nav.classList.remove("menu-open");
    menu.setAttribute("aria-expanded", "false");
    menu.setAttribute("aria-label", "Open navigation");
  }
  menu.addEventListener("click", () => {
    const open = nav.classList.toggle("menu-open");
    menu.setAttribute("aria-expanded", String(open));
    menu.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && nav.classList.contains("menu-open")) {
      closeMenu();
      menu.focus();
    }
  });
  document.addEventListener("click", (event) => {
    if (!nav.contains(event.target)) closeMenu();
  });
  links.forEach((link) => link.addEventListener("click", closeMenu));
  window.matchMedia("(min-width: 801px)").addEventListener("change", closeMenu);
  const sections = links.map((link) => document.getElementById(link.dataset.section)).filter(Boolean);
  let pending = false;
  function updateActiveSection() {
    const distance = document.documentElement.scrollHeight - window.innerHeight;
    document.querySelector(".reading-progress span").style.transform =
      `scaleX(${distance > 0 ? Math.min(1, Math.max(0, window.scrollY / distance)) : 0})`;
    let active = null;
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= 140) active = section.id;
    }
    if (sections.length && window.scrollY > 0 && window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
      active = sections[sections.length - 1].id;
    }
    links.forEach((link) => {
      if (link.dataset.section === active) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
    pending = false;
  }
  window.addEventListener(
    "scroll",
    () => {
      if (!pending) {
        pending = true;
        requestAnimationFrame(updateActiveSection);
      }
    },
    { passive: true }
  );
  window.addEventListener("resize", updateActiveSection);
  document.querySelector(".news-archive")?.addEventListener("toggle", updateActiveSection);
  new ResizeObserver(updateActiveSection).observe(document.body);
  updateActiveSection();
})();
