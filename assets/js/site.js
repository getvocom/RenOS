// Navigation, forms and the pricing toggle. No dependencies.
(function () {
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('nav-menu');
  var items = Array.prototype.slice.call(document.querySelectorAll('.nav-item'));
  var desktop = window.matchMedia('(min-width: 1061px)');

  // ---- Mega menu
  function closeAll(except) {
    items.forEach(function (item) {
      if (item === except) return;
      item.classList.remove('is-open');
      item.querySelector('.nav-top').setAttribute('aria-expanded', 'false');
    });
  }
  function setItem(item, open) {
    closeAll(open ? item : null);
    item.classList.toggle('is-open', open);
    item.querySelector('.nav-top').setAttribute('aria-expanded', String(open));
  }
  items.forEach(function (item) {
    var btn = item.querySelector('.nav-top');
    var links = Array.prototype.slice.call(item.querySelectorAll('.mega a'));
    btn.addEventListener('click', function () {
      setItem(item, !item.classList.contains('is-open'));
    });
    item.addEventListener('mouseenter', function () { if (desktop.matches) setItem(item, true); });
    item.addEventListener('mouseleave', function () { if (desktop.matches) setItem(item, false); });
    item.addEventListener('keydown', function (e) {
      var i = links.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (!item.classList.contains('is-open')) setItem(item, true);
        links[Math.min(i + 1, links.length - 1)].focus();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (i > 0) links[i - 1].focus(); else btn.focus();
      } else if (e.key === 'Escape') {
        setItem(item, false);
        btn.focus();
      }
    });
    item.addEventListener('focusout', function (e) {
      if (desktop.matches && !item.contains(e.relatedTarget)) setItem(item, false);
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-item')) closeAll();
  });

  // ---- Mobile menu
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menu.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open);
  }
  toggle.addEventListener('click', function () {
    setMenu(toggle.getAttribute('aria-expanded') !== 'true');
  });
  menu.addEventListener('click', function (e) {
    if (e.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && menu.classList.contains('is-open')) setMenu(false);
  });
  desktop.addEventListener('change', function () { setMenu(false); closeAll(); });

  function onScroll() {
    header.classList.toggle('is-scrolled', window.scrollY > 8);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ---- Contact form: prefill the request type from ?type=
  var type = new URLSearchParams(location.search).get('type');
  var typeSelect = document.querySelector('select[name="type"]');
  if (type && typeSelect && typeSelect.querySelector('option[value="' + type + '"]')) {
    typeSelect.value = type;
  }

  // ---- Lead forms
  document.querySelectorAll('.lead-form').forEach(function (form) {
    var status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.dataset.endpoint) {
        status.classList.add('is-warn');
        status.textContent = "Thanks. This form isn't connected yet, so nothing was sent. Please email us instead while we finish setting it up.";
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error(r.status);
          form.reset();
          status.classList.remove('is-warn');
          status.textContent = "Thanks. We'll be in touch within one business day.";
        })
        .catch(function () {
          status.classList.add('is-warn');
          status.textContent = 'Something went wrong sending the form. Please try again.';
        })
        .then(function () { btn.disabled = false; });
    });
  });

  // ---- Pricing: annual / monthly
  var billing = document.querySelectorAll('.billing button');
  billing.forEach(function (b) {
    b.addEventListener('click', function () {
      var monthly = b.dataset.bill === 'monthly';
      billing.forEach(function (x) {
        x.classList.toggle('is-on', x === b);
        x.setAttribute('aria-pressed', String(x === b));
      });
      document.querySelectorAll('[data-monthly]').forEach(function (el) { el.hidden = !monthly; });
      document.querySelectorAll('[data-monthly]').forEach(function (el) {
        var annual = el.parentNode.querySelector('[data-annual]');
        if (annual) annual.hidden = monthly;
      });
    });
  });
})();
