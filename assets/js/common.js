$(document).ready(function () {
  $("[data-publication-toggle]").click(function () {
    const button = $(this);
    const card = button.closest(".publication-card");
    const targetId = button.attr("aria-controls");
    const target = document.getElementById(targetId);
    const shouldOpen = button.attr("aria-expanded") !== "true";

    card.find("[data-publication-toggle]").attr("aria-expanded", "false");
    card.find(".publication-details").prop("hidden", true);

    if (shouldOpen && target) {
      button.attr("aria-expanded", "true");
      target.hidden = false;
    }
  });
  $("a").removeClass("waves-effect waves-light");

  // bootstrap-toc
  if ($("#toc-sidebar").length) {
    // remove related publications years from the TOC
    $(".publications h2").each(function () {
      $(this).attr("data-toc-skip", "");
    });
    var navSelector = "#toc-sidebar";
    var $myNav = $(navSelector);
    Toc.init($myNav);
    $("body").scrollspy({
      target: navSelector,
      offset: 100,
    });
  }

  // add css to jupyter notebooks
  const cssLink = document.createElement("link");
  cssLink.href = "../css/jupyter.css";
  cssLink.rel = "stylesheet";
  cssLink.type = "text/css";

  let jupyterTheme = determineComputedTheme();

  $(".jupyter-notebook-iframe-container iframe").each(function () {
    $(this).contents().find("head").append(cssLink);

    if (jupyterTheme == "dark") {
      $(this).bind("load", function () {
        $(this).contents().find("body").attr({
          "data-jp-theme-light": "false",
          "data-jp-theme-name": "JupyterLab Dark",
        });
      });
    }
  });

  // trigger popovers
  $('[data-toggle="popover"]').popover({
    trigger: "hover",
  });
});
