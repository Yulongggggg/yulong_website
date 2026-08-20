---
title: Research
nav: true
nav_order: 2
permalink: /research/
layout: page
heading: Physics-aware learning for complex subsurface systems.
description: My research connects high-fidelity mechanics with scientific machine learning that is fast, reliable, and interpretable.
---

<section class="research-manifesto">
  <p class="manifesto-line">Simulation gives us physical fidelity. Learning gives us speed and adaptability. My work asks how to keep both.</p>
</section>

<section class="research-grid">
  <article class="content-card">
    <p class="page-kicker">Simulate</p>
    <h3>Computational geomechanics</h3>
    <p class="section-copy">Coupled thermo-hydro-mechanical models of fractured rock, pressurized cavities, excavation, and reservoir systems using finite elements and MOOSE.</p>
  </article>

  <article class="content-card">
    <p class="page-kicker">Learn</p>
    <h3>Scientific machine learning</h3>
    <p class="section-copy">Physics-informed neural networks, implicit neural representations, and operator learning for geometry-aware, physics-aware prediction.</p>
  </article>

  <article class="content-card">
    <p class="page-kicker">Upscale</p>
    <h3>Reservoirs &amp; porous media</h3>
    <p class="section-copy">Poromechanics, geothermal injection-production, fracture-controlled transport, and multiscale upscaling in porous subsurface media.</p>
  </article>

  <article class="content-card">
    <p class="page-kicker">Verify</p>
    <h3>Reliable AI for simulation</h3>
    <p class="section-copy">PDE-grounded verification and LLM-based systems that reason about physical intent, not just syntactically valid simulation code.</p>
  </article>
</section>

<section class="section-stack project-section">
  <div class="section-heading section-heading--split">
    <div>
      <p class="page-kicker">Selected projects</p>
      <h2 class="section-title">Current research map.</h2>
    </div>
    <p class="section-intro">Three connected scales: local mechanics, reservoir response, and trustworthy AI workflows.</p>
  </div>

  <div class="project-list">
    <article class="project-row">
      <div class="project-number">01</div>
      <div>
        <p class="project-kind">Geothermal reservoirs</p>
        <h3>Operator learning for fractured injection-production systems</h3>
        <p>Surrogate models for rapid evaluation of coupled geothermal scenarios, trained on high-fidelity simulation ensembles.</p>
      </div>
      <figure><img src="{{ '/assets/img/research-results/generalization-1.png' | relative_url }}" alt="Model generalization across fracture configurations."></figure>
    </article>

    <article class="project-row">
      <div class="project-number">02</div>
      <div>
        <p class="project-kind">Rock mechanics</p>
        <h3>Physics-informed cavity mechanics across complex geometry</h3>
        <p>Stress and displacement prediction for arbitrary smooth cavities embedded in heterogeneous rock.</p>
      </div>
      <figure><img src="{{ '/assets/img/research-results/fig11-1layer-30.png' | relative_url }}" alt="Stress and displacement fields around a cavity."></figure>
    </article>

    <article class="project-row">
      <div class="project-number">03</div>
      <div>
        <p class="project-kind">LLMs for science</p>
        <h3>PDE-grounded intent verification</h3>
        <p>Checking whether LLM-generated multiphysics code solves the intended physical problem rather than merely running.</p>
      </div>
      <figure><img src="{{ '/assets/img/research-results/temp-fig1-1.png' | relative_url }}" alt="Workflow figure for physics verification research."></figure>
    </article>
  </div>
</section>
