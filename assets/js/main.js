/* ============================================================
   Solar World Electric — interactions
   ============================================================ */
(function () {
  'use strict';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const naira = n => '₦' + Math.round(n).toLocaleString('en-NG');

  /* ---------- Navbar ---------- */
  const nav = $('.nav');
  const onScroll = () => nav && nav.classList.toggle('scrolled', window.scrollY > 24);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const toggle = $('.nav__toggle');
  const links = $('.nav__links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      toggle.classList.toggle('open');
      links.classList.toggle('open');
    });
    $$('.nav__links a').forEach(a => a.addEventListener('click', () => {
      toggle.classList.remove('open'); links.classList.remove('open');
    }));
  }

  /* ---------- Hero slider ---------- */
  const heroSlider = $('#heroSlider');
  if (heroSlider) {
    const slides = $$('.hero__slide', heroSlider);
    const textEl = $('.hero__text', heroSlider);
    const dotsWrap = $('#heroDots');
    let idx = 0;
    slides.forEach((s, i) => {
      const b = document.createElement('button');
      b.innerHTML = '<i></i>';
      b.setAttribute('aria-label', 'Go to slide ' + (i + 1));
      b.addEventListener('click', () => show(i));
      dotsWrap.appendChild(b);
    });
    const dots = $$('button', dotsWrap);
    const bars = $$('i', dotsWrap);
    function show(n) {
      idx = (n + slides.length) % slides.length;
      slides.forEach((s, i) => s.classList.toggle('is-active', i === idx));
      dots.forEach((d, i) => d.classList.toggle('is-active', i === idx));
      const s = slides[idx];
      textEl.innerHTML = '<h1>' + s.dataset.h1 + '</h1><p class="sub">' + s.dataset.sub + '</p>';
    }
    // advance exactly when the active progress bar fills — keeps everything in lock-step
    bars.forEach(bar => bar.addEventListener('animationend', () => {
      if (bar.parentElement.classList.contains('is-active')) show(idx + 1);
    }));
    const next = $('#heroNext'), prev = $('#heroPrev');
    next && next.addEventListener('click', () => show(idx + 1));
    prev && prev.addEventListener('click', () => show(idx - 1));
    heroSlider.addEventListener('mouseenter', () => heroSlider.classList.add('is-paused'));
    heroSlider.addEventListener('mouseleave', () => heroSlider.classList.remove('is-paused'));
    show(0);
  }

  /* ---------- Scroll reveal ---------- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  $$('[data-reveal]').forEach(el => io.observe(el));

  /* ---------- Animated counters ---------- */
  const animate = (el) => {
    const target = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const dec = (el.dataset.dec | 0);
    const dur = 1600; const t0 = performance.now();
    const step = (t) => {
      const p = Math.min((t - t0) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      const val = target * eased;
      el.textContent = val.toLocaleString('en-NG', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const cio = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { animate(e.target); cio.unobserve(e.target); } });
  }, { threshold: 0.5 });
  $$('[data-count]').forEach(el => cio.observe(el));

  /* ---------- Range live value ---------- */
  $$('input[type=range][data-out]').forEach(r => {
    const out = $('#' + r.dataset.out);
    const fmt = r.dataset.fmt;
    const upd = () => {
      let v = +r.value;
      out.textContent = fmt === 'kva' ? v + ' kVA' : fmt === 'naira' ? naira(v) : v;
    };
    r.addEventListener('input', () => { upd(); if (r.dataset.calc) window.runSavings && window.runSavings(); });
    upd();
  });

  /* ---------- Savings calculator ---------- */
  const sForm = $('#savings');
  if (sForm) {
    const out = {
      monthly: $('#r-monthly'), annual: $('#r-annual'), five: $('#r-five'),
      carbon: $('#r-carbon'), roi: $('#r-roi')
    };
    const bars = { gen: $('#bar-gen'), solar: $('#bar-solar') };
    window.runSavings = function () {
      const bill = +$('#in-bill').value || 0;
      const fuel = +$('#in-fuel').value || 0;
      const type = $('#in-type').value;
      const size = +$('#in-size').value || 5;
      // Current monthly energy spend (grid + generator fuel)
      const current = bill + fuel;
      // Solar offsets ~85-92% of spend depending on system adequacy
      const offset = type === 'industrial' ? 0.82 : type === 'commercial' ? 0.88 : 0.9;
      const monthlySave = current * offset;
      const annual = monthlySave * 12;
      const five = annual * 5;
      // Carbon: ~0.45 kg CO2 per kWh diesel; estimate kWh from size
      const kwhMonth = size * 4 * 30; // kVA * sun-hours * days (rough usable)
      const carbon = (kwhMonth * 0.45 * 12) / 1000; // tonnes/yr
      // ROI months: system cost ~ size * 950k, payback = cost / monthlySave
      const sysCost = size * 950000;
      const roiMonths = monthlySave > 0 ? sysCost / monthlySave : 0;
      out.monthly.textContent = naira(monthlySave);
      out.annual.textContent = naira(annual);
      out.five.textContent = naira(five);
      out.carbon.textContent = carbon.toFixed(1) + ' t';
      out.roi.textContent = (roiMonths / 12).toFixed(1) + ' yrs';
      // bars
      const max = Math.max(current, monthlySave, 1);
      bars.gen.style.height = (current / max * 100) + '%';
      bars.solar.style.height = (Math.max(current - monthlySave, current * 0.1) / max * 100) + '%';
    };
    sForm.addEventListener('input', window.runSavings);
    window.runSavings();
  }

  /* ---------- Smart sizing calculator ---------- */
  const szForm = $('#sizer');
  if (szForm) {
    const APPL = { ac: 1500, fridge: 200, tv: 120, pc: 150, pump: 750, light: 15, freezer: 300 };
    const out = {
      load: $('#sz-load'), sys: $('#sz-sys'), batt: $('#sz-batt'),
      panels: $('#sz-panels'), cost: $('#sz-cost'), monthly: $('#sz-monthly')
    };
    window.runSizer = function () {
      let watts = 0;
      $$('[data-appl]').forEach(i => { watts += (APPL[i.dataset.appl] || 0) * (+i.value || 0); });
      watts += (+$('#sz-lights').value || 0) * APPL.light;
      const kva = Math.max(Math.ceil((watts * 1.3) / 1000 / 0.8), 1); // 30% headroom, 0.8 pf
      const backupHrs = +$('#sz-backup').value || 8;
      const wh = watts * backupHrs;
      const battKwh = Math.ceil((wh / 0.9) / 1000); // 90% DoD lithium
      const panels = Math.max(Math.ceil((kva * 1000) / 550), 4); // 550W panels
      const cost = kva * 950000 + battKwh * 320000;
      out.load.textContent = (watts / 1000).toFixed(1) + ' kW';
      out.sys.textContent = kva + ' kVA';
      out.batt.textContent = battKwh + ' kWh';
      out.panels.textContent = panels + ' panels';
      out.cost.textContent = '~' + naira(cost);
      out.monthly.textContent = naira(cost * 0.7 / 9); // 30% down, 9-month plan on 70%
    };
    szForm.addEventListener('input', window.runSizer);
    window.runSizer();
  }

  /* ---------- Financing calculator ---------- */
  const fForm = $('#financing');
  if (fForm) {
    window.runFinance = function () {
      const total = +$('#f-total').value || 0;
      const months = +$('#f-term').value || 6;
      const down = total * 0.30;
      const principal = total - down;
      const rate = 0.04; // 4% flat monthly per brochure note, simple split
      const interest = principal * rate * months / 12 * 0 + principal * 0.04; // 4% flat add-on
      const financed = principal + interest;
      const monthly = financed / months;
      $('#f-down').textContent = naira(down);
      $('#f-principal').textContent = naira(principal);
      $('#f-monthly').textContent = naira(monthly);
      $('#f-totalpay').textContent = naira(down + financed);
    };
    fForm.addEventListener('input', window.runFinance);
    window.runFinance();
  }

  /* ---------- Project filter ---------- */
  const filters = $$('.filter-btn');
  if (filters.length) {
    filters.forEach(b => b.addEventListener('click', () => {
      filters.forEach(x => x.classList.remove('active'));
      b.classList.add('active');
      const f = b.dataset.filter;
      $$('.gal__item').forEach(it => {
        it.classList.toggle('hide', f !== 'all' && it.dataset.cat !== f);
      });
    }));
  }

  /* ---------- FAQ accordion ---------- */
  $$('.faq__q').forEach(q => q.addEventListener('click', () => {
    const item = q.closest('.faq__item');
    const a = item.querySelector('.faq__a');
    const open = item.classList.toggle('open');
    a.style.maxHeight = open ? a.scrollHeight + 'px' : 0;
  }));

  /* ---------- Forms (demo) ---------- */
  $$('form[data-demo]').forEach(f => f.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = f.querySelector('[type=submit]');
    const old = btn.textContent;
    btn.textContent = 'Sent ✓'; btn.disabled = true;
    const note = f.querySelector('.form-note');
    if (note) note.textContent = "Thank you — our team will reach out within 24 hours.";
    setTimeout(() => { btn.textContent = old; btn.disabled = false; f.reset(); }, 3500);
  }));

  /* ---------- AI Assistant (scripted) ---------- */
  const chat = $('#chat'); const openBtn = $('#chatOpen'); const body = $('#chatBody');
  if (chat && openBtn) {
    openBtn.addEventListener('click', () => chat.classList.toggle('open'));
    const close = $('#chatClose'); close && close.addEventListener('click', () => chat.classList.remove('open'));
    const add = (text, who) => {
      const m = document.createElement('div');
      m.className = 'msg ' + who; m.innerHTML = text;
      body.appendChild(m); body.scrollTop = body.scrollHeight;
    };
    const KB = {
      pricing: "Our systems start around <b>₦7M for a 7.5kVA</b> residential setup. With financing you pay just <b>30% upfront</b> and spread the rest over 3–12 months. Try our <a href='calculator.html'>Smart Calculator</a> for a tailored estimate.",
      sizing: "Sizing depends on your appliances (ACs, fridges, pumps…). Our <a href='calculator.html'>Smart Solar Calculator</a> recommends the exact kVA, battery & panel count in seconds.",
      financing: "Yes! Pay 30% upfront, get approval in 24–48 hours, and choose 3, 6, 9 or 12-month repayment at a low 4% flat rate. <a href='financing.html'>See how it works →</a>",
      offices: "We have offices in <b>Abuja</b> (Jabi, Wuse 2, Gwarinpa), <b>Port Harcourt</b> (GRA Phase 2 & 3, City Mall) and <b>Lagos</b> (Lekki Phase 1, Circle Mall). <a href='contact.html'>Find the nearest →</a>",
      warranty: "Warranties: Solar Panels up to <b>20 years</b>, Lithium Batteries <b>5 years</b>, Inverters <b>2 years</b>, plus <b>1 year free after-sales support</b>.",
      book: "Great! Book a <b>free site inspection</b> on our <a href='contact.html'>Contact page</a> or chat on WhatsApp at <a href='https://wa.me/2349063315492'>0906 331 5492</a>.",
      default: "I can help with pricing, system sizing, financing, warranties and office locations. What would you like to know?"
    };
    window.chatAsk = function (key, label) {
      add(label || key, 'user');
      setTimeout(() => add(KB[key] || KB.default, 'bot'), 450);
    };
  }
})();
