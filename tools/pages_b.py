# -*- coding: utf-8 -*-
"""Page bodies: pricing, projects, reviews, faq, financing, calculator, contact."""

from data import (COMPANY, OFFICES, CATEGORIES, PACKAGES, WARRANTY,
                  PRICE_DEYE, PRICE_SOLIS, PRICE_STANDARD, PRICE_UPDATED)
from content import FAQ_GROUPS, WA_REVIEWS, PHOTO_REVIEWS, FINANCE_STEPS, PROCESS
from case_studies import CASES
from layout import ico, page_head, cta_band, naira
from pages_a import client_marquee, faq_block, wa_card, case_card, pkg_card


# ---------------------------------------------------------------------------
# PRICING
# ---------------------------------------------------------------------------
def _ptable(rows):
    body = "".join(
        '<tr><td class="cap">%s</td><td>%s</td><td>%s</td><td class="amt">%s</td></tr>'
        % (cap, inc, app, naira(price)) for cap, inc, app, price in rows
    )
    return """
<div class="ptable-wrap">
  <table class="ptable">
    <thead><tr><th>System capacity</th><th>What is included</th><th>Rated appliances</th><th>Price</th></tr></thead>
    <tbody>%s</tbody>
  </table>
</div>""" % body


def pricing():
    charts = [
        ("deye", "Deye systems", PRICE_DEYE, PRICE_UPDATED["deye"], WARRANTY["deye_solis"]),
        ("solis", "Solis systems", PRICE_SOLIS, PRICE_UPDATED["solis"], WARRANTY["deye_solis"]),
        ("standard", "Standard systems", PRICE_STANDARD, PRICE_UPDATED["standard"], WARRANTY["standard"]),
    ]
    tabs = "".join(
        '<button class="tab%s" type="button" role="tab" data-tab="chart-%s" aria-selected="%s">%s</button>'
        % (" is-active" if i == 0 else "", key, "true" if i == 0 else "false", label)
        for i, (key, label, _, _, _) in enumerate(charts)
    )
    panels = ""
    for i, (key, label, rows, updated, warranty) in enumerate(charts):
        wl = "".join('<li>%s<span>%s</span></li>' % (ico("check"), w) for w in warranty)
        panels += """
<div class="tabpanel" id="chart-%s"%s>
  <div class="row" style="justify-content:space-between;margin-bottom:18px">
    <h3 style="margin:0">%s price chart</h3>
    <span class="chip">Updated %s</span>
  </div>
  %s
  <div class="card" style="margin-top:24px">
    <h4>Warranty on this line</h4>
    <ul class="pkg__list" style="margin:0">%s</ul>
  </div>
</div>""" % (key, "" if i == 0 else " hidden", label, updated, _ptable(rows), wl)

    return """
%(head)s

<section class="section section--tight">
  <div class="container container--narrow">
    <div class="answer" data-reveal>
      <span class="answer__k">%(spark)s Quick answer</span>
      <p><b>How much does a solar system cost in Nigeria?</b> Solar World Electric systems range from
      <b>₦1,490,000</b> for a 3 kVA inverter package to <b>₦147,190,950</b> for a 125 kW industrial system.
      A typical Nigerian family home lands between <b>₦3.5m and ₦16m</b> installed. Prices are quoted in two
      parts, the <b>inverter package</b> (inverter, lithium battery, cables, accessories and installation) and
      the <b>solar package</b> (the panel array, cables, accessories and installation), so you can buy the
      inverter first and add panels later. Financing starts at a 30%% deposit.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Published price charts</span>
      <h2>Every system, every price, in the open</h2>
      <p>These are our current published rates, taken directly from our price charts. All prices are in Nigerian
      Naira and include installation. Prices are reviewed periodically, confirm the current rate with our team
      before ordering.</p>
    </div>
    <div class="tabs" data-tabs="#charts" role="tablist">%(tabs)s</div>
    <div id="charts">%(panels)s</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Complete packages</span>
      <h2>Popular complete systems</h2>
      <p>Inverter package plus matching solar array, combined and installed.</p>
    </div>
    <div class="grid grid-4">%(pkgs)s</div>
  </div>
</section>

<section class="section section--deep">
  <div class="container split">
    <div data-reveal="left">
      <span class="eyebrow">Financing</span>
      <h2>Start from 30%% and spread the rest</h2>
      <p class="lead" style="color:var(--d-fg-muted)">You do not need the full amount to start. Pay a 30%%
      deposit, and our financing partner covers the balance over 3, 6, 9 or 12 months with a fixed 4%% monthly
      interest added to the principal.</p>
      <div class="facts" style="margin-top:26px">
        <div><dt>On a ₦5,000,000 system</dt><dd>₦1,500,000 upfront</dd></div>
        <div><dt>Financed balance</dt><dd>₦3,500,000</dd></div>
        <div><dt>Disbursement</dt><dd>24–48 hours</dd></div>
        <div><dt>Installation</dt><dd>Immediately after</dd></div>
      </div>
      <div class="btn-row" style="margin-top:28px">
        <a class="btn btn--primary" href="financing.html">How financing works</a>
        <a class="btn btn--ghost" data-wa="Hello Solar World, I would like to apply for solar financing. Please tell me what I need.">Ask about financing</a>
      </div>
    </div>
    <div data-reveal="right">
      <div class="card card--glass">
        <h3>What decides your price</h3>
        <ul class="pkg__list" style="margin-top:16px">%(factors)s</ul>
        <a class="btn btn--primary btn--block" style="margin-top:22px" href="calculator.html">Size my system %(arrow)s</a>
      </div>
    </div>
  </div>
</section>

%(cta)s
""" % {
        "head": page_head(
            "Solar system prices in Nigeria",
            "Our full published price charts for Deye, Solis and standard solar and inverter systems, "
            "from ₦1.49m starter packages to ₦147m industrial installations. All prices include installation.",
            [("Home", "index.html"), ("Pricing", None)], bg="pkg/pkg-25kw.jpg"),
        "spark": ico("spark"), "tabs": tabs, "panels": panels,
        "pkgs": "".join(pkg_card(p) for p in PACKAGES[:4]),
        "factors": "".join('<li>%s<span>%s</span></li>' % (ico("check"), f) for f in [
            "How many air conditioners you run, and their horsepower, almost always the deciding factor",
            "Whether you need power overnight or only during outages (battery capacity)",
            "Refrigeration: fridges and freezers run continuously and set your base load",
            "Single-phase or three-phase supply",
            "Roof area and orientation, or whether a ground-mounted array is needed",
            "Whether you buy the inverter package first and add the solar array later",
        ]),
        "arrow": ico("arrow"),
        "cta": cta_band("Want a price for your exact building?",
                        "Send us your appliance list and we will size the system and quote it against these "
                        "published charts, no markup, no surprises."),
    }


# ---------------------------------------------------------------------------
# PROJECTS / CASE STUDIES
# ---------------------------------------------------------------------------
def _case_article(c):
    specs = "".join('<div><dt>%s</dt><dd>%s</dd></div>' % (k, v) for k, v in c["specs"])
    body = ""
    for sec in c["sections"]:
        title, paras = sec[0], sec[1]
        kind = sec[2] if len(sec) > 2 else "p"
        body += "<h3>%s</h3>" % title
        if kind == "list":
            body += '<ul class="pkg__list">%s</ul>' % "".join(
                '<li>%s<span>%s</span></li>' % (ico("check"), p) for p in paras)
        else:
            body += "".join("<p>%s</p>" % p for p in paras)

    quote = ""
    if c.get("quote"):
        note = ('<p class="small muted" style="margin:10px 0 0">%s</p>' % c["quote_status"]) if c.get("quote_status") else ""
        quote = '<h3>Customer experience</h3><blockquote><p>“%s”</p></blockquote>%s' % (c["quote"], note)

    kws = "".join('<span class="chip">%s</span>' % k for k in c["keywords"])
    cat_label = next(x["label"] for x in CATEGORIES if x["key"] == c["cat"])
    meta = " · ".join(filter(None, [cat_label, c["type"], c.get("location")]))

    return """
<article class="cs-article" id="cs-%s" data-reveal>
  <span class="eyebrow">%s</span>
  <h2>%s</h2>
  <p class="lead">%s</p>
  <dl class="cs-specs">%s</dl>
  <p><b>Primary loads:</b> %s</p>
  %s
  %s
  <div class="cs-keywords"><b>Related searches</b>%s</div>
</article>""" % (c["id"], meta, c["title"], c["excerpt"], specs, c["loads"], body, quote, kws)


def projects():
    counts = {}
    for c in CASES:
        counts[c["cat"]] = counts.get(c["cat"], 0) + 1

    filters = ('<button class="filter is-active" type="button" data-filter="all">All projects '
               '<span class="ct">%d</span></button>' % len(CASES))
    filters += "".join(
        '<button class="filter" type="button" data-filter="%s">%s <span class="ct">%d</span></button>'
        % (c["key"], c["label"], counts.get(c["key"], 0)) for c in CATEGORIES
    )

    cards = "".join(case_card(c) for c in CASES)

    cat_sections = ""
    for cat in CATEGORIES:
        items = [c for c in CASES if c["cat"] == cat["key"]]
        if not items:
            continue
        types = "".join('<span class="chip">%s</span>' % t for t in cat["types"])
        arts = "".join(_case_article(c) for c in items)
        cat_sections += """
<section class="section%s" id="%s">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">%s case studies</span>
      <h2>%s solar installations</h2>
      <p>%s</p>
      <div class="row" style="margin-top:16px">%s</div>
    </div>
    <div class="stack" style="gap:clamp(20px,2.6vw,32px)">%s</div>
  </div>
</section>""" % (" section--alt" if cat["key"] in ("commercial", "infrastructure") else "",
                 cat["key"], cat["label"], cat["label"], cat["blurb"], types, arts)

    return """
%(head)s

<section class="section section--tight">
  <div class="container container--narrow">
    <div class="answer" data-reveal>
      <span class="answer__k">%(spark)s Quick answer</span>
      <p><b>What kinds of solar projects has Solar World Electric completed?</b> We have powered over 60,000
      homes, offices, hotels, businesses and communities across Nigeria since 2015, in four categories:
      <b>residential</b> (homeowners, estates, duplexes, apartments and family homes), <b>commercial</b>
      (offices, hotels, schools, hospitals, shopping facilities, restaurants, warehouses and retail),
      <b>industrial</b> (factories, manufacturing and processing facilities) and <b>energy infrastructure</b>
      (solar streetlights, community projects, solar pumping and EV charging). Systems range from 5 kVA to
      125 kW.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Project index</span>
      <h2>Browse by category</h2>
      <p>Filter the index, then scroll for the full write-up of each installation, what the customer needed,
      what we recommended and installed, and what it achieved.</p>
    </div>
    <div class="filters" data-filters="#caseGrid">%(filters)s</div>
    <div class="cases" id="caseGrid">%(cards)s</div>
    <p id="noResults" hidden class="center muted" style="padding:40px 0">No projects in this category yet.</p>
  </div>
</section>

%(cats)s

%(marquee)s

%(cta)s
""" % {
        "head": page_head(
            "Solar installation projects &amp; case studies in Nigeria",
            "Residential, commercial, industrial and infrastructure solar installations, with the system "
            "specification, the loads carried and the outcome for each customer.",
            [("Home", "index.html"), ("Projects", None)], bg="project-ground-array-1.jpg"),
        "spark": ico("spark"), "filters": filters, "cards": cards, "cats": cat_sections,
        "marquee": client_marquee(dark=True, title="Some of the organisations we have powered"),
        "cta": cta_band("Want a system like one of these?",
                        "Tell us which project matches your building and we will size and price the equivalent "
                        "for you, usually within the same working day."),
    }


# ---------------------------------------------------------------------------
# REVIEWS
# ---------------------------------------------------------------------------
def reviews():
    wa_cards = "".join(wa_card(r) for r in WA_REVIEWS)
    photos = "".join(
        '<figure class="photo-card" data-reveal><img src="assets/img/%s" alt="%s" loading="lazy">'
        '<figcaption><b>%s</b>%s</figcaption></figure>' % (p["img"], p["alt"], p["title"], p["cap"])
        for p in PHOTO_REVIEWS
    )
    # Video-ready placeholders: drop MP4s into assets/video/ and swap <img> for <video>
    return """
%(head)s

<section class="section section--tight">
  <div class="container container--narrow">
    <div class="answer" data-reveal>
      <span class="answer__k">%(spark)s Quick answer</span>
      <p><b>Is Solar World Electric reliable?</b> Customers who message us months and years after installation
      report systems that are still performing. The reviews below are unedited WhatsApp conversations with real
      customers, homeowners, offices and businesses, captured during our routine post-installation check-ins.
      Names are shortened for privacy. Every installation carries warranty coverage of up to 25 years on panels,
      10 years on lithium batteries and 5 years on inverters, plus a year of free after-sales service.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">The review wall</span>
      <h2>Straight from our customers&rsquo; WhatsApp</h2>
      <p>We check in with customers weeks, months and years after installation. These are their replies.</p>
    </div>
    <div class="filters" data-filters="#reviewWall" data-empty="#noReviews" style="justify-content:center">
      <button class="filter is-active" type="button" data-filter="all">All reviews</button>
      <button class="filter" type="button" data-filter="residential">Homes</button>
      <button class="filter" type="button" data-filter="commercial">Offices &amp; business</button>
      <button class="filter" type="button" data-filter="longterm">Years later</button>
    </div>
    <div class="wall" id="reviewWall">%(wa)s</div>
    <p id="noReviews" hidden class="center muted" style="padding:30px 0">No reviews in this group yet.</p>
  </div>
</section>

<section class="section section--deep">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Installation gallery</span>
      <h2>The work behind the reviews</h2>
      <p>Photographs from completed installations across Abuja, Lagos and Port Harcourt.</p>
    </div>
    <div class="grid grid-3">%(photos)s</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Video testimonials</span>
      <h2>Customers, in their own words</h2>
      <p>Short recorded answers to the questions customers ask most before buying.</p>
    </div>
    <div class="grid grid-4">%(videos)s</div>
    <p class="small muted center" style="margin-top:22px">Video testimonials are being recorded. Drop your
    MP4 files into <code>assets/video/</code> and they will appear here.</p>
  </div>
</section>

%(cta)s
""" % {
        "head": page_head(
            "Customer reviews &amp; testimonials",
            "Unedited WhatsApp messages from Solar World Electric customers across Nigeria, homeowners, "
            "offices and businesses, weeks and years after installation.",
            [("Home", "index.html"), ("Reviews", None)], bg="install-room-stack1.jpg"),
        "spark": ico("spark"), "wa": wa_cards, "photos": photos,
        "videos": "".join(
            '<figure class="vid-card" data-reveal><img src="assets/img/%s" alt="%s" loading="lazy">'
            '<span class="vid-card__play"><span>%s</span></span><figcaption>%s</figcaption></figure>'
            % (img, alt, ico("play"), cap) for img, alt, cap in [
                ("pkg/pkg-16kw.jpg",
                 "Video testimonial about a 16kW residential solar installation in Nigeria",
                 "“How much does a solar system for a home cost?”"),
                ("pkg/pkg-50kw-a.jpg",
                 "Video testimonial about a 50kW commercial solar installation",
                 "“Can solar really run my office air conditioners?”"),
                ("project-ground-array-2.jpg",
                 "Video testimonial about a ground-mounted solar array installation",
                 "“What happens on cloudy days and in the rainy season?”"),
                ("install-deye-3batt.jpg",
                 "Video testimonial about lithium battery lifespan and warranty",
                 "“How long do the batteries actually last?”"),
            ]),
        "cta": cta_band("Join 60,000+ powered homes and businesses",
                        "Book a free consultation and load assessment at any of our 21 offices, or send us "
                        "your appliance list on WhatsApp."),
    }


# ---------------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------------
def faq():
    sections = ""
    for g in FAQ_GROUPS:
        sections += """
<section class="section%s" id="%s" data-search-group>
  <div class="container container--narrow">
    <div class="section-head">
      <span class="eyebrow">%s</span>
      <h2>%s</h2>
    </div>
    %s
  </div>
</section>""" % (" section--alt" if g["key"] in ("sizing", "equipment", "myths") else "",
                 g["key"],
                 "%d question%s" % (len(g["items"]), "" if len(g["items"]) == 1 else "s"),
                 g["label"], faq_block([g]))

    nav_chips = "".join('<a href="#%s">%s</a>' % (g["key"], g["label"]) for g in FAQ_GROUPS)

    return """
%(head)s

<section class="section section--tight">
  <div class="container container--narrow">
    <div class="searchbox" data-search="#faqAll" style="margin-bottom:22px">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
           stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input type="search" placeholder="Search all 29 questions, e.g. &quot;air conditioner&quot; or &quot;warranty&quot;"
             aria-label="Search the FAQ">
      <span class="searchbox__count"></span>
    </div>
    <nav class="pagenav" aria-label="FAQ sections">%(chips)s</nav>
    <div class="answer" data-reveal>
      <span class="answer__k">%(spark)s The three questions everyone starts with</span>
      <p><b>How much?</b> ₦1.49m for a 3 kVA starter package up to ₦147m for a 125 kW industrial system;
      most Nigerian homes fall between ₦3.5m and ₦16m installed.</p>
      <p><b>What will it run?</b> Every package from 5 kVA up is rated for air conditioning. A 16 kW system
      runs five 1.5 HP ACs alongside a full household load.</p>
      <p><b>How long does it take?</b> Installation is completed within 48 hours of payment confirmation for
      most systems; one to three working days for larger commercial and industrial installations.</p>
    </div>
  </div>
</section>

<div id="faqAll">%(sections)s</div>

%(cta)s
""" % {
        "head": page_head(
            "Solar energy FAQ for Nigeria",
            "Straight answers on solar system costs, sizing, installation, warranties, batteries, financing "
            "and the myths that stop Nigerians going solar.",
            [("Home", "index.html"), ("FAQ", None)], bg="showroom-interior.jpg"),
        "chips": nav_chips, "spark": ico("spark"), "sections": sections,
        "cta": cta_band("Still have a question?",
                        "Send it to us on WhatsApp. A real engineer answers, usually within minutes during "
                        "working hours.",
                        wa_text="Hello Solar World, I have a question about going solar: "),
    }


# ---------------------------------------------------------------------------
# FINANCING
# ---------------------------------------------------------------------------
def financing():
    steps = "".join(
        '<div class="step" data-reveal><div class="step__n"></div><div><h4>%s</h4><p>%s</p></div></div>'
        % (t, d) for t, d in FINANCE_STEPS
    )
    return """
%(head)s

<section class="section section--tight">
  <div class="container container--narrow">
    <div class="answer" data-reveal>
      <span class="answer__k">%(spark)s Quick answer</span>
      <p><b>Does Solar World offer solar financing in Nigeria?</b> Yes. Pay a <b>30%% deposit</b> and spread the
      balance over <b>3, 6, 9 or 12 months</b> through our financing partner, with a fixed <b>4%% monthly
      interest</b> added to the principal and no hidden charges. Applications are handled in-house at any of our
      21 offices, no bank queues, and approved financing is disbursed within <b>24 to 48 hours</b>, with
      installation following immediately.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container split" style="align-items:start">
    <div data-reveal="left" style="position:sticky;top:calc(var(--nav-h) + 30px)">
      <span class="eyebrow">How it works</span>
      <h2>Seven steps to a financed solar system</h2>
      <p class="lead">Whether you are a homeowner or a business owner, you can enjoy uninterrupted power supply
      from day one while spreading your payments over time.</p>
      <div class="facts" style="margin:26px 0">
        <div><dt>Deposit</dt><dd>30%%</dd></div>
        <div><dt>Terms</dt><dd>3 / 6 / 9 / 12 months</dd></div>
        <div><dt>Interest</dt><dd>Fixed 4%% monthly</dd></div>
        <div><dt>Disbursement</dt><dd>24–48 hours</dd></div>
      </div>
      <a class="btn btn--primary btn--lg" data-wa="Hello Solar World, I would like to apply for solar financing. Please tell me what I need to get started.">Apply on WhatsApp %(wa)s</a>
    </div>
    <div class="steps" data-reveal="right">%(steps)s</div>
  </div>
</section>

<section class="section section--alt" id="calculator">
  <div class="container split" style="align-items:start">
    <div data-reveal="left">
      <span class="eyebrow">Repayment estimator</span>
      <h2>See your monthly payment before you apply</h2>
      <p class="lead">Drag to your system cost and choose a term. The estimator uses our published
      terms: a 30%% deposit, with a flat 4%% of the financed balance added per month.</p>
      <div class="facts" style="margin-top:24px">
        <div><dt>Deposit</dt><dd>30%% of system cost</dd></div>
        <div><dt>Terms</dt><dd>3, 6, 9 or 12 months</dd></div>
        <div><dt>Disbursement</dt><dd>24 to 48 hours</dd></div>
      </div>
      <p class="small muted" style="margin-top:18px">Indicative. Your final terms are confirmed by our
      financing partner when your application is approved.</p>
    </div>

    <div class="card" id="repay" data-reveal="right">
      <div class="row" style="justify-content:space-between;margin-bottom:6px">
        <h3 style="margin:0">Estimate my repayments</h3>
        <span class="chip chip--gold">Live</span>
      </div>
      <div class="field" style="margin-top:18px">
        <label for="rpCost">System cost <b id="rpCostOut" class="text-gold"></b></label>
        <input class="range" type="range" id="rpCost" min="1490000" max="50000000" step="250000" value="9290000">
      </div>
      <div class="field">
        <label>Spread over</label>
        <div class="seg" id="rpTerms">
          <button type="button" data-m="3">3 months</button>
          <button type="button" data-m="6" class="is-on">6 months</button>
          <button type="button" data-m="9">9 months</button>
          <button type="button" data-m="12">12 months</button>
        </div>
      </div>
      <dl class="readout readout--total" id="rpOut" style="margin-top:18px"></dl>
      <a class="btn btn--primary btn--block" id="rpSend" style="margin-top:16px" href="#">
        Apply with these figures %(wa)s</a>
      <p class="form-note">Sends your figures to our financing team on WhatsApp.</p>
    </div>
  </div>
</section>

<section class="section section--deep">
  <div class="container container--narrow">
    <div class="card card--glass" data-reveal>
      <span class="eyebrow">Worked example</span>
      <h2 style="font-size:clamp(1.4rem,2.6vw,2rem)">A ₦5,000,000 system, financed</h2>
      <div class="facts" style="margin-top:22px;background:var(--d-hair);border-color:var(--d-hair)">
        <div style="background:rgba(255,255,255,.05)"><dt style="color:rgba(255,255,255,.6)">System cost</dt><dd style="color:#fff">₦5,000,000</dd></div>
        <div style="background:rgba(255,255,255,.05)"><dt style="color:rgba(255,255,255,.6)">Your deposit (30%%)</dt><dd style="color:#fff">₦1,500,000</dd></div>
        <div style="background:rgba(255,255,255,.05)"><dt style="color:rgba(255,255,255,.6)">Financed by partner</dt><dd style="color:#fff">₦3,500,000</dd></div>
        <div style="background:rgba(255,255,255,.05)"><dt style="color:rgba(255,255,255,.6)">Spread over</dt><dd style="color:#fff">3, 6, 9 or 12 months</dd></div>
      </div>
      <p style="margin-top:20px;color:var(--d-fg-muted)">A fixed 4%% interest is added to the principal each
      month for as long as you choose to spread the payment, so you know your total repayment from the start,
      with no hidden charges.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container--narrow">
    <div class="section-head center">
      <span class="eyebrow">The bottom line</span>
      <h2>You no longer have to wait</h2>
      <p>For years many Nigerians have wanted to switch to solar but were held back by the high initial cost.
      With our financing plan there is no huge upfront payment, just fast, hassle-free processing and flexible
      repayment options that fit your budget.</p>
    </div>
    %(faq)s
  </div>
</section>

%(cta)s
""" % {
        "head": page_head(
            "Solar financing in Nigeria: pay 30% and spread the rest",
            "Switching to solar should not be a financial burden. Pay 30% upfront and spread the balance over "
            "3, 6, 9 or 12 months, with financing disbursed in 24–48 hours.",
            [("Home", "index.html"), ("Financing", None)], bg="install-room-dual.jpg"),
        "spark": ico("spark"), "wa": ico("wa"), "steps": steps,
        "faq": faq_block([g for g in FAQ_GROUPS if g["key"] == "cost"], single=True),
        "cta": cta_band("Start with 30% today",
                        "Send us what you want to power. We will issue a pro-forma invoice and walk you "
                        "through the financing application at any of our offices.",
                        wa_text="Hello Solar World, I would like to apply for solar financing."),
    }


# ---------------------------------------------------------------------------
# CALCULATOR
# ---------------------------------------------------------------------------
def calculator():
    return """
%(head)s

<section class="section">
  <div class="container split" style="align-items:start">
    <div data-reveal="left">
      <span class="eyebrow">Solar sizing tool</span>
      <h2>Tell us what you run. We will tell you what you need.</h2>
      <p class="lead">Select your appliances and how long you run them. The calculator estimates the inverter
      size, battery capacity and panel count for your load, then gives an indicative price band from our
      published charts.</p>
      <div class="answer" style="margin-top:24px">
        <span class="answer__k">%(spark)s How sizing actually works</span>
        <p>Inverter size is set by your <b>peak simultaneous demand</b>: mostly air-conditioner start-up surge.
        Battery capacity is set by your <b>overnight energy use in kWh</b>. Panel count is set by how fast you
        need the battery refilled the next day. Getting one right and the others wrong is why undersized systems
        fail at 3 a.m.</p>
      </div>
      <div class="btn-row" style="margin-top:26px">
        <a class="btn btn--dark" href="pricing.html">See published prices</a>
        <a class="btn btn--outline" data-wa="Hello Solar World, I used your solar calculator and would like an engineer to confirm my system size.">Have an engineer confirm it</a>
      </div>
    </div>

    <div class="card" data-reveal="right" id="calc">
      <h3>Load calculator</h3>
      <p class="small muted">Enter quantities. Leave anything you do not have at zero.</p>
      <div id="calcRows" style="margin-top:18px"></div>
      <div class="field" style="margin-top:6px">
        <label for="calcHours">Hours of backup needed overnight</label>
        <select id="calcHours">
          <option value="6">6 hours (night only)</option>
          <option value="10" selected>10 hours (evening + night)</option>
          <option value="16">16 hours (most of the day)</option>
          <option value="24">24 hours (full independence)</option>
        </select>
      </div>
      <div class="facts" id="calcOut" style="margin-top:20px"></div>
      <a class="btn btn--primary btn--block" style="margin-top:18px" id="calcSend">Send this to an engineer %(wa)s</a>
      <p class="form-note">Estimates are indicative. A free site load assessment gives you the exact
      specification and price.</p>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head center">
      <span class="eyebrow">Reference</span>
      <h2>What each system size is rated for</h2>
      <p>Straight from our published price charts.</p>
    </div>
    <div class="grid grid-3">%(ref)s</div>
  </div>
</section>

%(cta)s

<script>
(function(){
  var APPLIANCES = [
    {k:'bulb',   n:'LED bulbs / lighting points', w:12,   dc:1.0},
    {k:'fan',    n:'Ceiling / standing fans',     w:75,   dc:0.6},
    {k:'tv',     n:'Television sets',             w:110,  dc:0.35},
    {k:'fridge', n:'Fridges',                     w:200,  dc:0.4},
    {k:'freezer',n:'Freezers',                    w:250,  dc:0.45},
    {k:'ac1',    n:'1 HP air conditioners',       w:900,  dc:0.55},
    {k:'ac15',   n:'1.5 HP air conditioners',     w:1250, dc:0.55},
    {k:'ac25',   n:'2.5 HP air conditioners',     w:2100, dc:0.55},
    {k:'pump',   n:'Water pumping machine',       w:750,  dc:0.1},
    {k:'wash',   n:'Washing machine',             w:500,  dc:0.08},
    {k:'micro',  n:'Microwave',                   w:1200, dc:0.05},
    {k:'office', n:'Computers / office equipment',w:150,  dc:0.5}
  ];
  var rows = document.getElementById('calcRows');
  if(!rows) return;
  APPLIANCES.forEach(function(a){
    var d = document.createElement('div');
    d.className = 'field-row';
    d.style.cssText = 'grid-template-columns:1fr 92px;align-items:center;gap:12px;margin-bottom:10px';
    d.innerHTML = '<label for="q-'+a.k+'" style="font-size:.9rem;font-weight:500">'+a.n+
      ' <span class="muted" style="font-weight:400">('+a.w+'W)</span></label>'+
      '<input id="q-'+a.k+'" type="number" min="0" step="1" value="0" style="padding:.5em .7em;text-align:center">';
    rows.appendChild(d);
  });

  var out = document.getElementById('calcOut');
  function fmt(n){ return n.toLocaleString('en-NG'); }

  function calc(){
    var peak = 0, daily = 0, list = [];
    APPLIANCES.forEach(function(a){
      var q = parseInt(document.getElementById('q-'+a.k).value || '0', 10);
      if(q > 0){
        peak  += q * a.w;
        daily += q * a.w * a.dc * 10 / 1000;   // kWh over a 10h active window
        list.push(q + ' x ' + a.n);
      }
    });
    var hours = parseInt(document.getElementById('calcHours').value, 10);
    // inverter: peak plus 30%% surge headroom, rounded to a real product size
    var sizes = [3,5,8,10,12,16,20,25,30,50,80,100,125];
    var need = peak * 1.3 / 1000;
    var inv = sizes.find(function(s){ return s >= need; }) || 125;
    // battery: overnight energy at 90%% depth of discharge
    var batt = Math.max(5, Math.ceil((peak/1000) * 0.55 * hours / 0.9));
    // panels: refill the battery plus carry daytime load, 620W panels at ~4.5 peak sun hours
    var panels = Math.max(4, Math.ceil((batt + daily) / (0.62 * 4.5)));
    out.innerHTML =
      '<div><dt>Inverter size</dt><dd>'+inv+' kW</dd></div>'+
      '<div><dt>Battery storage</dt><dd>'+fmt(batt)+' kWh</dd></div>'+
      '<div><dt>Solar panels</dt><dd>'+panels+' x 620 W</dd></div>'+
      '<div><dt>Peak demand</dt><dd>'+fmt(Math.round(peak))+' W</dd></div>';
    out.dataset.summary = list.join(', ') || 'no appliances selected';
    out.dataset.spec = inv+' kW inverter, '+batt+' kWh battery, '+panels+' x 620W panels';
  }

  rows.addEventListener('input', calc);
  document.getElementById('calcHours').addEventListener('change', calc);
  document.getElementById('calcSend').addEventListener('click', function(e){
    e.preventDefault();
    var msg = 'Hello Solar World, I used your solar calculator.\\n\\nMy appliances: '+
      (out.dataset.summary||'')+'\\nBackup needed: '+document.getElementById('calcHours').value+
      ' hours\\nEstimated system: '+(out.dataset.spec||'')+
      '\\n\\nPlease confirm the right system and price for me.';
    window.open(window.SWE.wa(msg), '_blank', 'noopener');
  });
  calc();
})();
</script>
""" % {
        "head": page_head(
            "Solar calculator: what size system do I need?",
            "Select your appliances and we will estimate the inverter size, battery capacity and panel count "
            "your property needs, with an indicative price from our published charts.",
            [("Home", "index.html"), ("Calculator", None)], bg="project-rooftop-garden.jpg"),
        "spark": ico("spark"), "wa": ico("wa"),
        "ref": "".join(
            '<article class="card" data-reveal><span class="chip chip--gold" style="margin-bottom:12px">%s</span>'
            '<p style="margin:0">%s</p></article>' % (cap, loads) for cap, loads in [
                ("5 kVA", "35 bulbs, 6 fans, 4 TVs, fridge, freezer, washing machine, one 1 HP AC and blender"),
                ("8 kW", "50 bulbs, 10 fans, 6 TVs, fridge and freezer, washing machine, two 1.5 HP ACs"),
                ("10 kW", "50 bulbs, 10 fans, 6 TVs, 2 fridges, 2 freezers, three 1.5 HP ACs, pump"),
                ("16 kW", "70 bulbs, 10 fans, 4 fridges and freezers, five 1.5 HP ACs, pump, microwave"),
                ("30 kW", "100 lighting points, 10 TVs, 3 fridges, 3 freezers, four 2.5 HP ACs, 7 kW EV charger"),
                ("125 kW", "Chillers, three-phase ACs, elevator, air compressor, industrial oven and pumps"),
            ]),
        "cta": cta_band("Prefer a person to size it?",
                        "Our engineers do a free load assessment on site or over WhatsApp, and they will tell "
                        "you if you need less than you think."),
    }


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
def contact():
    regions = {}
    for o in OFFICES:
        regions.setdefault(o["region"], []).append(o)

    office_cards = ""
    for region, items in regions.items():
        cards = "".join(
            '<article class="card" data-reveal><span class="chip chip--gold" style="margin-bottom:12px">%s</span>'
            '<h4>%s</h4><p class="small muted">%s</p>'
            '<a class="tlink" href="tel:%s">%s %s</a></article>'
            % (region, o["name"], o["address"], o["phone"].replace(" ", ""), ico("phone"), o["phone"])
            for o in items
        )
        office_cards += ('<div style="margin-bottom:40px"><h3 style="margin-bottom:20px">%s '
                         '<span class="muted" style="font-size:.6em;font-weight:500">(%d offices)</span></h3>'
                         '<div class="grid grid-3">%s</div></div>' % (region, len(items), cards))

    return """
%(head)s

<section class="section">
  <div class="container split" style="align-items:start">
    <div data-reveal="left">
      <span class="eyebrow">Reach out to us</span>
      <h2>Ready to make the switch?</h2>
      <p class="lead">Contact us today to schedule a free consultation, get expert advice, or simply learn more
      about how solar energy can benefit you.</p>

      <div class="grid grid-2" style="margin:30px 0">
        <a class="card spotlight" data-wa="">
          <div class="card__ico" style="background:rgba(37,211,102,.12);border-color:rgba(37,211,102,.3);color:#128C7E">%(wa)s</div>
          <h4>WhatsApp</h4><p class="small muted">Fastest route. Typically replies in minutes.</p>
          <span class="tlink">%(phone_display)s %(arrow)s</span>
        </a>
        <a class="card spotlight" href="tel:%(phone)s">
          <div class="card__ico">%(phoneico)s</div>
          <h4>Call us</h4><p class="small muted">Mon–Sat, 8:00am – 6:00pm.</p>
          <span class="tlink">%(phone_display)s %(arrow)s</span>
        </a>
        <a class="card spotlight" href="mailto:%(email)s">
          <div class="card__ico">%(mail)s</div>
          <h4>Email</h4><p class="small muted">For proposals, tenders and documentation.</p>
          <span class="tlink">%(email)s %(arrow)s</span>
        </a>
        <div class="card">
          <div class="card__ico">%(pin)s</div>
          <h4>Walk in</h4><p class="small muted">Branches across Abuja, Lagos and Port Harcourt.</p>
          <a class="tlink" href="#offices">See all locations %(arrow)s</a>
        </div>
      </div>
    </div>

    <div class="card" data-reveal="right">
      <h3>Book a free consultation</h3>
      <p class="small muted">Tell us what you want to power. We reply the same working day.</p>
      <form data-wa-form style="margin-top:20px">
        <div class="field-row">
          <div class="field"><label for="c-name">Full name <span class="req">*</span></label>
            <input id="c-name" name="name" required autocomplete="name" placeholder="Your name"></div>
          <div class="field"><label for="c-phone">Phone / WhatsApp <span class="req">*</span></label>
            <input id="c-phone" name="phone" type="tel" required autocomplete="tel" placeholder="0803 000 0000"></div>
        </div>
        <div class="field"><label for="c-email">Email</label>
          <input id="c-email" name="email" type="email" autocomplete="email" placeholder="you@example.com"></div>
        <div class="field-row">
          <div class="field"><label for="c-type">Property type</label>
            <select id="c-type" name="property">
              <option>Home / apartment</option><option>Duplex / estate</option><option>Office</option>
              <option>Hotel / short-stay</option><option>School</option><option>Hospital / clinic</option>
              <option>Shop / retail / restaurant</option><option>Factory / industrial</option>
              <option>Community / street lighting</option><option>Other</option>
            </select></div>
          <div class="field"><label for="c-city">City / state</label>
            <input id="c-city" name="city" placeholder="e.g. Port Harcourt"></div>
        </div>
        <div class="field"><label for="c-goal">What do you want to achieve? <span class="req">*</span></label>
          <textarea id="c-goal" name="goal" required placeholder="e.g. Run 3 ACs, a fridge, freezer, TVs and lights 24/7 without a generator."></textarea></div>
        <button class="btn btn--primary btn--block btn--lg" type="submit">Send my details %(arrow)s</button>
        <p class="form-note">Your details open in WhatsApp addressed to our team on %(phone_display)s.
        We never share your information.</p>
        <p data-wa-ok hidden class="small" style="color:var(--green);margin-top:12px">%(check)s Sent, check WhatsApp.</p>
      </form>
    </div>
  </div>
</section>

<section class="section section--alt" id="offices">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Our offices</span>
      <h2>Visit any of our locations</h2>
      <p>Our showrooms and branches across Abuja, Lagos and Port Harcourt, with nationwide
      installation. Call ahead on the number for the branch nearest you.</p>
    </div>
    %(offices)s
  </div>
</section>

%(cta)s
""" % {
        "head": page_head(
            "Contact Solar World Electric Technology Ltd.",
            "Branches across Abuja, Lagos and Port Harcourt. Call, WhatsApp, email or walk in for a free "
            "solar consultation and load assessment.",
            [("Home", "index.html"), ("Contact", None)], bg="store-front-2.jpg"),
        "wa": ico("wa"), "phoneico": ico("phone"), "mail": ico("mail"), "pin": ico("pin"),
        "arrow": ico("arrow"), "check": ico("check"),
        "phone": COMPANY["phone"], "phone_display": COMPANY["phone_display"], "email": COMPANY["email"],
        "offices": office_cards,
        "cta": cta_band("Prefer we call you?",
                        "Send your number on WhatsApp and a member of our team will call you back.",
                        wa_text="Hello Solar World, please call me back. My number is:"),
    }
