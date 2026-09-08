# -*- coding: utf-8 -*-
"""Shared page shell: <head>, nav, footer, icons and structured data."""

import json
from data import COMPANY, OFFICES

SITE = COMPANY["canonical_domain"]

# ---------------------------------------------------------------------------
# ICONS
# ---------------------------------------------------------------------------
def _svg(body, stroke=True, box="0 0 24 24"):
    if stroke:
        return ('<svg viewBox="%s" fill="none" stroke="currentColor" stroke-width="1.8" '
                'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (box, body))
    return '<svg viewBox="%s" fill="currentColor" aria-hidden="true">%s</svg>' % (box, body)

ICONS = {
    "arrow":   _svg('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    "check":   _svg('<path d="M20 6 9 17l-5-5"/>'),
    "chevron": _svg('<path d="m9 18 6-6-6-6"/>'),
    "plus":    _svg('<path d="M12 5v14M5 12h14"/>'),
    "left":    _svg('<path d="m15 18-6-6 6-6"/>'),
    "right":   _svg('<path d="m9 18 6-6-6-6"/>'),
    "shield":  _svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>'),
    "pin":     _svg('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>'),
    "sliders": _svg('<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>'),
    "headset": _svg('<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>'),
    "wallet":  _svg('<path d="M19 7V5a2 2 0 0 0-2-2H5a2 2 0 0 0 0 4h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5"/><path d="M16 12h.01"/>'),
    "badge":   _svg('<circle cx="12" cy="8" r="6"/><path d="M15.5 13.5 17 22l-5-3-5 3 1.5-8.5"/>'),
    "sun":     _svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'),
    "bolt":    _svg('<path d="M13 2 3 14h8l-1 8 10-12h-8z"/>'),
    "battery": _svg('<rect x="2" y="7" width="16" height="10" rx="2"/><path d="M22 11v2M10 10l-2 4h4l-2 4"/>'),
    "home":    _svg('<path d="M3 10.5 12 3l9 7.5V21H3z"/><path d="M9 21v-6h6v6"/>'),
    "office":  _svg('<path d="M3 21h18M5 21V4h9v17M14 21V9h5v12"/><path d="M8 8h2M8 12h2M8 16h2"/>'),
    "factory": _svg('<path d="M2 21h20M4 21V9l6 4V9l6 4V5h4v16"/><path d="M8 17h2M14 17h2"/>'),
    "grid":    _svg('<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20z"/>'),
    "phone":   _svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'),
    "mail":    _svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>'),
    "clock":   _svg('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
    "star":    _svg('<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.9L12 17.8 5.8 21l1.2-6.9-5-4.9 6.9-1z"/>', stroke=False),
    "quote":   _svg('<path d="M7 11H4a1 1 0 0 1-1-1V7a4 4 0 0 1 4-4v2a2 2 0 0 0-2 2v1h2a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4v-2h3zM17 11h-3a1 1 0 0 1-1-1V7a4 4 0 0 1 4-4v2a2 2 0 0 0-2 2v1h2a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1h-3v-2h3z"/>', stroke=False),
    "play":    _svg('<path d="M8 5v14l11-7z"/>', stroke=False),
    "spark":   _svg('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>'),
    "wa":      _svg('<path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.53.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.6-.92-2.2-.24-.58-.48-.5-.67-.5h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.22 3.08c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.23 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35M12.05 21.8h-.02c-1.74 0-3.45-.47-4.94-1.35l-.35-.21-3.67.96.98-3.58-.23-.37a9.79 9.79 0 0 1-1.5-5.22c0-5.4 4.4-9.8 9.81-9.8 2.62 0 5.08 1.02 6.93 2.88a9.73 9.73 0 0 1 2.87 6.93c0 5.41-4.4 9.81-9.8 9.81M20.52 3.45A11.7 11.7 0 0 0 12.05 0C5.6 0 .35 5.25.34 11.7c0 2.06.54 4.08 1.56 5.86L.24 24l6.6-1.73a11.7 11.7 0 0 0 5.2 1.33h.01c6.45 0 11.7-5.25 11.7-11.7 0-3.13-1.21-6.07-3.43-8.28"/>', stroke=False),
    "fb":      _svg('<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>'),
    "ig":      _svg('<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>'),
    "in":      _svg('<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-11h4v1.5A6 6 0 0 1 16 8z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>'),
    "x":       _svg('<path d="M18 2h3l-7.5 8.6L22.5 22H16l-5-6.5L5.2 22H2l8-9.2L1.8 2H8.5l4.5 6z"/>', stroke=False),
    "tiktok":  _svg('<path d="M16 2h3a5 5 0 0 0 5 5v3a8 8 0 0 1-5-1.8V15a6.5 6.5 0 1 1-6.5-6.5c.3 0 .7 0 1 .1v3.2a3.3 3.3 0 1 0 2.5 3.2z"/>', stroke=False),
}

def ico(name, cls=""):
    s = ICONS.get(name, "")
    if cls and s:
        s = s.replace("<svg ", '<svg class="%s" ' % cls, 1)
    return s


# ---------------------------------------------------------------------------
# NAV
# ---------------------------------------------------------------------------
NAV_ITEMS = [
    ("index.html", "Home", None),
    ("about.html", "About", [
        ("about.html", "Our story", "Who we are, our vision and mission"),
        ("about.html#team", "Meet the team", "The people behind every installation"),
        ("reviews.html", "Customer reviews", "What customers say after installation"),
        ("contact.html#offices", "Our offices", "21 locations across three cities"),
    ]),
    ("solutions.html", "Solutions", [
        ("solutions.html#residential", "Residential", "Homes, estates, duplexes and apartments"),
        ("solutions.html#commercial", "Commercial", "Offices, hotels, schools and retail"),
        ("solutions.html#industrial", "Industrial", "Factories and processing facilities"),
        ("solutions.html#infrastructure", "Energy &amp; infrastructure", "Streetlights, pumping and EV charging"),
    ]),
    ("products.html", "Product Prices", [
        ("products.html", "All products", "Panels, inverters, batteries and more"),
        ("pricing.html", "Pricing &amp; packages", "Full Deye, Solis and standard charts"),
        ("financing.html", "Financing", "Pay 30% and spread the balance"),
    ]),
    ("projects.html", "Projects", [
        ("projects.html", "All case studies", "Every project, filterable by category"),
        ("projects.html?c=residential", "Residential projects", "Homes, estates and apartments"),
        ("projects.html?c=commercial", "Commercial projects", "Offices, hotels, schools, retail"),
        ("projects.html?c=industrial", "Industrial projects", "Factories and large-scale sites"),
        ("projects.html?c=infrastructure", "Infrastructure", "Streetlights, pumping, EV charging"),
    ]),
    ("calculator.html", "Calculators", [
        ("calculator.html", "Solar calculator",
         "Add your appliances, get the system size and cost"),
        ("financing.html#calculator", "Finance calculator",
         "Repayment estimator: deposit and monthly payment"),
        ("faq.html", "FAQ", "29 answers on cost, sizing and warranty"),
    ]),
    ("blog.html", "Blog", None),
    ("contact.html", "Contact", None),
]


def _submenu(items):
    rows = "".join(
        '<a href="%s"><span class="nav__sub-t">%s</span>'
        '<span class="nav__sub-d">%s</span></a>' % (h, t, d)
        for h, t, d in items
    )
    return '<div class="nav__sub"><div class="nav__sub-in">%s</div></div>' % rows


def nav(active, over_hero=False):
    links = ""
    for item in NAV_ITEMS:
        href, label, sub = item
        is_active = href.split("#")[0].split("?")[0] == active
        cls = " class=\"nav__item%s\"" % (" is-active" if is_active else "")
        if sub:
            links += (
                '<div%s>'
                '<a href="%s"%s>%s<svg class="nav__caret" viewBox="0 0 24 24" fill="none" '
                'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" '
                'stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></a>'
                '<button class="nav__subtoggle" type="button" aria-expanded="false" '
                'aria-label="Show %s submenu"></button>%s</div>'
                % (cls, href, ' aria-current="page"' if is_active else "", label,
                   label.replace("&amp;", "and"), _submenu(sub))
            )
        else:
            links += '<div%s><a href="%s"%s>%s</a></div>' % (
                cls, href, ' aria-current="page"' if is_active else "", label)

    return """
<a class="skip" href="#main">Skip to content</a>
<div class="scrollbar" id="scrollbar"></div>
<header class="nav%s" id="nav">
  <div class="nav__inner">
    <a class="brand" href="index.html" aria-label="Solar World Electric Technology Ltd, home">
      <img class="brand__mark" src="assets/img/logo-mark.svg" alt="" width="40" height="40">
      <span class="brand__txt">
        <span class="brand__name">Solar World</span>
        <span class="brand__sub">Electric Technology Ltd.</span>
      </span>
    </a>

    <nav class="nav__links" id="navLinks" aria-label="Main">
      <div class="nav__mhead">
        <span>Menu</span>
        <button class="nav__mclose" id="navClose" type="button" aria-label="Close menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"
               stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
        </button>
      </div>
      <div class="nav__list">%s</div>
      <div class="nav__mfoot">
        <a class="btn btn--primary btn--block" href="contact.html">Free consultation</a>
        <a class="btn btn--green btn--block" data-wa="">Chat on WhatsApp</a>
        <p>%s<br><a href="tel:%s">%s</a></p>
      </div>
    </nav>

    <a class="btn btn--primary nav__cta" href="contact.html">Free consultation</a>
    <button class="nav__toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<div class="nav__scrim" id="navScrim" hidden></div>""" % (
        " is-over" if over_hero else "", links,
        COMPANY["email"], COMPANY["phone"], COMPANY["phone_display"])


# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
def footer():
    regions = {}
    for o in OFFICES:
        regions.setdefault(o["region"], []).append(o)

    office_html = ""
    for region, items in regions.items():
        rows = "".join(
            '<p><b style="color:rgba(255,255,255,.8)">%s</b><br>%s%s</p>'
            % (o["name"], o["address"],
               ('<br><a href="tel:%s" style="color:var(--gold)">%s</a>'
                % (o["phone"].replace(" ", ""), o["phone"])) if o["phone"] else "")
            for o in items
        )
        office_html += '<div><h6>%s</h6>%s</div>' % (region, rows)

    quick = "".join('<a href="%s">%s</a>' % (h, t) for h, t in [
        ("solutions.html", "Solutions"), ("products.html", "Products"),
        ("pricing.html", "Pricing &amp; packages"), ("projects.html", "Projects &amp; case studies"),
        ("reviews.html", "Customer reviews"), ("financing.html", "Financing"),
        ("calculator.html", "Solar calculator"), ("faq.html", "FAQ"),
        ("about.html", "About us"), ("blog.html", "Knowledge centre"),
    ])

    segs = "".join('<a href="projects.html?c=%s">%s</a>' % (k, v) for k, v in [
        ("residential", "Residential solar"), ("commercial", "Commercial solar"),
        ("industrial", "Industrial solar"), ("infrastructure", "Streetlights &amp; infrastructure"),
    ]) + "".join('<a href="%s">%s</a>' % (h, t) for h, t in [
        ("solutions.html#infrastructure", "Solar water pumping"),
        ("products.html", "Inverters &amp; batteries"),
    ])

    return """
<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div>
        <div class="footer__brand">
          <img src="assets/img/logo-mark.svg" alt="" width="44" height="44">
          <span><b>Solar World</b><span>Electric Technology Ltd.</span></span>
        </div>
        <p>%(vision_short)s</p>
        <p class="small" style="color:rgba(255,255,255,.42)">RC %(rc)s · Established %(founded)s</p>
        <div class="footer__social">
          <a href="https://wa.me/%(wa)s" target="_blank" rel="noopener" aria-label="WhatsApp">%(wa_ico)s</a>
          <a href="https://www.facebook.com/solarworldelectric" target="_blank" rel="noopener" aria-label="Facebook">%(fb)s</a>
          <a href="https://www.instagram.com/solarworldelectric" target="_blank" rel="noopener" aria-label="Instagram">%(ig)s</a>
          <a href="https://www.linkedin.com/company/solar-world-electric-technology" target="_blank" rel="noopener" aria-label="LinkedIn">%(in)s</a>
          <a href="https://www.tiktok.com/@solarworldelectric" target="_blank" rel="noopener" aria-label="TikTok">%(tt)s</a>
        </div>
      </div>
      <div>
        <h5>Explore</h5>
        <nav class="footer__links" aria-label="Footer">%(quick)s</nav>
      </div>
      <div>
        <h5>What we power</h5>
        <nav class="footer__links" aria-label="Segments">%(segs)s</nav>
      </div>
      <div>
        <h5>Talk to us</h5>
        <div class="footer__contact">
          <a href="tel:%(phone)s">%(phone_ico)s<span>%(phone_display)s</span></a>
          <a href="mailto:%(email)s">%(mail_ico)s<span>%(email)s</span></a>
          <a data-wa="">%(wa_ico2)s<span>Chat on WhatsApp</span></a>
          <div>%(clock)s<span>Mon–Sat, 8:00am – 6:00pm<br>Emergency support 24/7</span></div>
        </div>
        <a class="btn btn--primary" style="margin-top:20px" href="contact.html">Book a free consultation</a>
      </div>
    </div>

    <div class="footer__offices">%(offices)s</div>

    <div class="footer__bottom">
      <p>© %(year)s %(name)s. All rights reserved. RC %(rc)s.</p>
      <nav>
        <a href="faq.html">FAQ</a>
        <a href="contact.html">Contact</a>
        <a href="sitemap.xml">Sitemap</a>
      </nav>
    </div>
  </div>
</footer>""" % {
        "vision_short": "Power you can always count on. Solar, inverter and battery systems designed, "
                        "installed and maintained for Nigerian homes, businesses and institutions since 2015.",
        "rc": COMPANY["rc"], "founded": COMPANY["founded"], "wa": COMPANY["wa_number"],
        "wa_ico": ico("wa"), "fb": ico("fb"), "ig": ico("ig"), "in": ico("in"), "tt": ico("tiktok"),
        "quick": quick, "segs": segs,
        "phone": COMPANY["phone"], "phone_display": COMPANY["phone_display"], "email": COMPANY["email"],
        "phone_ico": ico("phone"), "mail_ico": ico("mail"), "wa_ico2": ico("wa"), "clock": ico("clock"),
        "offices": office_html, "year": 2026, "name": COMPANY["name"],
    }


# ---------------------------------------------------------------------------
# STRUCTURED DATA
# ---------------------------------------------------------------------------
def org_schema():
    return {
        "@type": "Organization",
        "@id": SITE + "/#organization",
        "name": COMPANY["name"],
        "alternateName": ["Solar World Electric", "Solar World Nigeria"],
        "legalName": COMPANY["legal"],
        "url": SITE + "/",
        "logo": SITE + "/assets/img/logo-mark.svg",
        "foundingDate": COMPANY["founded"],
        "description": ("Nigerian solar energy company specialising in the sales, installation and maintenance "
                        "of solar power, hybrid inverter and lithium battery systems for residential, commercial, "
                        "industrial and government customers. Over 60,000 homes, offices, hotels, businesses and "
                        "communities powered since 2015."),
        "identifier": {"@type": "PropertyValue", "name": "RC Number", "value": COMPANY["rc"]},
        "areaServed": {"@type": "Country", "name": "Nigeria"},
        "telephone": COMPANY["phone"],
        "email": COMPANY["email"],
        "sameAs": [
            "https://www.facebook.com/solarworldelectric",
            "https://www.instagram.com/solarworldelectric",
            "https://www.linkedin.com/company/solar-world-electric-technology",
            "https://www.tiktok.com/@solarworldelectric",
        ],
        "knowsAbout": [
            "Solar power systems", "Hybrid solar inverters", "Lithium battery energy storage",
            "Solar panel installation", "Solar street lighting", "Solar water pumping",
            "EV charging infrastructure", "Renewable energy in Nigeria",
        ],
    }


def local_business_schema():
    locs = []
    for i, o in enumerate(OFFICES):
        locs.append({
            "@type": "LocalBusiness",
            "@id": SITE + "/#office-%d" % i,
            "parentOrganization": {"@id": SITE + "/#organization"},
            "name": "%s, %s, %s" % (COMPANY["short"], o["name"], o["region"]),
            "image": SITE + "/assets/img/store-front-1.jpg",
            "telephone": o["phone"],
            "priceRange": "₦₦₦",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": o["address"],
                "addressLocality": o["region"],
                "addressCountry": "NG",
            },
            "openingHoursSpecification": [{
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                "opens": "08:00", "closes": "18:00",
            }],
        })
    return locs


def website_schema():
    return {
        "@type": "WebSite",
        "@id": SITE + "/#website",
        "url": SITE + "/",
        "name": COMPANY["name"],
        "publisher": {"@id": SITE + "/#organization"},
        "inLanguage": "en-NG",
    }


def breadcrumbs(items):
    """items: [(name, url_or_None), ...]"""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             **({"item": SITE + "/" + u} if u else {})}
            for i, (n, u) in enumerate(items)
        ],
    }


def jsonld(*graphs):
    flat = []
    for g in graphs:
        if g is None:
            continue
        flat.extend(g if isinstance(g, list) else [g])
    doc = {"@context": "https://schema.org", "@graph": flat}
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(doc, ensure_ascii=False, separators=(",", ":")))


# ---------------------------------------------------------------------------
# PAGE SHELL
# ---------------------------------------------------------------------------
FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Inter:wght@400;500;600;700&"
         "family=Sora:wght@500;600;700;800&"
         "family=Space+Grotesk:wght@500;600;700&display=swap")


def page(*, slug, title, description, body, active=None, over_hero=True,
         schema=None, og_image="assets/img/hero-drone-city.jpg", extra_head=""):
    canonical = SITE + "/" + ("" if slug == "index.html" else slug)
    schema_html = jsonld(website_schema(), org_schema(), schema) if schema is not None else \
                  jsonld(website_schema(), org_schema())

    return """<!DOCTYPE html>
<html lang="en-NG">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(canonical)s">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="%(name)s">
<meta name="geo.region" content="NG">
<meta name="theme-color" content="#05070F">

<meta property="og:type" content="website">
<meta property="og:site_name" content="%(name)s">
<meta property="og:locale" content="en_NG">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canonical)s">
<meta property="og:image" content="%(site)s/%(og)s">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="%(site)s/%(og)s">

<link rel="icon" href="assets/img/logo-mark.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/logo-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="%(fonts)s">
<link rel="stylesheet" href="%(fonts)s">
<link rel="stylesheet" href="assets/css/styles.css">
%(schema)s
%(extra)s
</head>
<body>
%(nav)s
<main id="main">
%(body)s
</main>
%(footer)s
<script src="assets/js/main.js" defer></script>
</body>
</html>
""" % {
        "title": title, "desc": description, "canonical": canonical, "name": COMPANY["name"],
        "site": SITE, "og": og_image, "fonts": FONTS, "schema": schema_html, "extra": extra_head,
        "nav": nav(active or slug, over_hero), "body": body, "footer": footer(),
    }


# ---------------------------------------------------------------------------
# REUSABLE BLOCKS
# ---------------------------------------------------------------------------
def page_head(title, subtitle, crumbs_items, bg=None):
    cr = ""
    for i, (name, href) in enumerate(crumbs_items):
        if href:
            cr += '<a href="%s">%s</a><span>/</span>' % (href, name)
        else:
            cr += '<span style="opacity:1;color:rgba(255,255,255,.85)">%s</span>' % name
    bg_html = ('<div class="phead__bg"><img src="assets/img/%s" alt="" loading="lazy"></div>' % bg) if bg else ""
    return """
<section class="phead">
  %s
  <div class="container">
    <div class="crumbs">%s</div>
    <h1 data-reveal>%s</h1>
    <p data-reveal>%s</p>
  </div>
</section>""" % (bg_html, cr, title, subtitle)


def cta_band(title, text, primary=("contact.html", "Book a free consultation"), wa_text=None):
    wa_btn = ('<a class="btn btn--green btn--lg" data-wa="%s">%s Chat on WhatsApp</a>'
              % (wa_text or COMPANY["wa_default"], ico("wa")))
    return """
<section class="section">
  <div class="container">
    <div class="cta-band" data-reveal>
      <div class="split" style="align-items:center">
        <div>
          <span class="eyebrow">Get started</span>
          <h2>%s</h2>
          <p>%s</p>
        </div>
        <div class="btn-row" style="justify-content:flex-end">
          <a class="btn btn--primary btn--lg" href="%s">%s</a>
          %s
        </div>
      </div>
    </div>
  </div>
</section>""" % (title, text, primary[0], primary[1], wa_btn)


def naira(n):
    return "₦" + format(n, ",d")
