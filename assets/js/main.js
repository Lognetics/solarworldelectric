/* =========================================================================
   SOLAR WORLD ELECTRIC — main.js
   Nav · scroll motion · hero slider · accordions · filters · tabs
   WhatsApp chat widget (injected site-wide) · 30s lead popup (site-wide)
   ========================================================================= */
(function () {
  'use strict';

  /* ------------------------------------------------------------------
     Config — edit these in one place
     ------------------------------------------------------------------ */
  var CFG = {
    phone: '2349063315492',
    phoneDisplay: '+234 906 331 5492',
    email: 'solarworldes@gmail.com',
    waText: 'Hello Solar World, I am interested in getting your solar and inverter package. Please may I know how to proceed?',
    popupDelay: 30000,          // 30 seconds, per brief
    popupCooldownDays: 7,       // don't re-nag a visitor who closed it
    heroInterval: 7000
  };

  var wa = function (text) {
    return 'https://wa.me/' + CFG.phone + '?text=' + encodeURIComponent(text || CFG.waText);
  };

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private mode */ } }
  };

  /* ------------------------------------------------------------------
     1. Navigation
     ------------------------------------------------------------------ */
  function initNav() {
    var nav = $('#nav');
    if (!nav) return;
    var toggle = $('#navToggle');
    var links = $('#navLinks');
    var lastY = 0;

    function onScroll() {
      var y = window.scrollY;
      nav.classList.toggle('is-stuck', y > 24);
      // hide on scroll-down, reveal on scroll-up (only past the fold)
      if (!nav.classList.contains('menu-open')) {
        nav.classList.toggle('is-hidden', y > 420 && y > lastY + 6);
      }
      lastY = y;
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    if (toggle && links) {
      toggle.addEventListener('click', function () {
        var open = links.classList.toggle('is-open');
        toggle.classList.toggle('is-open', open);
        nav.classList.toggle('menu-open', open);
        nav.classList.remove('is-hidden');
        document.body.style.overflow = open ? 'hidden' : '';
        toggle.setAttribute('aria-expanded', String(open));
      });
      links.addEventListener('click', function (e) {
        if (e.target.closest('a')) {
          links.classList.remove('is-open');
          toggle.classList.remove('is-open');
          nav.classList.remove('menu-open');
          document.body.style.overflow = '';
        }
      });
    }
  }

  /* ------------------------------------------------------------------
     2. Scroll progress bar
     ------------------------------------------------------------------ */
  function initProgress() {
    var bar = $('#scrollbar');
    if (!bar) return;
    function tick() {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
    }
    window.addEventListener('scroll', tick, { passive: true });
    window.addEventListener('resize', tick);
    tick();
  }

  /* ------------------------------------------------------------------
     3. Scroll reveal + staggering
     ------------------------------------------------------------------ */
  function initReveal() {
    var els = $$('[data-reveal]');
    if (!els.length) return;
    if (reduceMotion || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    // auto-stagger siblings that share a parent
    var groups = {};
    els.forEach(function (el, i) {
      var p = el.parentNode;
      var key = p.__rvKey || (p.__rvKey = 'g' + i);
      groups[key] = groups[key] || 0;
      if (!el.style.getPropertyValue('--rd')) {
        el.style.setProperty('--rd', Math.min(groups[key] * 90, 540) + 'ms');
      }
      groups[key]++;
    });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('is-in');
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------------------
     4. Animated counters
     ------------------------------------------------------------------ */
  function initCounters() {
    var els = $$('[data-count]');
    if (!els.length) return;

    function run(el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var dur = parseInt(el.getAttribute('data-dur') || '1900', 10);
      var dec = parseInt(el.getAttribute('data-dec') || '0', 10);
      var pre = el.getAttribute('data-pre') || '';
      var suf = el.getAttribute('data-suf') || '';
      if (reduceMotion) {
        el.textContent = pre + target.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
        return;
      }
      var t0 = null;
      function step(ts) {
        if (t0 === null) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        var v = target * eased;
        el.textContent = pre + v.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }

    if (!('IntersectionObserver' in window)) { els.forEach(run); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { run(en.target); io.unobserve(en.target); }
      });
    }, { threshold: 0.4 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------------------
     5. Hero slider (image + <video> ready)
     ------------------------------------------------------------------ */
  function initHero() {
    var hero = $('#hero');
    if (!hero) return;
    var slides = $$('.hero__slide', hero);
    if (slides.length < 1) return;

    var h1 = $('#heroTitle');
    var sub = $('#heroSub');
    var dotWrap = $('#heroDots');
    var i = 0, timer = null;

    hero.style.setProperty('--hero-dur', CFG.heroInterval + 'ms');

    var dots = slides.map(function (s, n) {
      var b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', 'Go to slide ' + (n + 1));
      b.addEventListener('click', function () { go(n); });
      if (dotWrap) dotWrap.appendChild(b);
      return b;
    });

    function paint() {
      slides.forEach(function (s, n) {
        s.classList.toggle('is-active', n === i);
        var v = s.querySelector('video');
        if (v) { if (n === i) { v.play().catch(function () {}); } else { v.pause(); } }
      });
      dots.forEach(function (d, n) {
        d.classList.remove('is-active');
        if (n === i) { void d.offsetWidth; d.classList.add('is-active'); }
      });
      var s = slides[i];
      if (h1 && s.dataset.h1) {
        h1.innerHTML = s.dataset.h1;
        h1.style.animation = 'none'; void h1.offsetWidth;
        h1.style.animation = 'msgIn .8s var(--ease-out) both';
      }
      if (sub && s.dataset.sub) {
        sub.textContent = s.dataset.sub;
        sub.style.animation = 'none'; void sub.offsetWidth;
        sub.style.animation = 'msgIn .8s .1s var(--ease-out) both';
      }
    }

    function go(n) { i = (n + slides.length) % slides.length; paint(); restart(); }
    function next() { go(i + 1); }
    function prev() { go(i - 1); }
    function restart() {
      clearInterval(timer);
      if (slides.length > 1 && !reduceMotion) timer = setInterval(next, CFG.heroInterval);
    }

    var nx = $('#heroNext'), pv = $('#heroPrev');
    if (nx) nx.addEventListener('click', next);
    if (pv) pv.addEventListener('click', prev);

    // swipe
    var x0 = null;
    hero.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    hero.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 55) { dx < 0 ? next() : prev(); }
      x0 = null;
    }, { passive: true });

    document.addEventListener('visibilitychange', function () {
      document.hidden ? clearInterval(timer) : restart();
    });

    paint();
    restart();
  }

  /* ------------------------------------------------------------------
     6. Accordions (FAQ) — height-animated, a11y-correct
     ------------------------------------------------------------------ */
  function initAccordions() {
    $$('.faq').forEach(function (faq) {
      var single = faq.hasAttribute('data-single');
      $$('.faq__q', faq).forEach(function (btn) {
        var panel = btn.nextElementSibling;
        if (!panel) return;
        var open = btn.getAttribute('aria-expanded') === 'true';
        if (open) panel.style.height = 'auto';

        btn.addEventListener('click', function () {
          var isOpen = btn.getAttribute('aria-expanded') === 'true';
          if (single && !isOpen) {
            $$('.faq__q[aria-expanded="true"]', faq).forEach(function (o) {
              o.setAttribute('aria-expanded', 'false');
              var op = o.nextElementSibling;
              op.style.height = op.scrollHeight + 'px';
              requestAnimationFrame(function () { op.style.height = '0px'; });
            });
          }
          btn.setAttribute('aria-expanded', String(!isOpen));
          if (isOpen) {
            panel.style.height = panel.scrollHeight + 'px';
            requestAnimationFrame(function () { panel.style.height = '0px'; });
          } else {
            panel.style.height = panel.scrollHeight + 'px';
            panel.addEventListener('transitionend', function te(e) {
              if (e.propertyName !== 'height') return;
              panel.style.height = 'auto';
              panel.removeEventListener('transitionend', te);
            });
          }
        });
      });
    });
  }

  /* ------------------------------------------------------------------
     7. Filters (projects / case studies)
     ------------------------------------------------------------------ */
  function initFilters() {
    $$('[data-filters]').forEach(function (bar) {
      var targetSel = bar.getAttribute('data-filters');
      var items = $$(targetSel + ' [data-cat]');
      var empty = $(bar.getAttribute('data-empty') || '#noResults');

      $$('.filter', bar).forEach(function (btn) {
        btn.addEventListener('click', function () {
          var cat = btn.getAttribute('data-filter');
          $$('.filter', bar).forEach(function (b) { b.classList.toggle('is-active', b === btn); });
          var shown = 0;
          items.forEach(function (it) {
            var match = cat === 'all' || it.getAttribute('data-cat') === cat;
            it.hidden = !match;
            if (match) {
              shown++;
              it.style.animation = 'none'; void it.offsetWidth;
              it.style.animation = 'msgIn .5s var(--ease-out) both';
            }
          });
          if (empty) empty.hidden = shown > 0;
          if (history.replaceState) {
            history.replaceState(null, '', cat === 'all' ? location.pathname : '?c=' + cat);
          }
        });
      });

      // deep link: ?c=residential
      var pre = new URLSearchParams(location.search).get('c');
      if (pre) {
        var b = $('.filter[data-filter="' + CSS.escape(pre) + '"]', bar);
        if (b) b.click();
      }
    });
  }

  /* ------------------------------------------------------------------
     8. Tabs (pricing charts)
     ------------------------------------------------------------------ */
  function initTabs() {
    $$('[data-tabs]').forEach(function (bar) {
      var panels = $$(bar.getAttribute('data-tabs') + ' .tabpanel');
      $$('.tab', bar).forEach(function (btn) {
        btn.addEventListener('click', function () {
          var id = btn.getAttribute('data-tab');
          $$('.tab', bar).forEach(function (b) {
            var on = b === btn;
            b.classList.toggle('is-active', on);
            b.setAttribute('aria-selected', String(on));
          });
          panels.forEach(function (p) { p.hidden = p.id !== id; });
        });
      });
    });
  }

  /* ------------------------------------------------------------------
     9. Spotlight + tilt micro-interactions
     ------------------------------------------------------------------ */
  function initPointerFx() {
    if (reduceMotion || window.matchMedia('(hover: none)').matches) return;

    $$('.spotlight').forEach(function (el) {
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        el.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        el.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });

    $$('.tilt').forEach(function (el) {
      var max = parseFloat(el.getAttribute('data-tilt') || '7');
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = 'perspective(900px) rotateX(' + (-py * max) + 'deg) rotateY(' + (px * max) + 'deg)';
      });
      el.addEventListener('pointerleave', function () { el.style.transform = ''; });
    });
  }

  /* ------------------------------------------------------------------
     10. Marquee — duplicate track for a seamless loop
     ------------------------------------------------------------------ */
  function initMarquee() {
    $$('.marquee__track').forEach(function (track) {
      if (track.dataset.cloned) return;
      track.dataset.cloned = '1';
      track.innerHTML += track.innerHTML;
    });
  }

  /* ------------------------------------------------------------------
     11. WhatsApp chat widget — injected on every page
     ------------------------------------------------------------------ */
  var ICON = {
    wa: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.53.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.6-.92-2.2-.24-.58-.48-.5-.67-.5h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.22 3.08c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.23 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35M12.05 21.8h-.02c-1.74 0-3.45-.47-4.94-1.35l-.35-.21-3.67.96.98-3.58-.23-.37a9.79 9.79 0 0 1-1.5-5.22c0-5.4 4.4-9.8 9.81-9.8 2.62 0 5.08 1.02 6.93 2.88a9.73 9.73 0 0 1 2.87 6.93c0 5.41-4.4 9.81-9.8 9.81M20.52 3.45A11.7 11.7 0 0 0 12.05 0C5.6 0 .35 5.25.34 11.7c0 2.06.54 4.08 1.56 5.86L.24 24l6.6-1.73a11.7 11.7 0 0 0 5.2 1.33h.01c6.45 0 11.7-5.25 11.7-11.7 0-3.13-1.21-6.07-3.43-8.28"/></svg>',
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
    arrow: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
  };

  function initWhatsApp() {
    if ($('.wa')) return;
    var now = new Date();
    var time = now.getHours().toString().padStart(2, '0') + ':' + now.getMinutes().toString().padStart(2, '0');

    var quick = [
      ['I want a price for my home', 'Hello Solar World, please send me pricing for a home solar and inverter system.'],
      ['I want a price for my business', 'Hello Solar World, I need a solar system for my business. Please send pricing and options.'],
      ['What size system do I need?', 'Hello Solar World, I would like help sizing a solar system for my property. Here are my appliances:'],
      ['Tell me about financing', 'Hello Solar World, I would like to know more about your 30% deposit financing plan.']
    ];

    var el = document.createElement('div');
    el.className = 'wa';
    el.innerHTML =
      '<div class="wa__panel" role="dialog" aria-label="Chat with Solar World on WhatsApp">' +
        '<div class="wa__head">' +
          '<span class="av">' + ICON.wa + '</span>' +
          '<span><b>Solar World Electric</b><small><i></i>Typically replies in minutes</small></span>' +
          '<button class="wa__close" type="button" aria-label="Close chat">' + ICON.close + '</button>' +
        '</div>' +
        '<div class="wa__body">' +
          '<div class="wa__msg">👋 Hi there! Welcome to <b>Solar World Electric Technology Ltd.</b><span class="wa__time">' + time + '</span></div>' +
          '<div class="wa__msg">We have powered over <b>60,000 homes, offices, hotels, businesses and communities</b> across Nigeria since 2015.<span class="wa__time">' + time + '</span></div>' +
          '<div class="wa__msg">Tell us what you want to power and we will size it, price it and install it — usually within 48 hours of payment. How can we help?<span class="wa__time">' + time + '</span></div>' +
        '</div>' +
        '<div class="wa__quick"><p>Quick questions</p>' +
          quick.map(function (q) {
            return '<a href="' + wa(q[1]) + '" target="_blank" rel="noopener">' + q[0] + ICON.arrow + '</a>';
          }).join('') +
        '</div>' +
        '<div class="wa__foot"><a class="btn btn--green" href="' + wa() + '" target="_blank" rel="noopener">' + ICON.wa + ' Start WhatsApp chat</a></div>' +
      '</div>' +
      '<button class="wa__fab" type="button" aria-expanded="false" aria-label="Chat with us on WhatsApp">' +
        '<span class="wa__avatar">' + ICON.wa + '</span>' +
        '<span class="wa__label"><b>Chat with us</b><span><i></i>We are online</span></span>' +
        '<span class="wa__badge">1</span>' +
      '</button>';

    document.body.appendChild(el);

    var fab = $('.wa__fab', el);
    fab.addEventListener('click', function () {
      var open = el.classList.toggle('is-open');
      fab.setAttribute('aria-expanded', String(open));
      if (open) store.set('swe_wa_seen', '1');
    });
    $('.wa__close', el).addEventListener('click', function () {
      el.classList.remove('is-open');
      fab.setAttribute('aria-expanded', 'false');
    });
    document.addEventListener('click', function (e) {
      if (!el.contains(e.target)) { el.classList.remove('is-open'); fab.setAttribute('aria-expanded', 'false'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { el.classList.remove('is-open'); fab.setAttribute('aria-expanded', 'false'); }
    });

    if (store.get('swe_wa_seen')) $('.wa__badge', el).style.display = 'none';
  }

  /* ------------------------------------------------------------------
     12. Lead-capture popup — fires 30s after landing, on every page
     ------------------------------------------------------------------ */
  function initLeadPopup() {
    if ($('.leadpop')) return;

    var snooze = parseInt(store.get('swe_lead_snooze') || '0', 10);
    var done = store.get('swe_lead_done');
    if (done || (snooze && Date.now() < snooze)) return;

    var el = document.createElement('div');
    el.className = 'leadpop';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-modal', 'true');
    el.setAttribute('aria-label', 'Get a free solar consultation');
    el.hidden = false;
    el.innerHTML =
      '<div class="leadpop__scrim"></div>' +
      '<div class="leadpop__box">' +
        '<button class="leadpop__close" type="button" aria-label="Close">' + ICON.close + '</button>' +
        '<aside class="leadpop__aside">' +
          '<h3>Get a free solar plan for your property</h3>' +
          '<p>Tell us what you want to power. Our engineers will size the system and send you a costed proposal — no obligation.</p>' +
          '<ul>' +
            '<li>' + ICON.check + '<span>Free load assessment &amp; system sizing</span></li>' +
            '<li>' + ICON.check + '<span>Transparent pricing, no hidden charges</span></li>' +
            '<li>' + ICON.check + '<span>Financing from 30% deposit</span></li>' +
            '<li>' + ICON.check + '<span>Installation typically within 48 hours</span></li>' +
          '</ul>' +
        '</aside>' +
        '<div class="leadpop__main">' +
          '<form class="leadpop__form" novalidate>' +
            '<h4>Tell us what you want to achieve</h4>' +
            '<p class="small muted" style="margin-bottom:18px">Takes 30 seconds. We reply the same working day.</p>' +
            '<div class="field-row">' +
              '<div class="field"><label for="ld-name">Full name <span class="req">*</span></label><input id="ld-name" name="name" required autocomplete="name" placeholder="Your name"></div>' +
              '<div class="field"><label for="ld-phone">Phone / WhatsApp <span class="req">*</span></label><input id="ld-phone" name="phone" required type="tel" autocomplete="tel" placeholder="0803 000 0000"></div>' +
            '</div>' +
            '<div class="field"><label for="ld-email">Email</label><input id="ld-email" name="email" type="email" autocomplete="email" placeholder="you@example.com"></div>' +
            '<div class="field-row">' +
              '<div class="field"><label for="ld-type">Property type</label><select id="ld-type" name="property">' +
                '<option>Home / apartment</option><option>Duplex / estate</option><option>Office</option>' +
                '<option>Hotel / short-stay</option><option>School</option><option>Hospital / clinic</option>' +
                '<option>Shop / retail / restaurant</option><option>Factory / industrial</option>' +
                '<option>Community / street lighting</option><option>Other</option>' +
              '</select></div>' +
              '<div class="field"><label for="ld-city">City / state</label><input id="ld-city" name="city" placeholder="e.g. Port Harcourt"></div>' +
            '</div>' +
            '<div class="field"><label for="ld-goal">What do you want to achieve? <span class="req">*</span></label>' +
              '<textarea id="ld-goal" name="goal" required placeholder="e.g. I want to run 3 ACs, a fridge, freezer, TVs and lights 24/7 without a generator."></textarea></div>' +
            '<div class="field"><label for="ld-budget">Budget range (optional)</label><select id="ld-budget" name="budget">' +
              '<option value="">Not sure yet</option><option>Under ₦3m</option><option>₦3m – ₦6m</option>' +
              '<option>₦6m – ₦12m</option><option>₦12m – ₦30m</option><option>Above ₦30m</option>' +
            '</select></div>' +
            '<button class="btn btn--primary btn--block btn--lg" type="submit">Send my details on WhatsApp' + ICON.arrow + '</button>' +
            '<p class="form-note">By sending, your details open in WhatsApp addressed to our team on ' + CFG.phoneDisplay + '. We never share your information.</p>' +
          '</form>' +
          '<div class="leadpop__ok">' +
            '<div class="tick">' + ICON.check + '</div>' +
            '<h4>Thank you — your details are on the way.</h4>' +
            '<p class="muted">WhatsApp should have opened with your message. If it did not, tap the button below and our team will pick it up straight away.</p>' +
            '<a class="btn btn--green btn--lg" href="' + wa() + '" target="_blank" rel="noopener">' + ICON.wa + ' Open WhatsApp</a>' +
          '</div>' +
        '</div>' +
      '</div>';

    document.body.appendChild(el);

    function close(snoozeIt) {
      el.classList.remove('is-open');
      document.body.style.overflow = '';
      if (snoozeIt) store.set('swe_lead_snooze', String(Date.now() + CFG.popupCooldownDays * 864e5));
    }
    function open() {
      if (document.body.classList.contains('leadpop-suppressed')) return;
      el.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      var f = $('#ld-name', el); if (f) setTimeout(function () { f.focus(); }, 420);
    }

    $('.leadpop__close', el).addEventListener('click', function () { close(true); });
    $('.leadpop__scrim', el).addEventListener('click', function () { close(true); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && el.classList.contains('is-open')) close(true);
    });

    $('.leadpop__form', el).addEventListener('submit', function (e) {
      e.preventDefault();
      var f = e.target;
      var bad = false;
      ['name', 'phone', 'goal'].forEach(function (n) {
        var input = f.elements[n];
        if (!input.value.trim()) { input.style.borderColor = '#E5484D'; bad = true; }
        else { input.style.borderColor = ''; }
      });
      if (bad) return;

      var v = function (n) { return (f.elements[n] && f.elements[n].value.trim()) || '—'; };
      var msg =
        'Hello Solar World, I would like a solar consultation.\n\n' +
        'Name: ' + v('name') + '\n' +
        'Phone: ' + v('phone') + '\n' +
        'Email: ' + v('email') + '\n' +
        'Property: ' + v('property') + '\n' +
        'Location: ' + v('city') + '\n' +
        'Budget: ' + v('budget') + '\n\n' +
        'What I want to achieve:\n' + v('goal') + '\n\n' +
        '(Sent from solarworldelectric.com)';

      window.open(wa(msg), '_blank', 'noopener');
      store.set('swe_lead_done', '1');
      el.classList.add('is-done');
      document.dispatchEvent(new CustomEvent('swe:lead', { detail: { source: 'popup' } }));
    });

    // Fire after the configured delay, or on strong exit intent — whichever first.
    var fired = false;
    var t = setTimeout(function () { if (!fired) { fired = true; open(); } }, CFG.popupDelay);
    document.addEventListener('mouseout', function (e) {
      if (fired || e.clientY > 8 || e.relatedTarget) return;
      if (performance.now() < 8000) return; // don't ambush an immediate bounce
      fired = true; clearTimeout(t); open();
    });
  }

  /* ------------------------------------------------------------------
     13. Any inline form that should route to WhatsApp
     ------------------------------------------------------------------ */
  function initWaForms() {
    $$('form[data-wa-form]').forEach(function (f) {
      f.addEventListener('submit', function (e) {
        e.preventDefault();
        var lines = ['Hello Solar World, I am making an enquiry from your website.', ''];
        $$('input, select, textarea', f).forEach(function (input) {
          if (!input.name || input.type === 'submit') return;
          var label = f.querySelector('label[for="' + input.id + '"]');
          var key = (label ? label.textContent : input.name).replace('*', '').trim();
          if (input.value.trim()) lines.push(key + ': ' + input.value.trim());
        });
        lines.push('', '(Sent from solarworldelectric.com)');
        window.open(wa(lines.join('\n')), '_blank', 'noopener');
        var ok = f.querySelector('[data-wa-ok]');
        if (ok) { ok.hidden = false; f.reset(); }
      });
    });
  }

  /* ------------------------------------------------------------------
     14. Prefill WhatsApp links declared in markup
     ------------------------------------------------------------------ */
  function initWaLinks() {
    $$('[data-wa]').forEach(function (a) {
      a.href = wa(a.getAttribute('data-wa') || '');
      a.target = '_blank';
      a.rel = 'noopener';
    });
  }

  /* ------------------------------------------------------------------
     Boot
     ------------------------------------------------------------------ */
  function boot() {
    initNav();
    initProgress();
    initReveal();
    initCounters();
    initHero();
    initAccordions();
    initFilters();
    initTabs();
    initPointerFx();
    initMarquee();
    initWaLinks();
    initWaForms();
    initWhatsApp();
    initLeadPopup();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  window.SWE = { wa: wa, config: CFG };
})();
