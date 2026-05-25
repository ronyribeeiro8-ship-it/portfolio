(function () {
  // Cards com entrada animada
  document.querySelectorAll('.card').forEach(card => {
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting) {
        const delay = ((parseInt(card.dataset.i) - 1) % 3) * 100;
        setTimeout(() => card.classList.add('visible'), delay);
      }
    }, { threshold: .1 }).observe(card);
  });

  // Barras de skill
  document.querySelectorAll('.skill-fill').forEach(f => {
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting) f.classList.add('go');
    }, { threshold: .3 }).observe(f);
  });
})();
