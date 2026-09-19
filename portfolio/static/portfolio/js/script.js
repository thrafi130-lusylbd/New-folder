(function () {
  // ---- Mobile nav toggle ----
  var navToggle = document.getElementById('navToggle');
  var navLinks = document.getElementById('navLinks');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var open = navLinks.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', String(open));
    });
    navLinks.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        navLinks.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ---- Lamp pull-cord ----
  var scene = document.getElementById('lampScene');
  var pull = document.getElementById('lampPull');
  if (!scene || !pull) return;

  var isOn = false;
  var animating = false;

  function toggleLamp() {
    if (animating) return;
    animating = true;

    pull.classList.add('is-pulling');
    isOn = !isOn;

    window.setTimeout(function () {
      scene.classList.toggle('is-on', isOn);
      pull.setAttribute('aria-pressed', String(isOn));
      pull.setAttribute(
        'aria-label',
        isOn ? 'Pull the cord to switch the light off' : 'Pull the cord to switch the light on'
      );
    }, 140);

    window.setTimeout(function () {
      pull.classList.remove('is-pulling');
      animating = false;
    }, 520);
  }

  pull.addEventListener('click', toggleLamp);
  pull.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggleLamp();
    }
  });
})();
