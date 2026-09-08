---
layout: research
title: About
permalink: /
---

<section class="hero" id="top" aria-labelledby="profile-title">
  <div class="hero-heading">
    <div>
      <p class="eyebrow">Microsoft · M365 Copilot</p>
      <h1 id="profile-title">Ananya Shukla</h1>
      <p class="hero-role">Research Fellow <span class="role-separator">@</span> Microsoft M365 Copilot</p>
      <p class="location">{% include research/icon.liquid name='pin' %} {{ site.data.profile.location }}</p>
    </div>
    <img class="portrait" src="{{ site.data.profile.portrait | relative_url }}" alt="Ananya Shukla" width="960" height="1280" fetchpriority="high">
  </div>
  <div class="biography">
    <p>I am a Research Fellow with the M365 Copilot team at Microsoft, working on <strong>Self-Evolving Agents</strong> and <strong>Recursive Self-Improvement</strong>.</p>
    <p>Previously, I worked on Multimodal and Vision-Language Models for Radiology and Compositional Clinical Reasoning through <a href="https://www.microsoft.com/en-us/research/project/care/">Project CARE</a> at Microsoft Research. I have also worked with the Image, Informatics &amp; Intelligence (i3) Lab at Harvard Medical School, the Rubenstein Lab at Brown University, and the Biomolecular Computation Lab at the Indian Institute of Science (IISc).</p>
  </div>
  <div class="contact-links" aria-label="Contact and profiles">
    <a href="mailto:{{ site.data.profile.email }}">{% include research/icon.liquid name='email' %} {{ site.data.profile.email }}</a>
    {% for link in site.data.profile.links %}<a href="{{ link.url | escape }}">{% include research/icon.liquid name=link.icon %} {{ link.label }}</a>{% endfor %}
  </div>
  {% if site.data.profile.interests.size > 0 %}<ul class="interests" aria-label="Research interests">{% for interest in site.data.profile.interests %}<li>{{ interest }}</li>{% endfor %}</ul>{% endif %}
</section>
{% include research/news.liquid %}
{% include research/experience.liquid %}
{% include research/publications.liquid %}
{% include research/talks.liquid %}
{% include research/education.liquid %}
{% include research/services.liquid %}
