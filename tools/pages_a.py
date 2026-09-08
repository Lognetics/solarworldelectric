# -*- coding: utf-8 -*-
"""Page bodies: home, about, solutions, products."""

from data import COMPANY, STATS, CLIENTS, PACKAGES, CATEGORIES, OFFICES
from content import WHY_US, PROCESS, FAQ_GROUPS, WA_REVIEWS, TEAM
from case_studies import CASES
from layout import ico, page_head, cta_band, naira, SITE
from globe import globe_block, orbit_globe


# ---------------------------------------------------------------------------
# SHARED BLOCKS
# ---------------------------------------------------------------------------
def client_marquee(dark=True, title=None):
    items = "".join(
        '<div class="marquee__item"><img src="assets/img/clients/%s" alt="%s, Solar World Electric client" '
        'loading="lazy" width="180" height="70"></div>' % (c["file"], c["name"])
        for c in CLIENTS
    )
    head = ('<p class="center small muted" style="margin-bottom:26px;letter-spacing:.14em;'
            'text-transform:uppercase;font-weight:650">%s</p>' % title) if title else ""
    return """
<section class="section--tight%s" style="padding-block:clamp(34px,4.4vw,56px)">
  <div class="container">%s</div>
  <div class="marquee"><div class="marquee__track">%s</div></div>
</section>""" % (" section--dark" if dark else " section--alt", head, items)


def stats_band():
    cells = "".join(
        '<div class="stat" data-reveal><div class="stat__n"><span data-count="%d" data-suf="%s">0</span></div>'
        '<div class="stat__l">%s</div></div>' % (s["n"], s["suffix"], s["label"])
        for s in STATS
    )
    return '<section class="section--dark"><div class="stats">%s</div></section>' % cells


def faq_block(groups, single=False, limit=None):
    out = []
    n = 0
    for g in groups:
        for q, a in g["items"]:
            if limit and n >= limit:
                break
            body = "".join(p if p.startswith("<ul") else "<p>%s</p>" % p for p in a)
            out.append(
                '<div class="faq__item" data-searchable>'
                '<button class="faq__q" type="button" aria-expanded="false">'
                '<span>%s</span><span class="ico">%s</span></button>'
                '<div class="faq__a"><div>%s</div></div></div>' % (q, ico("plus"), body)
            )
            n += 1
    return '<div class="faq"%s>%s</div>' % (" data-single" if single else "", "".join(out))


def wa_card(r):
    return """
<figure class="wa-card" data-cat="%s" data-reveal>
  <figcaption class="wa-card__bar">
    %s
    <span><span class="wa-card__who">%s</span><span class="wa-card__where">%s</span></span>
    <span class="wa-card__verified">%s Verified</span>
  </figcaption>
  <div class="wa-card__shot"><img src="assets/img/reviews/%s" alt="%s" loading="lazy"></div>
  <blockquote class="wa-card__quote">“%s”</blockquote>
</figure>""" % (r.get("cat", "residential"), ico("wa"), r["who"], r["where"], ico("check"), r["shot"], r["alt"], r["quote"])


def pkg_card(p):
    specs = "".join('<li>%s<span>%s</span></li>' % (ico("check"), s) for s in p["specs"])
    return """
<article class="pkg" data-reveal>
  <div class="pkg__media">
    <img src="assets/img/%s" alt="%s" loading="lazy">
    <span class="pkg__tag">%s</span>
  </div>
  <div class="pkg__body">
    <h3 class="pkg__title">%s</h3>
    <div class="pkg__spec"><span class="chip chip--gold">%s</span></div>
    <ul class="pkg__list">%s</ul>
    <p class="small muted"><b>Runs:</b> %s</p>
    <div class="pkg__price">
      <span class="amt">%s</span>
      <span class="note">%s</span>
    </div>
    <a class="btn btn--dark btn--block" style="margin-top:16px" data-wa="Hello Solar World, I am interested in the %s. Please send me the details and next steps.">Request this package %s</a>
  </div>
</article>""" % (p["img"], p["alt"], p["tag"], p["title"], p["kw"], specs, p["loads"],
                 naira(p["price"]), p["note"], p["title"].replace("&amp;", "and"), ico("arrow"))


def case_card(c):
    specs = "".join('<div><div class="v">%s</div><div class="k">%s</div></div>' % (v, k)
                    for k, v in c["specs"][:3])
    cat_label = next(x["label"] for x in CATEGORIES if x["key"] == c["cat"])
    return """
<article class="case" data-cat="%s" data-reveal id="%s">
  <div class="case__media">
    <img src="assets/img/%s" alt="%s" loading="lazy">
    <span class="case__cat">%s</span>
  </div>
  <div class="case__body">
    <h3>%s</h3>
    <div class="case__meta"><span class="chip">%s</span>%s</div>
    <p class="case__excerpt">%s</p>
    <div class="case__spec">%s</div>
    <div class="case__foot"><a class="tlink" href="projects.html#cs-%s">Read the full case study %s</a></div>
  </div>
</article>""" % (c["cat"], c["id"], c["img"], c["alt"], cat_label, c["title"], c["type"],
                 ('<span class="chip">%s</span>' % c["location"]) if c.get("location") else "",
                 c["excerpt"], specs, c["id"], ico("arrow"))


def sizer_block():
    """Interactive system sizer. Tap a load to add, shift-tap to remove."""
    return """
<div class="card" id="sizer" data-reveal="right">
  <div class="row" style="justify-content:space-between;margin-bottom:6px">
    <h3 style="margin:0">Size your system</h3>
    <span class="chip chip--gold">Live</span>
  </div>
  <p class="small muted">Tap an appliance to add it. Shift-tap to take one off.</p>
  <div class="picker" id="sizerPicker" style="margin:16px 0 18px"></div>
  <div class="field">
    <label for="sizerHours">How long must it run without the grid?</label>
    <select id="sizerHours">
      <option value="6">6 hours, night only</option>
      <option value="10" selected>10 hours, evening and night</option>
      <option value="16">16 hours, most of the day</option>
      <option value="24">24 hours, full independence</option>
    </select>
  </div>
  <dl class="readout readout--total" id="sizerOut" style="margin-top:16px"></dl>
  <a class="btn btn--primary btn--block" id="sizerSend" style="margin-top:16px" href="#">
    Send this to an engineer %s</a>
  <p class="form-note">Indicative only. A free load assessment gives you the exact specification.</p>
</div>""" % ico("wa")


def versus_block(dark=True):
    """Generator vs solar running-cost comparison."""
    return """
<div class="card%s" id="versus" data-reveal="left">
  <h3>What is the generator actually costing you?</h3>
  <p class="small%s">Drag the sliders to match your own running pattern.</p>

  <div class="field" style="margin-top:20px">
    <label for="vsLitres">Diesel burned per day <b id="vsLitresOut" class="text-gold"></b></label>
    <input class="range" type="range" id="vsLitres" min="2" max="60" step="1" value="12">
  </div>
  <div class="field">
    <label for="vsPrice">Price per litre <b id="vsPriceOut" class="text-gold"></b></label>
    <input class="range" type="range" id="vsPrice" min="700" max="2000" step="25" value="1100">
  </div>
  <div class="field">
    <label for="vsSystem">Solar system cost <b id="vsSystemOut" class="text-gold"></b></label>
    <input class="range" type="range" id="vsSystem" min="1490000" max="50000000" step="250000" value="9290000">
  </div>
  <div class="field">
    <label for="vsYears">Compared over <b id="vsYearsOut" class="text-gold"></b></label>
    <input class="range" type="range" id="vsYears" min="1" max="15" step="1" value="5">
  </div>

  <div class="versus" style="margin-top:26px">
    <div class="versus__row">
      <div class="versus__top">
        <span class="versus__name"><i style="background:linear-gradient(90deg,#E5484D,#F76B1C)"></i>Generator</span>
        <span class="versus__val" id="vsGenVal"></span>
      </div>
      <div class="versus__bar"><div class="versus__fill versus__fill--gen" id="vsGenBar"></div></div>
    </div>
    <div class="versus__row">
      <div class="versus__top">
        <span class="versus__name"><i style="background:var(--g-gold)"></i>Solar system</span>
        <span class="versus__val" id="vsSolVal"></span>
      </div>
      <div class="versus__bar"><div class="versus__fill versus__fill--sol" id="vsSolBar"></div></div>
    </div>
  </div>
  <p class="versus__note" id="vsNote"></p>
  <p class="form-note">Generator figure includes fuel plus servicing at 12%% of annual fuel spend.
  It excludes the generator purchase and eventual replacement, so the real gap is wider.</p>
</div>""" % (" form-dark card--glass" if dark else "", " muted" if not dark else "")


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
HERO_SLIDES = [
    ("project-ground-array-1.jpg",
     "The future of power<br>in Africa is <span class=\"grad-text\">Solar</span>",
     "Solar, inverter and lithium battery systems designed, installed and maintained for Nigerian homes, "
     "businesses and institutions. Over 60,000 powered since 2015."),
    ("pkg/pkg-80kw.jpg",
     "Industrial power<br>that <span class=\"grad-text\">never stops</span>",
     "From 20 kW offices to 125 kW factories, high-voltage solar and lithium storage engineered for "
     "continuous duty in Nigerian conditions."),
    ("project-rooftop-lekki.jpg",
     "Your home, off the<br><span class=\"grad-text\">generator</span> for good",
     "Run your air conditioners, fridges, freezers and everything else through the night, silently, "
     "on stored sunlight."),
    ("pkg/pkg-25kw.jpg",
     "Own your system<br>from <span class=\"grad-text\">30% down</span>",
     "Pay 30% upfront and spread the balance over 3, 6, 9 or 12 months. Financing disbursed in 24–48 hours, "
     "installation straight after."),
]


def home():
    slides = ""
    for i, (img, h1, sub) in enumerate(HERO_SLIDES):
        # <video> ready: drop a .mp4 next to the image and swap the <img> for
        # <video muted playsinline loop preload="metadata" poster="...">
        slides += ('<div class="hero__slide%s" data-h1="%s" data-sub="%s">'
                   '<img src="assets/img/%s" alt="" %s></div>'
                   % (" is-active" if i == 0 else "", h1.replace('"', "&quot;"), sub.replace('"', "&quot;"),
                      img, 'fetchpriority="high"' if i == 0 else 'loading="lazy"'))

    hero_stats = "".join(
        '<div><div class="n"><span data-count="%d" data-suf="%s">0</span></div><div class="l">%s</div></div>'
        % (s["n"], s["suffix"], s["label"].replace("<br>", " "))
        for s in STATS
    )

    why = "".join(
        '<article class="card spotlight" data-reveal><div class="card__ico">%s</div>'
        '<h3>%s</h3><p>%s</p></article>' % (ico(i), t, d)
        for t, d, i in WHY_US
    )

    seg_icons = {"residential": "home", "commercial": "office",
                 "industrial": "factory", "infrastructure": "grid"}
    segs = "".join(
        '<a class="card card--glass spotlight" data-reveal href="projects.html?c=%s">'
        '<div class="card__ico">%s</div><h3>%s</h3><p>%s</p>'
        '<span class="tlink" style="margin-top:14px">See projects %s</span></a>'
        % (c["key"], ico(seg_icons[c["key"]]), c["label"], c["blurb"], ico("arrow"))
        for c in CATEGORIES
    )

    pkgs = "".join(pkg_card(p) for p in PACKAGES[:4])

    featured = [c for c in CASES if c.get("featured")][:3]
    cases = "".join(case_card(c) for c in featured)

    reviews = "".join(wa_card(r) for r in WA_REVIEWS[:6])

    steps = "".join(
        '<div class="step" data-reveal><div class="step__n"></div><div><h4>%s</h4><p>%s</p></div></div>'
        % (t, d) for t, d in PROCESS
    )

    return """
<section class="hero" id="hero">
  <div class="hero__stage">%(slides)s</div>
  <div class="hero__scrim"></div>
  <div class="hero__aurora" aria-hidden="true"><span></span><span></span><span></span></div>
  <div class="hero__grid" aria-hidden="true"></div>

  <div class="container hero__inner">
    <div class="hero__content">
      <span class="pill"><span class="dot"></span> RC %(rc)s · Powering Nigeria since %(founded)s</span>
      <h1 id="heroTitle" style="margin-top:1.2rem">%(h1)s</h1>
      <p class="hero__sub" id="heroSub">%(sub)s</p>
      <div class="btn-row">
        <a class="btn btn--primary btn--lg" href="contact.html">Get a free consultation</a>
        <a class="btn btn--ghost btn--lg" data-wa="">%(wa)s Chat on WhatsApp</a>
      </div>
      <div class="hero__stats">%(hstats)s</div>
    </div>
  </div>

  <div class="hero__scroll"><i></i> Scroll</div>
  <div class="hero__arrows">
    <button type="button" id="heroPrev" aria-label="Previous slide">%(left)s</button>
    <button type="button" id="heroNext" aria-label="Next slide">%(right)s</button>
  </div>
  <div class="hero__dots" id="heroDots" role="tablist" aria-label="Hero slides"></div>
</section>

<!-- ========== GLOBAL ENERGY BAND (spinning wireframe world map) ========== -->
<section class="section section--deep" style="padding-block:clamp(48px,6vw,86px)">
  <div class="container split" style="align-items:center">
    <div data-reveal="left">
      <span class="eyebrow">Live network</span>
      <h2 class="rise"><span>Powering Nigeria,<br>around the clock</span></h2>
      <p class="lead" style="color:var(--d-fg-muted)">Every system we install joins the same
      network of self-generated, self-stored power. No grid dependence, no fuel queue,
      no generator noise.</p>
      <div class="ticker" style="margin-top:26px">
        <div class="ticker__row"><span class="ticker__dot"></span>
          <span class="ticker__l">Homes, offices and businesses powered</span>
          <span class="ticker__v"><span data-count="60000" data-suf="+">0</span></span></div>
        <div class="ticker__row"><span class="ticker__dot"></span>
          <span class="ticker__l">Offices across three cities</span>
          <span class="ticker__v"><span data-count="11">0</span></span></div>
        <div class="ticker__row"><span class="ticker__dot"></span>
          <span class="ticker__l">Typical install after payment</span>
          <span class="ticker__v"><span data-count="48" data-suf="hr">0</span></span></div>
      </div>
    </div>
    <div data-reveal="right">%(orbit)s</div>
  </div>
</section>

%(marquee)s

<!-- ========== DIRECT ANSWER (AI / featured-snippet target) ========== -->
<section class="section">
  <div class="container split">
    <div data-reveal="left">
      <span class="eyebrow">Who we are</span>
      <h2>Nigeria&rsquo;s solar company for people who cannot afford to lose power</h2>
      <p class="lead">%(name)s (RC %(rc)s) has designed, installed and maintained solar, hybrid inverter and
      lithium battery systems across Nigeria since %(founded)s, for homes, offices, hotels, schools, hospitals,
      factories, communities and government institutions.</p>
      <div class="answer" style="margin-top:26px">
        <span class="answer__k">%(spark)s Quick answer</span>
        <p><b>What does Solar World Electric do?</b> We size, supply, install and maintain complete solar power
        systems in Nigeria, solar panels, hybrid inverters and lithium battery storage, from 3 kVA home
        packages to 125 kW industrial systems. We operate eleven offices across Abuja, Lagos and Port Harcourt,
        install nationwide, publish our prices openly, and back every installation with up to 25 years of panel
        warranty and a year of free after-sales support.</p>
      </div>
      <div class="btn-row" style="margin-top:28px">
        <a class="btn btn--outline" href="about.html">About Solar World</a>
        <a class="btn btn--outline" href="pricing.html">See our prices</a>
      </div>
    </div>
    <div class="media-stack" data-reveal="right">
      <div class="media"><img src="assets/img/showroom-interior.jpg"
        alt="Solar World Electric showroom displaying hybrid inverters, lithium batteries and solar panels" loading="lazy"></div>
      <div class="badge"><span class="n">60k+</span><span class="l">homes &amp; businesses<br>powered</span></div>
    </div>
  </div>
</section>

%(stats)s

<!-- ========== WHY US ========== -->
<section class="section section--alt">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">The competitive edge</span>
      <h2>Why Nigerians choose Solar World</h2>
      <p>We believe who you buy from is as important, if not more important, than the product itself.</p>
    </div>
    <div class="grid grid-3">%(why)s</div>
  </div>
</section>

<!-- ========== GLOBE / GLOBAL ENERGY ========== -->
<section class="section section--deep">
  <div class="container split">
    <div data-reveal="left">
      <span class="eyebrow">The global shift</span>
      <h2>The world is moving to renewable energy. Nigeria is moving faster.</h2>
      <p class="lead" style="color:var(--d-fg-muted)">Skyrocketing energy costs are not a Nigerian problem; they are a global one. The difference here is that we have never been able to rely on the grid, which
      makes the case for self-generated, self-stored power immediate rather than theoretical.</p>
      <div class="kpis" style="margin-top:30px">
        <div><div class="kpi__n" style="color:var(--gold)"><span data-count="60000" data-suf="+">0</span></div>
             <div class="kpi__l" style="color:var(--d-fg-muted)">Homes, offices, hotels, businesses and communities powered</div></div>
        <div><div class="kpi__n" style="color:var(--gold)"><span data-count="11">0</span></div>
             <div class="kpi__l" style="color:var(--d-fg-muted)">Offices across three cities, installing nationwide</div></div>
        <div><div class="kpi__n" style="color:var(--gold)"><span data-count="25" data-suf="yr">0</span></div>
             <div class="kpi__l" style="color:var(--d-fg-muted)">Panel warranty on our Deye and Solis lines</div></div>
      </div>
      <div class="btn-row" style="margin-top:32px">
        <a class="btn btn--primary" href="solutions.html">Explore our solutions</a>
        <a class="btn btn--ghost" href="projects.html">See what we have built</a>
      </div>
    </div>
    <div data-reveal="right">%(globe)s</div>
  </div>
</section>

<!-- ========== SEGMENTS ========== -->
<section class="section section--dark">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">What we power</span>
      <h2>Four categories. One standard of engineering.</h2>
      <p>Every system is sized against the building&rsquo;s actual load, never pulled off a shelf.</p>
    </div>
    <div class="grid grid-4">%(segs)s</div>
  </div>
</section>

<!-- ========== PACKAGES ========== -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Packages &amp; pricing</span>
      <h2>Complete solar and inverter packages, priced openly</h2>
      <p>Prices below include the inverter, lithium battery storage, the solar array, cables, accessories and
      installation. Full Deye, Solis and standard price charts are on the pricing page.</p>
    </div>
    <div class="grid grid-4">%(pkgs)s</div>
    <div class="btn-row" style="margin-top:38px;justify-content:center">
      <a class="btn btn--dark btn--lg" href="pricing.html">See all packages &amp; prices %(arrow)s</a>
      <a class="btn btn--outline btn--lg" href="calculator.html">Size my system</a>
    </div>
  </div>
</section>

<!-- ========== INTERACTIVE: SIZER ========== -->
<section class="section section--alt">
  <div class="container split" style="align-items:start">
    <div data-reveal="left">
      <span class="eyebrow">Try it yourself</span>
      <h2>What would your system look like?</h2>
      <p class="lead">Pick the appliances you want running when the grid is off. We will estimate the
      inverter size, battery capacity, panel count and an indicative price straight from our
      published charts.</p>
      <div class="facts" style="margin-top:26px">
        <div><dt>Inverter sized by</dt><dd>Peak surge</dd></div>
        <div><dt>Battery sized by</dt><dd>Overnight kWh</dd></div>
        <div><dt>Panels sized by</dt><dd>Daily refill</dd></div>
      </div>
      <p class="small muted" style="margin-top:18px">Air conditioning is almost always what decides
      the system. Add one AC and watch every number move.</p>
      <div class="btn-row" style="margin-top:20px">
        <a class="btn btn--dark" href="calculator.html">Open the full calculator %(arrow)s</a>
      </div>
    </div>
    %(sizer)s
  </div>
</section>

<!-- ========== INTERACTIVE: GENERATOR VS SOLAR ========== -->
<section class="section section--deep">
  <div class="container split" style="align-items:start">
    %(versus)s
    <div data-reveal="right">
      <span class="eyebrow">The real comparison</span>
      <h2>A generator is cheap to buy and expensive to own</h2>
      <p class="lead" style="color:var(--d-fg-muted)">A generator's purchase price is the smallest
      number in the story. Fuel, servicing, parts and replacement never stop, and they rise every year.</p>
      <p style="color:var(--d-fg-muted)">A solar system inverts that shape. The cost is concentrated
      once, at the start, and generation afterwards is effectively free. Our panels carry a 25-year
      warranty and our lithium batteries a 10-year warranty, so the system keeps producing long after
      a generator bought on the same day would have been replaced twice.</p>
      <div class="btn-row" style="margin-top:26px">
        <a class="btn btn--primary" href="financing.html">Spread it over 12 months</a>
        <a class="btn btn--ghost" href="pricing.html">See system prices</a>
      </div>
    </div>
  </div>
</section>

<!-- ========== CASE STUDIES ========== -->
<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Case studies</span>
      <h2>Real installations, real specifications</h2>
      <p>Residential, commercial, industrial and infrastructure projects, with the system configuration,
      the loads it carries and what it changed for the customer.</p>
    </div>
    <div class="cases">%(cases)s</div>
    <div class="btn-row" style="margin-top:38px;justify-content:center">
      <a class="btn btn--dark btn--lg" href="projects.html">Browse all case studies %(arrow)s</a>
    </div>
  </div>
</section>

<!-- ========== REVIEWS ========== -->
<section class="section section--deep">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Customer reviews</span>
      <h2>What customers message us afterwards</h2>
      <p>Unedited WhatsApp conversations with customers after installation. Names shortened for privacy.</p>
    </div>
    <div class="wall">%(reviews)s</div>
    <div class="btn-row" style="margin-top:40px;justify-content:center">
      <a class="btn btn--primary btn--lg" href="reviews.html">Read the full review wall %(arrow)s</a>
    </div>
  </div>
</section>

<!-- ========== PROCESS ========== -->
<section class="section">
  <div class="container split" style="align-items:start">
    <div data-reveal="left" style="position:sticky;top:calc(var(--nav-h) + 30px)">
      <span class="eyebrow">Our process</span>
      <h2>From first conversation to switch-on</h2>
      <p class="lead">Seven steps, no surprises. Most installations are completed within 48 hours of payment
      confirmation.</p>
      <div class="btn-row" style="margin-top:26px">
        <a class="btn btn--primary" href="contact.html">Start with a free consultation</a>
      </div>
    </div>
    <div class="steps" data-reveal="right">%(steps)s</div>
  </div>
</section>

<!-- ========== FINANCING ========== -->
<section class="section section--alt">
  <div class="container split">
    <div class="media" data-reveal="left">
      <img src="assets/img/install-room-stack1.jpg"
        alt="Lithium battery bank and hybrid inverters installed by Solar World Electric" loading="lazy">
    </div>
    <div data-reveal="right">
      <span class="eyebrow">Financing</span>
      <h2>Switching to solar should not be a financial burden</h2>
      <p class="lead">Pay <b>30%% upfront</b> and spread the balance over 3, 6, 9 or 12 months through our
      financing partner. A fixed 4%% monthly interest is added to the principal, with no hidden charges.</p>
      <div class="facts" style="margin:26px 0">
        <div><dt>Deposit</dt><dd>30%% of system cost</dd></div>
        <div><dt>Terms</dt><dd>3, 6, 9 or 12 months</dd></div>
        <div><dt>Disbursement</dt><dd>24–48 hours</dd></div>
        <div><dt>Interest</dt><dd>Fixed 4%% monthly</dd></div>
      </div>
      <p class="small muted">Example: on a ₦5,000,000 system your upfront payment is ₦1,500,000 and our
      financing partner covers the remaining ₦3,500,000.</p>
      <div class="btn-row" style="margin-top:22px">
        <a class="btn btn--dark" href="financing.html">How financing works</a>
        <a class="btn btn--outline" data-wa="Hello Solar World, I would like to know more about your 30%% deposit financing plan.">Ask about financing</a>
      </div>
    </div>
  </div>
</section>

<!-- ========== FAQ ========== -->
<section class="section">
  <div class="container container--narrow">
    <div class="section-head center">
      <span class="eyebrow">Questions people ask us</span>
      <h2>Solar in Nigeria, answered plainly</h2>
      <p>The questions we are asked most often, with straight answers, real prices and no hedging.</p>
    </div>
    %(faq)s
    <div class="btn-row" style="margin-top:36px;justify-content:center">
      <a class="btn btn--dark btn--lg" href="faq.html">See all %(faqcount)d questions %(arrow)s</a>
    </div>
  </div>
</section>

%(cta)s
""" % {
        "slides": slides, "rc": COMPANY["rc"], "founded": COMPANY["founded"],
        "h1": HERO_SLIDES[0][1], "sub": HERO_SLIDES[0][2], "wa": ico("wa"),
        "hstats": hero_stats, "left": ico("left"), "right": ico("right"),
        "marquee": client_marquee(dark=False, title="Trusted by leading Nigerian organisations"),
        "name": COMPANY["name"], "spark": ico("spark"),
        "stats": stats_band(), "why": why, "globe": globe_block(), "segs": segs,
        "orbit": orbit_globe(), "sizer": sizer_block(), "versus": versus_block(),
        "pkgs": pkgs, "arrow": ico("arrow"), "cases": cases, "reviews": reviews, "steps": steps,
        "faq": faq_block(FAQ_GROUPS, single=True, limit=7),
        "faqcount": sum(len(g["items"]) for g in FAQ_GROUPS),
        "cta": cta_band(
            "Tell us what you want to power. We will size it, price it and install it.",
            "Free consultation and load assessment at any of our eleven offices in Abuja, Lagos and Port Harcourt "
            ", or over WhatsApp, wherever you are in Nigeria."),
    }


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
def about():
    team = "".join(
        '<article class="team__card%s" data-reveal>'
        '<div class="team__photo">'
        '<img src="assets/img/%s" alt="%s, %s at Solar World Electric Technology Ltd" loading="lazy">'
        '<span class="team__ring"></span></div>'
        '<div class="team__body"><h3 class="team__name">%s</h3><p class="team__role">%s</p></div>'
        '</article>'
        % (" team__lead" if i < 3 else "", img, name, role.replace("&amp;", "and"), name, role)
        for i, (name, role, img) in enumerate(TEAM)
    )
    values = "".join(
        '<article class="card card--glass" data-reveal><div class="card__ico">%s</div><h3>%s</h3><p>%s</p></article>'
        % (ico(i), t, d) for t, d, i in [
            ("Our vision", COMPANY["vision"], "sun"),
            ("Our mission", COMPANY["mission"], "bolt"),
            ("Our belief system", COMPANY["belief"], "shield"),
        ]
    )
    return """
%(head)s

<section class="section">
  <div class="container split">
    <div data-reveal="left">
      <span class="eyebrow">Who we are</span>
      <h2>Transforming how Nigerian homes and businesses access energy</h2>
      <p class="lead">At %(legal)s, we are dedicated to transforming the way homes and businesses access energy
      by providing high-quality, sustainable and cost-effective solar power solutions.</p>
      <p>As a trusted leader in the renewable energy sector, we specialise in the sales, installation and
      maintenance of a wide range of solar-powered products designed to meet the unique energy needs of
      individuals and organisations.</p>
      <p>With the rising demand for reliable electricity, we offer cutting-edge solar technology that ensures
      uninterrupted power supply while reducing energy costs and environmental impact. Whether for residential,
      commercial or industrial use, our team of experts is well poised to deliver installations excellently and
      professionally.</p>
      <div class="facts" style="margin-top:28px">
        <div><dt>Established</dt><dd>%(founded)s</dd></div>
        <div><dt>RC number</dt><dd>%(rc)s</dd></div>
        <div><dt>Offices</dt><dd>9 across 3 cities</dd></div>
        <div><dt>Powered</dt><dd>60,000+ customers</dd></div>
      </div>
    </div>
    <div class="media" data-reveal="right">
      <img src="assets/img/team-1.jpg" alt="The Solar World Electric Technology Ltd team in Nigeria" loading="lazy">
    </div>
  </div>
</section>

<section class="section section--deep">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">What drives us</span>
      <h2>Vision, mission and belief system</h2>
    </div>
    <div class="grid grid-3">%(values)s</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Let us talk facts</span>
      <h2>Why switch to solar energy?</h2>
      <p>The reality of skyrocketing energy cost, not just in Nigeria but all over the world, has presented a
      clear need for a viable energy alternative. That alternative has to be renewable, because of the
      self-sustaining nature of the renewable energy solution.</p>
    </div>
    <div class="container--narrow">
      <div class="answer" data-reveal>
        <span class="answer__k">%(spark)s The short version</span>
        <p>Our homes need power. Our offices and business operations need power. Our communities and government
        institutions need power, and we are talking about reliable, sustainable and cost-effective power.
        That is what %(legal)s is offering.</p>
      </div>
    </div>
    <div class="grid grid-3" style="margin-top:44px">
      <article class="card" data-reveal><div class="card__ico">%(bolt)s</div>
        <h3>Reduce reliance on the grid</h3>
        <p>By generating your own power you stop being exposed to rising electricity costs and to whether the
        grid is up on any given day.</p></article>
      <article class="card" data-reveal><div class="card__ico">%(sun)s</div>
        <h3>Clean and renewable</h3>
        <p>Solar energy is clean, renewable and reduces carbon emissions, contributing to a greener planet, and a quieter, fume-free property.</p></article>
      <article class="card" data-reveal><div class="card__ico">%(wallet)s</div>
        <h3>Pays back over time</h3>
        <p>The initial investment can be high, but solar systems significantly reduce and eventually eliminate
        the fuel and diesel bill that a generator never stops charging you.</p></article>
    </div>
  </div>
</section>

<section class="section section--alt" id="team">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Behind the scenes</span>
      <h2>Meet our team</h2>
      <p>The people who design, sell, install and support every Solar World system. Fifteen of them,
      across Abuja, Lagos and Port Harcourt.</p>
    </div>
    <div class="team">%(team)s</div>
    <p class="center small muted" style="margin-top:34px">
      Every installation is carried out by our own engineers, never subcontracted.
    </p>
  </div>
</section>

%(marquee)s

%(cta)s
""" % {
        "head": page_head(
            "Power you can always count on",
            "Solar World Electric Technology Limited has been designing, installing and maintaining solar power "
            "systems across Nigeria since 2015, for homes, businesses, industries and government.",
            [("Home", "index.html"), ("About", None)], bg="store-front-1.jpg"),
        "legal": COMPANY["legal"], "founded": COMPANY["founded"], "rc": COMPANY["rc"],
        "values": values, "team": team, "spark": ico("spark"),
        "bolt": ico("bolt"), "sun": ico("sun"), "wallet": ico("wallet"),
        "marquee": client_marquee(dark=True, title="Organisations that trust us"),
        "cta": cta_band("Ready to make the switch?",
                        "Contact us today to schedule a free consultation, get expert advice, or simply learn "
                        "more about how solar energy can benefit you."),
    }


# ---------------------------------------------------------------------------
# SOLUTIONS
# ---------------------------------------------------------------------------
SOLUTION_BLOCKS = [
    ("residential", "home", "Residential &amp; small commercial solar",
     "5 kVA – 20 kVA",
     "install-deye-3batt.jpg",
     "Residential solar installation with hybrid inverter and lithium batteries in a Nigerian home",
     ["We provide residential and small commercial solar systems ranging from 5 kVA to 20 kVA to deliver "
      "reliable and efficient energy for homes, offices and growing businesses, delivering consistent power "
      "for everyday needs while ensuring backup during outages.",
      "These systems are built with durable, high-quality components that guarantee long-term performance "
      "with minimal maintenance. They are capable of powering essential appliances and systems including "
      "lighting, televisions, refrigerators, water pumps, internet devices, office equipment and air "
      "conditioning units.",
      "With quiet operation and reduced reliance on grid electricity, users benefit from lower energy costs, "
      "improved energy independence and protection against inconsistent power supply."],
     ["Homeowners", "Estates", "Duplexes", "Apartments", "Family homes"]),

    ("commercial", "office", "Commercial solar systems",
     "20 kW – 80 kW",
     "pkg/pkg-50kw-a.jpg",
     "Commercial solar and inverter installation for an office building in Nigeria",
     ["Offices, hotels, schools, hospitals, shopping facilities, restaurants, warehouses and retail businesses "
      "share one problem: an outage costs money the moment it starts, and a generator only converts that cost "
      "into fuel.",
      "Our commercial systems run from 20 kW three-phase installations up to 80 kW high-voltage packages with "
      "battery management, combiner boxes and engineered mounting. Because commercial demand usually peaks "
      "during daylight, most of the load is served directly from the array while storage carries early "
      "mornings, evenings and cloudy spells.",
      "Systems integrate with your existing distribution board, with no switchover gap for POS terminals, "
      "servers, refrigeration or medical equipment to survive."],
     ["Offices", "Hotels", "Schools", "Hospitals", "Shopping facilities", "Restaurants", "Warehouses", "Retail"]),

    ("industrial", "factory", "Industrial solar systems",
     "80 kW – 125 kW+",
     "install-deye-rack.jpg",
     "Industrial solar system with stacked lithium battery racks and dual inverters in Nigeria",
     ["These systems are designed for high-demand environments where consistent, uninterrupted power is "
      "essential, ranging from industrial facilities and commercial buildings to luxury residences and "
      "premium developments.",
      "%s delivers durable, high-performance systems built with industrial-grade components capable of "
      "withstanding heavy loads and continuous operation, ensuring long-term reliability and stability.",
      "These systems are capable of powering centralised air conditioning, chillers, compressors, air handling "
      "units, ventilation systems, cold rooms, industrial machinery, elevators and full-building power systems.",
      "Their robust and scalable design allows for future expansion, while intelligent energy management "
      "optimises power usage for maximum efficiency. By significantly reducing dependence on grid electricity "
      "and diesel generators, they lower operational costs, provide protection against power instability, and "
      "deliver a clean, quiet and dependable energy solution suited for both industrial performance and "
      "luxury comfort."],
     ["Factories", "Manufacturing", "Processing facilities", "Large-scale facilities"]),

    ("infrastructure", "grid", "Energy &amp; infrastructure",
     "Streetlights · pumping · EV",
     "project-streetlight.jpg",
     "Solar street lighting and infrastructure projects delivered by Solar World Electric",
     ["We also provide high-quality, reliable solutions across a range of essential products, including water "
      "heaters, submersible pumps, inverter air conditioners and street lighting systems.",
      "All-in-one solar street lights integrate the panel, lithium battery, controller and LED head into a "
      "single pole-mounted unit, with no trenching, no cabling and no metered supply. Solar water pumping drives a "
      "submersible pump directly from the array through an MPPT controller, storing water rather than "
      "electricity.",
      "Our installations are tailored to meet both residential and commercial needs, ensuring efficiency, "
      "durability and long-term performance. With a proven track record of successful projects for a diverse "
      "clientele, we are committed to delivering expert service, trusted products and customer satisfaction at "
      "every stage, from consultation to installation and support."],
     ["Solar streetlights", "Community projects", "Solar pumping", "EV charging"]),
]


def solutions():
    blocks = ""
    for i, (key, icon, title, cap, img, alt, paras, tags) in enumerate(SOLUTION_BLOCKS):
        body = "".join("<p>%s</p>" % (p % COMPANY["legal"] if "%s" in p else p) for p in paras)
        chips = "".join('<span class="chip">%s</span>' % t for t in tags)
        media = ('<div class="media" data-reveal="%s"><img src="assets/img/%s" alt="%s" loading="lazy"></div>'
                 % ("right" if i % 2 == 0 else "left", img, alt))
        text = """<div data-reveal="%s">
          <span class="eyebrow">%s</span>
          <h2>%s</h2>
          <div class="row" style="margin-bottom:18px">%s</div>
          %s
          <a class="btn btn--dark" style="margin-top:12px" href="projects.html?c=%s">See %s projects %s</a>
        </div>""" % ("left" if i % 2 == 0 else "right", cap, title, chips, body, key,
                     title.split("&amp;")[0].strip().lower(), ico("arrow"))
        inner = (text + media) if i % 2 == 0 else (media + text)
        blocks += ('<section class="section%s" id="%s"><div class="container split">%s</div></section>'
                   % (" section--alt" if i % 2 else "", key, inner))

    return """
%(head)s

<section class="section section--tight">
  <div class="container container--narrow">
    <div class="answer" data-reveal>
      <span class="answer__k">%(spark)s Quick answer</span>
      <p><b>What solar solutions does Solar World provide?</b> Four: residential and small commercial systems
      from 5 kVA to 20 kVA; commercial systems from 20 kW to 80 kW for offices, hotels, schools, hospitals and
      retail; industrial systems from 80 kW to 125 kW and beyond for factories and processing plants; and
      energy infrastructure, solar street lighting, solar water pumping, EV charging and community projects.
      Every system is sized against the building&rsquo;s actual measured load.</p>
    </div>
  </div>
</section>

%(blocks)s

<section class="section section--deep">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">The concept of a full solar system</span>
      <h2>What a complete solar system actually contains</h2>
      <p>Buying an inverter alone gives you backup. Buying the full system gives you generation.</p>
    </div>
    <div class="grid grid-auto-sm">%(components)s</div>
  </div>
</section>

<section class="section">
  <div class="container split" style="align-items:start">
    <div data-reveal="left" style="position:sticky;top:calc(var(--nav-h) + 30px)">
      <span class="eyebrow">Our process</span>
      <h2>How a Solar World installation runs</h2>
      <p class="lead">Seven steps from first conversation to switch-on, with a site visit wherever the
      building needs one.</p>
      <div class="btn-row" style="margin-top:24px">
        <a class="btn btn--primary" href="contact.html">Book a free consultation</a>
      </div>
    </div>
    <div class="steps" data-reveal="right">%(steps)s</div>
  </div>
</section>

%(cta)s
""" % {
        "head": page_head(
            "Solar solutions for every building in Nigeria",
            "Residential, commercial, industrial and infrastructure solar, designed around your actual load, "
            "installed by our own teams, and maintained afterwards.",
            [("Home", "index.html"), ("Solutions", None)], bg="project-rooftop-tilt.jpg"),
        "spark": ico("spark"), "blocks": blocks,
        "components": "".join(
            '<article class="card card--glass" data-reveal><div class="card__ico">%s</div><h4>%s</h4><p>%s</p></article>'
            % (ico(i), t, d) for t, d, i in [
                ("Solar panels", "Photovoltaic modules capture sunlight and convert it into direct current (DC) "
                 "electricity. We install 620 W monocrystalline panels as standard.", "sun"),
                ("Inverter", "Most household and commercial appliances use alternating current, so the inverter "
                 "transforms DC electricity into usable AC power.", "bolt"),
                ("Battery storage", "Batteries store excess energy for use during cloudy days or at night, "
                 "ensuring uninterrupted supply. We specify lithium on virtually every system.", "battery"),
                ("MPPT charge controller", "Regulates the voltage and current coming from the solar panels to "
                 "prevent battery overcharging and maximise harvest.", "sliders"),
                ("Mounting structures", "Secure the panels in place and optimise their angle for maximum "
                 "sunlight exposure, on roof or on ground-mounted frames.", "shield"),
            ]),
        "steps": "".join(
            '<div class="step" data-reveal><div class="step__n"></div><div><h4>%s</h4><p>%s</p></div></div>'
            % (t, d) for t, d in PROCESS),
        "cta": cta_band("Not sure which solution fits your building?",
                        "Send us your appliance list on WhatsApp and our engineers will size the system, "
                        "quote it and explain exactly what it will and will not run."),
    }


# ---------------------------------------------------------------------------
# PRODUCTS
# ---------------------------------------------------------------------------
def products():
    pkgs = "".join(pkg_card(p) for p in PACKAGES)
    gallery_imgs = [
        ("install-room-stack1.jpg", "Bauman Energy hybrid inverters with lithium battery storage installed by Solar World Electric"),
        ("install-room-stack2.jpg", "Wall-mounted hybrid inverter and BICODI lithium batteries in a Nigerian installation"),
        ("install-room-stack3.jpg", "Stacked lithium battery bank and inverter installation by Solar World Electric"),
        ("install-room-dual.jpg", "Dual hybrid inverter installation with surge protection and circuit breakers"),
        ("install-room-grey.jpg", "Solar inverter and lithium battery installation in a commercial utility room"),
        ("install-deye-vertical.jpg", "Deye high-voltage battery rack installed by Solar World Electric"),
        ("pkg/pkg-25kw.jpg", "25kW high voltage Deye battery rack and inverter"),
        ("pkg/pkg-60kw.jpg", "60kW 80kVA high voltage solar inverter and battery cabinets"),
        ("product-streetlight.jpg", "All-in-one solar street light with integrated panel, lithium battery and LED head"),
        ("project-streetlight.jpg", "Solar street light illuminating a Nigerian street at night, installed by Solar World Electric"),
        ("product-waterheater.jpg", "Solar water heaters installed on a rooftop by Solar World Electric"),
        ("product-pumpctrl.jpg", "AC/DC auto solar pump controller for a solar borehole pumping system"),
    ]
    gal = "".join(
        '<figure><img src="assets/img/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>' % (i, a, a)
        for i, a in gallery_imgs
    )
    return """
%(head)s

<section class="section section--tight">
  <div class="container container--narrow">
    <div class="answer" data-reveal>
      <span class="answer__k">%(spark)s Quick answer</span>
      <p><b>What products does Solar World Electric sell?</b> Monocrystalline solar panels (620 W and 460 W),
      hybrid solar inverters from Deye, Solis and ALP Solar, lithium battery storage from 2.5 kWh to 16 kWh per
      module, MPPT charge controllers and mounting structures, plus solar water heaters, submersible pumps,
      inverter air conditioners and all-in-one solar street lights. Everything is supplied installed and
      commissioned by our own teams.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Complete packages</span>
      <h2>Our solar and inverter packages</h2>
      <p>Each package below is a complete system, inverter, lithium storage, panel array, cables, accessories
      and installation. Prices are the current published rates.</p>
    </div>
    <div class="grid grid-4">%(pkgs)s</div>
    <p class="small muted center" style="margin-top:26px">Package prices combine the inverter package and the
    matching solar package from our current charts. See the <a href="pricing.html">full pricing page</a> for
    every configuration, including inverter-only options.</p>
  </div>
</section>

<section class="section section--deep">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Components</span>
      <h2>What we supply and install</h2>
    </div>
    <div class="grid grid-3">%(components)s</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Warranty</span>
      <h2>What is covered, and for how long</h2>
    </div>
    <div class="grid grid-2" style="max-width:900px;margin-inline:auto">
      <article class="card" data-reveal>
        <span class="chip chip--gold" style="margin-bottom:14px">Deye &amp; Solis lines</span>
        <ul class="pkg__list">%(w1)s</ul>
      </article>
      <article class="card" data-reveal>
        <span class="chip" style="margin-bottom:14px">Standard line</span>
        <ul class="pkg__list">%(w2)s</ul>
      </article>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Our array of products</span>
      <h2>Installed by our own engineers</h2>
      <p>A selection of inverter and battery installations completed across Abuja, Lagos and Port Harcourt.</p>
    </div>
    <div class="gal">%(gal)s</div>
  </div>
</section>

%(cta)s
""" % {
        "head": page_head(
            "Solar panels, hybrid inverters and lithium batteries",
            "Tier-1 components from Deye, Solis and ALP Solar, supplied, installed, commissioned and "
            "warrantied by Solar World Electric Technology Ltd.",
            [("Home", "index.html"), ("Products", None)], bg="showroom-interior.jpg"),
        "spark": ico("spark"), "pkgs": pkgs,
        "components": "".join(
            '<article class="card card--glass" data-reveal><div class="card__ico">%s</div><h3>%s</h3><p>%s</p></article>'
            % (ico(i), t, d) for t, d, i in [
                ("Monocrystalline solar panels", "620 W and 460 W monocrystalline modules, the panels behind every "
                 "array we install, carrying up to a 25-year warranty.", "sun"),
                ("Hybrid solar inverters", "Deye, Solis and ALP Solar hybrid inverters from 3 kVA to 125 kW, "
                 "single-phase and three-phase, with 5-year warranty on our Deye and Solis lines.", "bolt"),
                ("Lithium battery storage", "Modules from 2.5 kWh to 16 kWh, stackable into racks with battery "
                 "management. 10-year warranty and a 10–15 year service life.", "battery"),
                ("MPPT charge controllers", "Maximum power point tracking controllers that regulate charge and "
                 "protect the battery bank from overcharging.", "sliders"),
                ("Solar street lighting", "All-in-one units with integrated PV, lithium battery, controller and "
                 "LED head. Automatic dusk-to-dawn operation, no grid connection.", "spark"),
                ("Pumps, heaters &amp; inverter ACs", "Solar submersible pumps, solar water heaters and inverter "
                 "air conditioners, supplied and installed alongside your system.", "shield"),
            ]),
        "w1": "".join('<li>%s<span>%s</span></li>' % (ico("check"), w) for w in [
            "25-year warranty on solar panels", "10-year warranty on lithium batteries",
            "5-year warranty on inverters", "1 year free after-sales service support"]),
        "w2": "".join('<li>%s<span>%s</span></li>' % (ico("check"), w) for w in [
            "20-year warranty on solar panels", "5-year warranty on lithium batteries",
            "2-year warranty on inverters", "1 year on SMF/tubular batteries and charge controllers",
            "1 year free after-sales service support"]),
        "gal": gal,
        "cta": cta_band("Want a component list for your building?",
                        "Send us what you need to run. We will specify the panels, inverter and battery bank, "
                        "and price it against our published charts."),
    }
