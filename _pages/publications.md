---
layout: page
permalink: /publications/
title: Publications
description: Publications by categories in reversed chronological order.
nav: true
nav_order: 2
---

<div class="publications">
  <div class="publications-intro">
    <p class="publications-intro__eyebrow">Research portfolio</p>
    <p class="publications-intro__summary">
      <strong><span data-publication-count></span> publications</strong> spanning medical imaging, human-centered AI, and computational biology.
    </p>
  </div>

{% include bib_search.liquid %}
{% bibliography %}

</div>
