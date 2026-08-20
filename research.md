---
title: Research
nav: true
nav_order: 2
permalink: /research/
layout: page
heading: Physics-aware learning for complex subsurface systems
description: My research connects high-fidelity mechanics with scientific machine learning that is fast, reliable, and interpretable.
---

<p class="research-thesis">Simulation gives us physical fidelity. Learning gives us speed and adaptability. My work asks how to keep both.</p>

<section class="research-areas" aria-label="Research areas">
  <div class="area">
    <h3>Computational geomechanics</h3>
    <p>Coupled thermo-hydro-mechanical models of fractured rock, pressurized cavities, excavation, and reservoir systems using finite elements and MOOSE.</p>
  </div>
  <div class="area">
    <h3>Scientific machine learning</h3>
    <p>Physics-informed neural networks, implicit neural representations, and operator learning for geometry-aware, physics-aware prediction.</p>
  </div>
  <div class="area">
    <h3>Reservoirs &amp; porous media</h3>
    <p>Poromechanics, geothermal injection-production, fracture-controlled transport, and multiscale upscaling in porous subsurface media.</p>
  </div>
  <div class="area">
    <h3>Reliable AI for simulation</h3>
    <p>PDE-grounded verification and LLM-based systems that reason about physical intent, not just syntactically valid simulation code.</p>
  </div>
</section>

<section class="section-stack project-section">
  <div class="section-heading section-heading--split">
    <h2 class="section-title">Current projects</h2>
    <p class="section-intro">Local mechanics, reservoir response, and trustworthy AI workflows.</p>
  </div>

  <div class="project-list">
    <article class="project-row">
      <div>
        <p class="project-kind">Geothermal reservoirs</p>
        <h3>Operator learning for fractured injection-production systems</h3>
        <p>Surrogate models for rapid evaluation of coupled geothermal scenarios, trained on high-fidelity simulation ensembles.</p>
      </div>
      <figure><img src="{{ '/assets/img/research-results/generalization-1.png' | relative_url }}" alt="Model generalization across fracture configurations." loading="lazy"></figure>
    </article>

    <article class="project-row">
      <div>
        <p class="project-kind">Rock mechanics</p>
        <h3>Physics-informed cavity mechanics across complex geometry</h3>
        <p>Stress and displacement prediction for arbitrary smooth cavities embedded in heterogeneous rock.</p>
      </div>
      <figure><img src="{{ '/assets/img/research-results/fig11-1layer-30.png' | relative_url }}" alt="Stress and displacement fields around a cavity." loading="lazy"></figure>
    </article>

    <article class="project-row">
      <div>
        <p class="project-kind">LLMs for science</p>
        <h3>PDE-grounded intent verification</h3>
        <p>Checking whether LLM-generated multiphysics code solves the intended physical problem rather than merely running.</p>
      </div>
      <figure><img src="{{ '/assets/img/research-results/temp-fig1-1.png' | relative_url }}" alt="Workflow figure for physics verification research." loading="lazy"></figure>
    </article>
  </div>
</section>
