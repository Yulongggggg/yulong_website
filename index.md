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
    <p class="page-kicker">Computational geomechanics · Scientific machine learning</p>
    <h1 class="hero-headline">Building AI that understands the physics beneath our feet.</h1>
    <p class="hero-lead">
      I am Yulong Liu, a Ph.D. student at Cornell working at the intersection of computational geomechanics, poromechanics, reservoir simulation, and scientific machine learning.
    </p>
    <div class="hero-actions">
      <a class="cta-button cta-button--primary" href="{{ '/research/' | relative_url }}">Explore my research <span aria-hidden="true">↗</span></a>
      <a class="cta-button" href="{{ '/assets/pdf/Yulong_CV2026_V2.pdf' | relative_url }}?v={{ site.time | date: '%s' }}" target="_blank" rel="noreferrer">Download CV</a>
    </div>
  </div>
  <div class="hero-visual">
    <div class="hero-photo">
      <img src="{{ '/assets/img/yulong-liu-portrait.jpeg' | relative_url }}" alt="Portrait of Yulong Liu">
    </div>
    <p class="portrait-caption"><span>01</span> Yulong Liu<br>Ph.D. student · Cornell EAS</p>
  </div>
</section>

<section class="profile-strip" aria-label="Profile at a glance">
  <div>
    <span class="strip-label">Based at</span>
    <strong>Cornell University</strong>
  </div>
  <div>
    <span class="strip-label">Advisor</span>
    <strong><a href="https://arsonlab.engineering.cornell.edu/" target="_blank" rel="noreferrer">Chloé Arson ↗</a></strong>
  </div>
  <div>
    <span class="strip-label">Core methods</span>
    <strong>PINNs · INRs · Operators · LLMs</strong>
  </div>
  <div>
    <span class="strip-label">Current focus</span>
    <strong>Subsurface &amp; reservoir systems</strong>
  </div>
</section>

<section class="home-section">
  <div class="section-heading section-heading--split">
    <div>
      <p class="page-kicker">Now / 2026</p>
      <h2 class="section-title">Recent signals.</h2>
    </div>
    <p class="section-intro">New publications, proposals, and computing allocations supporting physics-aware AI for geomechanics.</p>
  </div>

  <div class="signal-grid">
    <article class="signal-card signal-card--accent">
      <div class="signal-topline"><span>Publication</span><span>2026</span></div>
      <h3>Physics-informed neural modeling of pressurized cavities in heterogeneous rock.</h3>
      <p><em>Rock Mech Rock Eng</em> · DOI 10.1007/s00603-026-05882-5</p>
      <a class="card-link" href="https://doi.org/10.1007/s00603-026-05882-5" target="_blank" rel="noreferrer">View article <span aria-hidden="true">↗</span></a>
    </article>

    <article class="signal-card">
      <div class="signal-topline"><span>NASA FINESST</span><span>Under review</span></div>
      <h3>A physics-guided subsurface Earth-system model for uncertainty-aware geothermal prediction.</h3>
      <p>Future Investigator: Y. Liu · PI: C. Arson</p>
    </article>

    <article class="signal-card">
      <div class="signal-topline"><span>NSF ACCESS</span><span>1.5M CPU hours</span></div>
      <h3>Learned uncertainty propagation and world models for enhanced geothermal reservoirs.</h3>
      <p>Student lead: Y. Liu · Advisor: C. Arson</p>
    </article>

    <article class="signal-card">
      <div class="signal-topline"><span>Empire AI Alpha+Beta</span><span>5.5K GPU hours</span></div>
      <h3>AI-aided computational geomechanics.</h3>
      <p>PIs: Y.C. Han, Y. Liu, A. Tristani, C. Arson</p>
    </article>
  </div>
</section>

<section class="home-section">
  <div class="section-heading section-heading--split">
    <div>
      <p class="page-kicker">Research / Selected</p>
      <h2 class="section-title">From equations to decisions.</h2>
    </div>
    <p class="section-intro">I connect high-fidelity multiphysics simulation with models that are faster, interpretable, and physically grounded.</p>
  </div>

  <div class="featured-work">
    <article class="featured-card featured-card--large">
      <figure class="featured-figure">
        <img src="{{ '/assets/img/research-results/generalization-1.png' | relative_url }}" alt="Generalization comparison across fracture configurations.">
      </figure>
      <div class="featured-copy">
        <p class="project-index">01 / Operator learning</p>
        <h3>Fast surrogates for geothermal injection-production systems.</h3>
        <p>Learning the response of fractured reservoirs without losing the geometry and physics that make each system distinct.</p>
      </div>
    </article>

    <article class="featured-card">
      <figure class="featured-figure featured-figure--field">
        <img src="{{ '/assets/img/research-results/fig11-1layer-30.png' | relative_url }}" alt="Displacement, stress, and error fields around a pressurized cavity.">
      </figure>
      <div class="featured-copy">
        <p class="project-index">02 / Physics-informed AI</p>
        <h3>Geometry-aware cavity mechanics.</h3>
        <p>PINNs for arbitrary smooth cavities embedded in heterogeneous rock.</p>
      </div>
    </article>
  </div>

  <a class="text-route" href="{{ '/research/' | relative_url }}">See the full research map <span aria-hidden="true">→</span></a>
</section>

<section class="home-section home-section--papers">
  <div class="section-heading">
    <p class="page-kicker">Selected papers</p>
    <h2 class="section-title">Work in mechanics, Earth systems, and reliable AI.</h2>
  </div>
  <div class="paper-teasers">
    <a class="paper-teaser" href="{{ '/publications/' | relative_url }}">
      <span class="paper-year">2026</span>
      <span class="paper-title">A Physics-Informed Neural Network for Pressurized Cavities of Arbitrary Shape in Heterogeneous Rock</span>
      <span class="paper-status status-accepted">Journal</span>
    </a>
    <a class="paper-teaser" href="https://arxiv.org/abs/2605.09360" target="_blank" rel="noreferrer">
      <span class="paper-year">2026</span>
      <span class="paper-title">Your Simulation Runs but Solves the Wrong Physics</span>
      <span class="paper-status">NeurIPS review</span>
    </a>
    <a class="paper-teaser" href="{{ '/publications/' | relative_url }}">
      <span class="paper-year">2026</span>
      <span class="paper-title">Operator Learning Surrogate Modeling of Hydraulically Fractured Geothermal Injection-Production Systems</span>
      <span class="paper-status">ARMA</span>
    </a>
  </div>
</section>

<section class="contact-band">
  <p class="page-kicker">Start a conversation</p>
  <h2>Interested in physics-aware AI for subsurface systems?</h2>
  <a href="mailto:yl3825@cornell.edu">yl3825@cornell.edu <span aria-hidden="true">↗</span></a>
</section>
