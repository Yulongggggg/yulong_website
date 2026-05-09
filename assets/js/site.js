const resultsTriggers = [...document.querySelectorAll('[data-results-open]')];
const resultsLightbox = document.querySelector('[data-results-lightbox]');
const resultsImage = resultsLightbox?.querySelector('[data-results-image]');
const resultsClose = [...(resultsLightbox?.querySelectorAll('[data-results-close]') || [])];

const openResultsLightbox = (trigger) => {
  if (!resultsLightbox || !(resultsImage instanceof HTMLImageElement)) return;
  const { resultsSrc, resultsAlt } = trigger.dataset;
  if (!resultsSrc) return;

  resultsImage.src = resultsSrc;
  resultsImage.alt = resultsAlt || '';
  resultsLightbox.hidden = false;
  document.body.style.overflow = 'hidden';
};

const closeResultsLightbox = () => {
  if (!resultsLightbox || resultsLightbox.hidden) return;
  resultsLightbox.hidden = true;
  document.body.style.removeProperty('overflow');
  if (resultsImage instanceof HTMLImageElement) {
    resultsImage.removeAttribute('src');
    resultsImage.removeAttribute('alt');
  }
};

for (const trigger of resultsTriggers) {
  trigger.addEventListener('click', () => openResultsLightbox(trigger));
  trigger.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      openResultsLightbox(trigger);
    }
  });
}

for (const control of resultsClose) {
  control.addEventListener('click', closeResultsLightbox);
}

window.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeResultsLightbox();
  }
});
