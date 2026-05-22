const scrollButtons = document.querySelectorAll('[data-scroll-target]');

scrollButtons.forEach(button => {
  button.addEventListener('click', () => {
    const targetId = button.dataset.scrollTarget;
    const targetSection = document.getElementById(targetId);
    if (targetSection) {
      targetSection.scrollIntoView({
        behavior: 'smooth'
      });
    }
  });
});