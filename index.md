---
title: Yulong Liu
nav_title: About
nav: true
nav_order: 1
permalink: /
layout: page
hide_title: true
body_class: page-about
description: Cornell Ph.D. student working across computational geomechanics, poromechanics, reservoir simulation, and scientific machine learning.
---

<section class="hero-card">
  <div class="hero-copy">
    <p class="hero-badge">Ph.D. student · Cornell University</p>
    <h1 class="hero-headline">Building AI that understands the <em>physics beneath our feet</em>.</h1>
    <p class="hero-lead">
      I am Yulong Liu, a Ph.D. student at Cornell working at the intersection of computational geomechanics, poromechanics, reservoir simulation, and scientific machine learning.
    </p>
    <div class="hero-actions">
      <a class="cta-button cta-button--primary" href="{{ '/research/' | relative_url }}">Explore my research</a>
      <a class="cta-button" href="{{ '/assets/pdf/Yulong_CV2026_V2.pdf' | relative_url }}?v={{ site.time | date: '%s' }}" target="_blank" rel="noreferrer">Download CV</a>
    </div>
  </div>
  <div class="hero-visual">
    <div class="hero-photo">
      <img src="{{ '/assets/img/yulong-liu-portrait.jpeg' | relative_url }}" alt="Portrait of Yulong Liu">
    </div>
  </div>
</section>

<section class="profile-strip" aria-label="Profile at a glance">
  <div>
    <span class="strip-label">Based at</span>
    <strong>Cornell University</strong>
  </div>
  <div>
    <span class="strip-label">Advisor</span>
    <strong><a href="https://arsonlab.engineering.cornell.edu/" target="_blank" rel="noreferrer">Chloé Arson</a></strong>
  </div>
  <div>
    <span class="strip-label">Core methods</span>
    <strong>PINNs · INRs · Operators · LLMs</strong>
  </div>
  <div>
    <span class="strip-label">Focus</span>
    <strong>Subsurface &amp; reservoir systems</strong>
  </div>
</section>

<section class="home-section" aria-label="Featured research">
  <div class="section-heading section-heading--split">
    <div>
      <p class="page-kicker">Research</p>
      <h2 class="section-title">Three connected threads.</h2>
    </div>
    <p class="section-intro">Local mechanics, reservoir response, and trustworthy AI workflows for simulation.</p>
  </div>

  <div class="home-feature-grid">
    <a class="home-feature" href="{{ '/research/' | relative_url }}">
      <figure><img src="{{ '/assets/img/research-results/generalization-1.png' | relative_url }}" alt="Model generalization across fracture configurations." loading="lazy"></figure>
      <div class="home-feature-copy">
        <p class="project-kind">Geothermal reservoirs</p>
        <h3>Operator learning for fractured injection-production systems</h3>
        <p>Fast surrogate models for coupled geothermal scenarios, trained on high-fidelity simulation ensembles.</p>
      </div>
    </a>

    <a class="home-feature" href="{{ '/research/' | relative_url }}">
      <figure><img src="{{ '/assets/img/research-results/fig11-1layer-30.png' | relative_url }}" alt="Stress and displacement fields around a cavity." loading="lazy"></figure>
      <div class="home-feature-copy">
        <p class="project-kind">Rock mechanics</p>
        <h3>Physics-informed cavity mechanics across complex geometry</h3>
        <p>Stress and displacement prediction for arbitrary smooth cavities in heterogeneous rock.</p>
      </div>
    </a>

    <a class="home-feature" href="{{ '/research/' | relative_url }}">
      <figure><img src="{{ '/assets/img/research-results/temp-fig1-1.png' | relative_url }}" alt="Workflow figure for physics verification research." loading="lazy"></figure>
      <div class="home-feature-copy">
        <p class="project-kind">LLMs for science</p>
        <h3>PDE-grounded intent verification</h3>
        <p>Checking whether LLM-generated multiphysics code solves the intended physical problem — not just whether it runs.</p>
      </div>
    </a>
  </div>
  <a class="text-route" href="{{ '/research/' | relative_url }}">See the full research map</a>
</section>

<section class="home-section" aria-label="Selected publications">
  <div class="section-heading section-heading--split">
    <div>
      <p class="page-kicker">Writing</p>
      <h2 class="section-title">Selected publications.</h2>
    </div>
    <p class="section-intro">Journal, conference, and preprint work aligned with the current CV.</p>
  </div>

  <div class="home-pub-list">
    <a class="home-pub" href="{{ '/publications/' | relative_url }}">
      <span class="home-pub-year">2026</span>
      <span>
        <h3>A Physics-Informed Neural Network for Pressurized Cavities of Arbitrary Shape in Heterogeneous Rock</h3>
        <p class="home-pub-venue">Rock Mechanics and Rock Engineering</p>
      </span>
      <span class="home-pub-tag home-pub-tag--journal">Journal</span>
    </a>

    <a class="home-pub" href="{{ '/publications/' | relative_url }}">
      <span class="home-pub-year">2026</span>
      <span>
        <h3>Your Simulation Runs but Solves the Wrong Physics: PDE-Grounded Intent Verification for LLM-Generated Multiphysics Simulation Code</h3>
        <p class="home-pub-venue">arXiv preprint · under review at NeurIPS 2026</p>
      </span>
      <span class="home-pub-tag">Preprint</span>
    </a>

    <a class="home-pub" href="{{ '/publications/' | relative_url }}">
      <span class="home-pub-year">2026</span>
      <span>
        <h3>Operator Learning Surrogate Modeling of Hydraulically Fractured Geothermal Injection-Production Systems</h3>
        <p class="home-pub-venue">ARMA 2026, Tucson</p>
      </span>
      <span class="home-pub-tag">Conference</span>
    </a>
  </div>
  <a class="text-route" href="{{ '/publications/' | relative_url }}">All publications</a>
</section>

<section class="contact-band" aria-label="Contact">
  <p class="page-kicker">Get in touch</p>
  <h2>Open to thoughtful research conversations and collaboration.</h2>
  <p>Geomechanics, poromechanics, scientific machine learning, or reliable AI for simulation — I would love to hear from you.</p>
  <div class="hero-actions">
    <a class="cta-button cta-button--primary" href="mailto:yl3825@cornell.edu">yl3825@cornell.edu</a>
    <a class="cta-button" href="{{ '/contact/' | relative_url }}">More ways to reach me</a>
  </div>
</section>
