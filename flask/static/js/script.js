window.addEventListener('load', () => {
    const btn = document.querySelector('.btn-get-started');
    btn.style.opacity = 0;
    btn.style.transform = 'translateY(10px)';
    setTimeout(() => {
      btn.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      btn.style.opacity = 1;
      btn.style.transform = 'translateY(0)';
    }, 300); // pequeno atraso ao carregar
  });