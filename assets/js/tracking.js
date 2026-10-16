/* Solar World Electric: Google Ads conversion tracking.
 *
 * Fill in GOOGLE_ADS_ID and the labels below (Google Ads > Goals > Conversions > the
 * conversion action > Tag setup > "Use Google Tag Manager"/"Install the tag yourself").
 * Until GOOGLE_ADS_ID is set, nothing is sent to Google; events are only pushed to dataLayer.
 * A conversion whose label is empty is not reported to Google Ads, so you can add them one by one.
 */
(function () {
  'use strict';

  var GOOGLE_ADS_ID = 'AW-17136017888';       // the Google tag itself is inlined in every page's <head>
  var LABELS = {
    // Primary conversions: a real person reaching us.
    whatsapp_click:  'KhJaCM_wsJ8dEODDi-s_',   // any WhatsApp button/link, chat widget or calculator "send to engineer"
    phone_click:     '',   // any tap on a phone number (click-to-call)
    lead_form:       '',   // consultation popup, contact form, financing application sent
    ai_chat_lead:    '',   // visitor sent a message to the NETICS AI assistant
    // Secondary / observation conversions: interest, not contact.
    email_click:     '',
    calculator_use:  ''
  };

  var live = /^AW-\d+$/.test(GOOGLE_ADS_ID);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  var once = {};
  var lastLead = 0;

  function track(name, params, oncePerPage) {
    if (oncePerPage) { if (once[name]) return; once[name] = 1; }
    params = params || {};
    params.page_path = location.pathname;
    gtag('event', name, params);                      // GA4 / dataLayer
    if (live && LABELS[name]) {
      gtag('event', 'conversion', {
        send_to: GOOGLE_ADS_ID + '/' + LABELS[name],
        value: 1.0, currency: 'NGN',
        event_callback: function () {}
      });
    }
    if (window.console && location.search.indexOf('trackdebug') > -1) console.log('[track]', name, params);
  }
  window.sweTrack = track;

  function where(el) {
    if (!el || !el.closest) return 'page';
    if (el.closest('.wa')) return 'whatsapp_widget';
    if (el.closest('.leadpop')) return 'consultation_popup';
    if (el.closest('#smartCalc, #sizer, .package-result, .package-send')) return 'calculator';
    if (el.closest('#repay, [id^="rp"]')) return 'finance_calculator';
    if (el.closest('.hero')) return 'hero';
    if (el.closest('.promo')) return 'promo';
    if (el.closest('footer')) return 'footer';
    if (el.closest('header, .nav, .topbar')) return 'header';
    return 'page_body';
  }

  /* Clicks on WhatsApp, phone and email links (works for links added later too). */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    if (/^https?:\/\/(wa\.me|api\.whatsapp\.com|wa\.link)\b/i.test(h)) {
      // A form that already reported a lead and then offers "Open WhatsApp" is the same person.
      if (Date.now() - lastLead < 15000) return;
      track('whatsapp_click', { location: where(a) });
    } else if (/^tel:/i.test(h)) {
      track('phone_click', { location: where(a), number: h.slice(4) });
    } else if (/^mailto:/i.test(h)) {
      track('email_click', { location: where(a) });
    }
  }, true);

  /* Lead forms (the site dispatches swe:lead after a successful submit). */
  document.addEventListener('swe:lead', function (e) {
    lastLead = Date.now();
    track('lead_form', { location: (e.detail && e.detail.source) || 'form' });
  });

  /* Calculators: first real interaction on the page. */
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (t.closest && t.closest('#smartCalc .stepper__btn, #sizer button[data-k], #smartCalc select, #repay')) {
      track('calculator_use', { location: where(t) }, true);
    }
  });
  document.addEventListener('change', function (e) {
    if (e.target.closest && e.target.closest('#smartCalc, #sizer')) track('calculator_use', { location: 'calculator' }, true);
  });

  /* NETICS AI assistant (events bubble out of its shadow DOM, composed). */
  document.addEventListener('netics-open', function () { track('ai_chat_open', {}, true); });
  ['netics-message', 'netics-voice-start', 'netics-handoff'].forEach(function (ev) {
    document.addEventListener(ev, function () { track('ai_chat_lead', { event: ev }, true); });
  });
})();
