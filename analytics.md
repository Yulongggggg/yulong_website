---
title: Analytics
nav: true
nav_order: 7
permalink: /analytics/
layout: page
heading: Visit overview and countries.
description: Private visitor analytics snapshot pulled during deployment.
---

{% assign snapshot = site.data["analytics-snapshot"] %}

<section class="analytics-hero">
  <p class="section-copy">This page stays lightweight on purpose. The snapshot is generated during deployment from GoatCounter and is not hard-coded into the front-end.</p>
</section>

{% if snapshot.connected %}
  <section class="analytics-grid">
    <div class="analytics-summary">
      <div class="analytics-card">
        <p class="analytics-label">Visits</p>
        <p class="analytics-value">{{ snapshot.totalVisitors }}</p>
        <p class="analytics-copy">All-time GoatCounter snapshot</p>
      </div>

      <div class="analytics-card">
        <p class="analytics-label">Countries</p>
        <p class="analytics-value">{{ snapshot.countries | size }}</p>
        <p class="analytics-copy">Places where visits have come from</p>
      </div>

      <div class="analytics-card">
        <p class="analytics-label">Updated</p>
        <p class="analytics-value analytics-value--small">{{ snapshot.generatedAt | date: "%b %-d, %Y, %-I:%M %p" }}</p>
        <p class="analytics-copy">Refreshed automatically during deployment</p>
      </div>
    </div>

    <div class="analytics-country-card">
      <p class="analytics-label">Countries</p>
      <ul class="analytics-country-list">
        {% for country in snapshot.countries %}
          <li class="analytics-country-item">
            <span class="analytics-country-icon" aria-hidden="true">{% if country.flag and country.flag != "" %}{{ country.flag }}{% else %}•{% endif %}</span>
            <span class="analytics-country-name">{{ country.name }}</span>
            <span class="analytics-country-count">{{ country.count }}</span>
          </li>
        {% endfor %}
      </ul>
    </div>
  </section>
{% else %}
  <section class="content-card">
    <p class="section-copy">Analytics is connected, but the first private snapshot has not been generated yet. Push once after adding <code>GOATCOUNTER_API_TOKEN</code>, or rerun the deploy workflow from GitHub Actions.</p>
  </section>
{% endif %}
