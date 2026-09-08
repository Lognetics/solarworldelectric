# -*- coding: utf-8 -*-
"""
Static site generator for Solar World Electric.

Run from the `site/` folder:

    python3 tools/build.py

Writes the HTML pages, robots.txt, sitemap.xml and llms.txt.
"""

import os
import re
import sys
import html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from data import COMPANY, CATEGORIES, PACKAGES, PRICE_DEYE, PRICE_SOLIS, PRICE_STANDARD, CLIENTS
from content import FAQ_GROUPS, WA_REVIEWS
from case_studies import CASES
import layout
from layout import page, breadcrumbs, local_business_schema, SITE, naira
import pages_a as A
import pages_b as B


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def write(name, content):
    path = os.path.join(ROOT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  %-22s %7.1f KB" % (name, len(content.encode("utf-8")) / 1024))


# ---------------------------------------------------------------------------
# schema builders
# ---------------------------------------------------------------------------
def faq_schema(groups):
    items = []
    for g in groups:
        for q, a in g["items"]:
            items.append({
                "@type": "Question",
                "name": strip_tags(q),
                "acceptedAnswer": {"@type": "Answer", "text": strip_tags(" ".join(a))},
            })
    return {"@type": "FAQPage", "@id": SITE + "/faq.html#faq", "mainEntity": items}


def product_schema():
    out = []
    for p in PACKAGES:
        out.append({
            "@type": "Product",
            "name": strip_tags(p["title"]),
            "image": SITE + "/assets/img/" + p["img"],
            "description": "Complete solar and inverter package: %s. Rated for %s."
                           % ("; ".join(strip_tags(s) for s in p["specs"]), strip_tags(p["loads"])),
            "brand": {"@id": SITE + "/#organization"},
            "category": "Solar power system",
            "offers": {
                "@type": "Offer",
                "price": str(p["price"]),
                "priceCurrency": "NGN",
                "availability": "https://schema.org/InStock",
                "seller": {"@id": SITE + "/#organization"},
                "url": SITE + "/pricing.html",
            },
        })
    return out


def review_schema():
    # Standalone Review nodes pointing at the organisation. We deliberately do
    # not attach a numeric reviewRating: these are WhatsApp messages, not
    # star-rated reviews, and inventing a score would misrepresent them.
    return [
        {"@type": "Review",
         "@id": SITE + "/reviews.html#review-%d" % i,
         "itemReviewed": {"@id": SITE + "/#organization"},
         "reviewBody": r["quote"],
         "author": {"@type": "Person", "name": r["who"]},
         "publisher": {"@id": SITE + "/#organization"}}
        for i, r in enumerate(WA_REVIEWS)
    ]


def case_schema():
    out = []
    for c in CASES:
        cat = next(x["label"] for x in CATEGORIES if x["key"] == c["cat"])
        text = " ".join(
            " ".join(sec[1]) if isinstance(sec[1], list) else sec[1]
            for sec in c["sections"]
        )
        out.append({
            "@type": "Article",
            "@id": SITE + "/projects.html#cs-" + c["id"],
            "headline": strip_tags(c["title"]),
            "description": strip_tags(c["excerpt"]),
            "image": SITE + "/assets/img/" + c["img"],
            "articleSection": strip_tags(cat),
            "keywords": ", ".join(c["keywords"]),
            "author": {"@id": SITE + "/#organization"},
            "publisher": {"@id": SITE + "/#organization"},
            "about": {"@type": "Thing", "name": strip_tags(c["title"])},
            "articleBody": strip_tags(text)[:1200],
        })
    return out


def service_schema():
    return [{
        "@type": "Service",
        "@id": SITE + "/solutions.html#" + c["key"],
        "serviceType": strip_tags(c["label"]) + " solar installation",
        "provider": {"@id": SITE + "/#organization"},
        "areaServed": {"@type": "Country", "name": "Nigeria"},
        "description": strip_tags(c["blurb"]),
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": strip_tags(c["label"]) + " solar systems",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t}}
                for t in c["types"]
            ],
        },
    } for c in CATEGORIES]


# ---------------------------------------------------------------------------
# blog
# ---------------------------------------------------------------------------
POSTS = [
    {
        "slug": "how-much-does-solar-cost-in-nigeria",
        "title": "How much does a solar system cost in Nigeria in 2026?",
        "excerpt": "Real published prices for every system size, what drives the number up or down, and how to "
                   "work out where your own building lands.",
        "img": "pkg/pkg-25kw.jpg",
        "alt": "Solar system pricing in Nigeria — a high voltage lithium battery rack and inverter installation",
        "cat": "Pricing",
        "body": [
            ("The short answer",
             ["A complete solar and inverter system in Nigeria costs between <b>₦1.49 million</b> and "
              "<b>₦147 million</b>, depending on what you need to run. Most family homes land between "
              "<b>₦3.5 million and ₦16 million</b> installed.",
              "That range is wide because &lsquo;solar system&rsquo; covers everything from a 3 kVA package "
              "running lights and a fridge to a 125 kW plant running chillers and industrial ovens."]),
            ("Why prices are quoted in two parts",
             ["Almost every quote you receive in Nigeria splits into an <b>inverter package</b> and a "
              "<b>solar package</b>. The inverter package is the inverter, the lithium battery, cables, "
              "accessories and installation. The solar package is the panel array, its cables, accessories and "
              "installation.",
              "This exists for a practical reason: many customers buy the inverter package first — which "
              "already ends the generator dependence for evenings and outages — and add the panel array a few "
              "months later. A 5 kVA inverter package is ₦2,820,000; the matching four-panel solar package is "
              "₦1,120,000."]),
            ("What actually drives your price",
             ["<ul>"
              "<li><b>Air conditioning.</b> This is nearly always the deciding factor. A 1.5 HP AC draws around "
              "1.25 kW while running and surges far higher on start-up.</li>"
              "<li><b>Refrigeration.</b> Fridges and freezers run day and night and set your base load, which "
              "is what the battery has to carry.</li>"
              "<li><b>How long you need power.</b> Bridging outages needs far less battery than running 24/7.</li>"
              "<li><b>Single-phase or three-phase.</b> Estate residences and commercial buildings usually need "
              "three-phase inverters.</li>"
              "<li><b>Roof or ground mount.</b> Where roof area or orientation is unsuitable, a ground-mounted "
              "array adds structure cost.</li>"
              "</ul>"]),
            ("Is it cheaper than a generator?",
             ["Over the life of the system, comfortably. A generator has a lower purchase price and an unlimited "
              "running cost. A solar system is the reverse — concentrated upfront, then effectively free.",
              "Our panels carry a 25-year warranty and our lithium batteries a 10-year warranty. A generator "
              "bought on the same day would typically have been replaced twice in that period, with fuel and "
              "servicing throughout."]),
            ("How to find your own number",
             ["Write down every appliance you want running when the grid is off, note how many air conditioners "
              "and their horsepower, and decide whether you need overnight power or only outage cover. That list "
              "is all an engineer needs.",
              "You can run it through our <a href=\"calculator.html\">solar calculator</a> for an indicative "
              "size, then check it against the <a href=\"pricing.html\">published price charts</a>."]),
        ],
    },
    {
        "slug": "what-size-solar-system-do-i-need",
        "title": "What size solar system do I need for my house?",
        "excerpt": "Inverter size, battery capacity and panel count are three different questions. Getting one "
                   "right and the others wrong is why systems fail at 3 a.m.",
        "img": "pkg/pkg-16kw.jpg",
        "alt": "Sizing a solar system for a Nigerian home — 16kW inverter with lithium battery storage",
        "cat": "Sizing",
        "body": [
            ("Three numbers, not one",
             ["People ask &lsquo;what size solar do I need?&rsquo; as though it is a single number. It is three:",
              "<ul>"
              "<li><b>Inverter size (kW)</b> — set by your peak simultaneous demand, dominated by air-conditioner "
              "start-up surge.</li>"
              "<li><b>Battery capacity (kWh)</b> — set by how much energy you use while the sun is down.</li>"
              "<li><b>Panel count (kWp)</b> — set by how fast you need that battery refilled the next day.</li>"
              "</ul>",
              "An oversized inverter with a small battery empties before morning. A large battery with too few "
              "panels never refills. Both are common, and both are avoidable."]),
            ("A practical guide by property",
             ["<ul>"
              "<li><b>3–5 kVA</b> — lights, fans, TVs, one fridge/freezer, sometimes one 1 HP AC</li>"
              "<li><b>8–10 kW</b> — a full family home with 2 fridges, 2 freezers and two to three 1.5 HP ACs</li>"
              "<li><b>12–16 kW</b> — a large home or duplex with three to five 1.5 HP ACs and a pumping machine</li>"
              "<li><b>20–30 kW</b> — an estate residence, office or small commercial building, often three-phase</li>"
              "<li><b>50 kW+</b> — hotels, schools, hospitals, warehouses and industrial facilities</li>"
              "</ul>"]),
            ("Why air conditioning decides everything",
             ["A 1.5 HP inverter AC draws roughly 1.1–1.3 kW while running. Three of them is close to 4 kW of "
              "continuous demand before you have switched on a single light.",
              "This is why we ask for the horsepower of each unit rather than just how many rooms you have. "
              "A 3 HP unit and a 1 HP unit place completely different demands on the same system — as we found "
              "on a <a href=\"projects.html#cs-16kw-residential-airbnb\">two-bedroom Airbnb</a> running two "
              "1.5 HP units and one 3 HP unit."]),
            ("Get it assessed rather than guessed",
             ["Our load assessment is free, and it is genuinely diagnostic — our engineers regularly tell "
              "customers they need less than they were about to buy.",
              "Send your appliance list on WhatsApp, or start with the <a href=\"calculator.html\">calculator</a>."]),
        ],
    },
    {
        "slug": "solar-myths-in-nigeria",
        "title": "Five myths about solar energy in Nigeria, answered",
        "excerpt": "Too expensive, only works in sunshine, wrecks your roof, needs constant maintenance — "
                   "the beliefs that keep Nigerians on diesel, examined one at a time.",
        "img": "project-rooftop-garden.jpg",
        "alt": "Solar panels installed on a Nigerian rooftop, addressing common myths about solar energy",
        "cat": "Myths",
        "body": [
            ("Myth 1: Solar is too expensive for the average Nigerian",
             ["Solar energy is becoming increasingly affordable, with financing options and payment plans "
              "available to suit different budgets. Our entry-level 3 kVA inverter package starts at ₦1,490,000, "
              "and with a 30% deposit you can start at ₦447,000 and spread the balance over up to 12 months.",
              "It is an investment that pays off over time by reducing — and eventually removing — your "
              "electricity and fuel costs."]),
            ("Myth 2: Solar panels only work in sunny climates",
             ["Solar panels can still generate power on cloudy days. While sunlight is essential, modern "
              "monocrystalline panels are designed to work efficiently in a variety of weather conditions, "
              "including the Nigerian rainy season.",
              "What matters in practice is battery sizing: storage is what carries you through a run of "
              "overcast days without touching a generator."]),
            ("Myth 3: Solar systems require too much maintenance",
             ["Solar systems require minimal maintenance. Regular cleaning of the panels so they are not "
              "obstructed by dust or dirt, plus occasional checks, is usually all that is needed to keep them "
              "functioning efficiently.",
              "There are no filters to change, no oil to top up and no fuel to buy. Every installation also "
              "includes one year of free after-sales service support."]),
            ("Myth 4: Solar panels will damage my roof",
             ["Solar panels do not damage roofs when installed properly. In fact they can protect your roof by "
              "shielding it from rain, sun and debris.",
              "Where roof condition, orientation or available area is unsuitable, we install a ground-mounted "
              "array instead — as on a recent Port Harcourt residential compound."]),
            ("Myth 5: You have to get rid of your generator",
             ["You do not. A hybrid installation integrates with your existing distribution board and your "
              "generator can stay exactly where it is as a backup.",
              "Most of our customers keep it for the first year and then notice they have stopped starting it."]),
        ],
    },
]


def blog_index():
    cards = "".join(
        '<article class="case" data-reveal><div class="case__media">'
        '<img src="assets/img/%s" alt="%s" loading="lazy"><span class="case__cat">%s</span></div>'
        '<div class="case__body"><h3>%s</h3><p class="case__excerpt">%s</p>'
        '<div class="case__foot"><a class="tlink" href="%s.html">Read the article %s</a></div>'
        '</div></article>' % (p["img"], p["alt"], p["cat"], p["title"], p["excerpt"], p["slug"],
                              layout.ico("arrow"))
        for p in POSTS
    )
    return """
%s

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Knowledge centre</span>
      <h2>Solar in Nigeria, explained</h2>
      <p>Straight, practical guidance on cost, sizing, equipment and the decisions that actually matter.</p>
    </div>
    <div class="cases">%s</div>
  </div>
</section>

%s
""" % (layout.page_head(
        "Solar knowledge centre",
        "Practical guides on solar system cost, sizing, equipment and financing in Nigeria — written by the "
        "engineers who install them.",
        [("Home", "index.html"), ("Knowledge centre", None)], bg="project-rooftop-tilt.jpg"),
       cards,
       layout.cta_band("Have a question we have not covered?",
                       "Send it to us on WhatsApp and we will answer it — and probably turn it into the next "
                       "article."))


def blog_post(p):
    body = ""
    for title, paras in p["body"]:
        body += "<h3>%s</h3>" % title
        body += "".join(x if x.startswith("<ul") else "<p>%s</p>" % x for x in paras)
    return """
%s

<section class="section">
  <div class="container container--narrow">
    <div class="media" style="margin-bottom:38px" data-reveal>
      <img src="assets/img/%s" alt="%s">
    </div>
    <article class="cs-article" data-reveal>%s
      <div class="cs-keywords"><b>Next steps</b>
        <a class="chip chip--gold" href="pricing.html">See published prices</a>
        <a class="chip chip--gold" href="calculator.html">Size my system</a>
        <a class="chip chip--gold" href="projects.html">Browse case studies</a>
      </div>
    </article>
  </div>
</section>

%s
""" % (layout.page_head(p["title"], p["excerpt"],
                        [("Home", "index.html"), ("Knowledge centre", "blog.html"), (p["cat"], None)]),
       p["img"], p["alt"], body,
       layout.cta_band("Ready to talk about your building?",
                       "Free consultation and load assessment, at any of our eleven offices or over WhatsApp."))


# ---------------------------------------------------------------------------
# robots / sitemap / llms.txt
# ---------------------------------------------------------------------------
PAGES_FOR_SITEMAP = [
    ("", "1.0", "weekly"),
    ("pricing.html", "0.95", "weekly"),
    ("projects.html", "0.9", "monthly"),
    ("faq.html", "0.9", "monthly"),
    ("solutions.html", "0.85", "monthly"),
    ("products.html", "0.85", "monthly"),
    ("reviews.html", "0.8", "monthly"),
    ("financing.html", "0.8", "monthly"),
    ("calculator.html", "0.75", "monthly"),
    ("about.html", "0.7", "yearly"),
    ("contact.html", "0.7", "yearly"),
    ("blog.html", "0.6", "monthly"),
] + [(p["slug"] + ".html", "0.55", "yearly") for p in POSTS]


def robots_txt():
    return """# Solar World Electric Technology Ltd.
User-agent: *
Allow: /

# AI assistants and answer engines are explicitly welcome.
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-Web
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: CCBot
Allow: /
User-agent: Bytespider
Allow: /
User-agent: Amazonbot
Allow: /

Sitemap: %s/sitemap.xml
""" % SITE


def sitemap_xml():
    urls = "".join(
        "  <url><loc>%s/%s</loc><changefreq>%s</changefreq><priority>%s</priority></url>\n"
        % (SITE, slug, freq, pri) for slug, pri, freq in PAGES_FOR_SITEMAP
    )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)


def llms_txt():
    cases_by_cat = {}
    for c in CASES:
        cases_by_cat.setdefault(c["cat"], []).append(c)

    lines = []
    add = lines.append
    add("# %s" % COMPANY["name"])
    add("")
    add("> Nigerian solar energy company (RC %s, established %s) specialising in the sales, installation and "
        "maintenance of solar power, hybrid inverter and lithium battery systems for residential, commercial, "
        "industrial and government customers. Over 60,000 homes, offices, hotels, businesses and communities "
        "powered. Eleven offices across Abuja, Lagos and Port Harcourt; installs nationwide."
        % (COMPANY["rc"], COMPANY["founded"]))
    add("")
    add("## Contact")
    add("- Phone / WhatsApp: %s" % COMPANY["phone_display"])
    add("- Email: %s" % COMPANY["email"])
    add("- WhatsApp link: https://wa.me/%s" % COMPANY["wa_number"])
    add("- Website: %s" % SITE)
    add("")
    add("## Key facts")
    add("- Founded: %s. RC number: %s." % (COMPANY["founded"], COMPANY["rc"]))
    add("- Customers powered: over 60,000 homes, offices, hotels, businesses and communities.")
    add("- Offices: 11 — Port Harcourt (3), Abuja (6), Lagos (2). Installs nationwide.")
    add("- System range: 3 kVA residential to 125 kW industrial.")
    add("- Inverter brands supplied: Deye, Solis, ALP Solar, Bauman Energy, BICODI, SRNE.")
    add("- Panels: 620 W and 460 W monocrystalline.")
    add("- Batteries: lithium, 2.5 kWh to 16 kWh per module, stackable racks with battery management.")
    add("- Warranty (Deye/Solis lines): 25 years panels, 10 years lithium batteries, 5 years inverters, "
        "1 year free after-sales service.")
    add("- Warranty (standard line): 20 years panels, 5 years lithium batteries, 2 years inverters.")
    add("- Installation time: within 48 hours of payment confirmation for most systems; 1–3 working days "
        "for larger commercial and industrial systems.")
    add("- Financing: 30% deposit, balance over 3/6/9/12 months, fixed 4% monthly interest, disbursed in "
        "24–48 hours.")
    add("")
    add("## Pricing (Nigerian Naira, installation included)")
    add("")
    add("Prices are quoted as an *inverter package* (inverter + lithium battery + cables + installation) and a "
        "*solar package* (panel array + cables + installation). Buying both gives a complete system.")
    add("")
    for label, rows in [("Deye systems", PRICE_DEYE), ("Solis systems", PRICE_SOLIS),
                        ("Standard systems", PRICE_STANDARD)]:
        add("### %s" % label)
        for cap, inc, app, price in rows:
            add("- **%s** — %s. Includes: %s. Rated for: %s." % (cap, naira(price), inc, app))
        add("")
    add("## Complete packages")
    for p in PACKAGES:
        add("- **%s** (%s) — %s. %s. Runs: %s."
            % (strip_tags(p["title"]), p["kw"], naira(p["price"]),
               "; ".join(strip_tags(s) for s in p["specs"]), strip_tags(p["loads"])))
    add("")
    add("## Project categories and case studies")
    for cat in CATEGORIES:
        add("### %s" % strip_tags(cat["label"]))
        add("%s Types served: %s." % (strip_tags(cat["blurb"]), ", ".join(cat["types"])))
        for c in cases_by_cat.get(cat["key"], []):
            add("- **%s** — %s Specification: %s."
                % (strip_tags(c["title"]), strip_tags(c["excerpt"]),
                   "; ".join("%s: %s" % (k, v) for k, v in c["specs"])))
        add("")
    add("## Clients")
    add(", ".join(c["name"] for c in CLIENTS) + ".")
    add("")
    add("## Frequently asked questions")
    for g in FAQ_GROUPS:
        add("### %s" % strip_tags(g["label"]))
        for q, a in g["items"]:
            add("**%s**" % strip_tags(q))
            add("")
            add(strip_tags(" ".join(a)))
            add("")
    add("## Pages")
    add("- [Home](%s/): overview, packages, case studies, reviews" % SITE)
    add("- [Pricing](%s/pricing.html): full Deye, Solis and standard price charts" % SITE)
    add("- [Projects](%s/projects.html): case studies by category" % SITE)
    add("- [FAQ](%s/faq.html): full question and answer set" % SITE)
    add("- [Solutions](%s/solutions.html): residential, commercial, industrial, infrastructure" % SITE)
    add("- [Products](%s/products.html): panels, inverters, batteries, street lights, pumps" % SITE)
    add("- [Reviews](%s/reviews.html): customer testimonials" % SITE)
    add("- [Financing](%s/financing.html): 30%% deposit payment plan" % SITE)
    add("- [Calculator](%s/calculator.html): system sizing tool" % SITE)
    add("- [Contact](%s/contact.html): all nine office addresses" % SITE)
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    print("Building Solar World Electric site…\n")

    write("index.html", page(
        slug="index.html",
        title="Solar World Electric — Solar, Inverter &amp; Battery Systems in Nigeria",
        description="Nigeria's solar energy company since 2015. Complete solar, hybrid inverter and lithium "
                    "battery systems for homes, offices, hotels, factories and communities. 60,000+ powered, "
                    "11 offices, prices published openly, financing from 30%.",
        body=A.home(), over_hero=True,
        schema=[breadcrumbs([("Home", "")])] + local_business_schema() + product_schema()
               + [faq_schema(FAQ_GROUPS[:2]), review_schema()]))

    write("about.html", page(
        slug="about.html",
        title="About Solar World Electric Technology Ltd. — Nigeria's Solar Company",
        description="Founded in 2015, Solar World Electric Technology Ltd (RC 1684774) designs, installs and "
                    "maintains solar power systems across Nigeria. Meet our team, vision and mission.",
        body=A.about(),
        schema=[breadcrumbs([("Home", ""), ("About", "about.html")])] + local_business_schema()))

    write("solutions.html", page(
        slug="solutions.html",
        title="Solar Solutions for Homes, Businesses &amp; Industry in Nigeria",
        description="Residential (5–20 kVA), commercial (20–80 kW), industrial (80–125 kW+) and infrastructure "
                    "solar solutions — street lighting, water pumping and EV charging. Sized to your load.",
        body=A.solutions(),
        schema=[breadcrumbs([("Home", ""), ("Solutions", "solutions.html")])] + service_schema()))

    write("products.html", page(
        slug="products.html",
        title="Solar Panels, Hybrid Inverters &amp; Lithium Batteries — Nigeria",
        description="Deye, Solis and ALP Solar hybrid inverters, 620W monocrystalline panels, lithium battery "
                    "storage, MPPT controllers, solar street lights and pumps — supplied and installed nationwide.",
        body=A.products(),
        schema=[breadcrumbs([("Home", ""), ("Products", "products.html")])] + product_schema()))

    write("pricing.html", page(
        slug="pricing.html",
        title="Solar System Prices in Nigeria — Full Price Charts | Solar World",
        description="Published Deye, Solis and standard solar price charts. From ₦1,490,000 for a 3 kVA "
                    "package to ₦147,190,950 for a 125 kW industrial system. Installation included, "
                    "financing from 30% deposit.",
        body=B.pricing(), og_image="assets/img/pkg/pkg-25kw.jpg",
        schema=[breadcrumbs([("Home", ""), ("Pricing", "pricing.html")])] + product_schema()
               + [faq_schema([g for g in FAQ_GROUPS if g["key"] == "cost"])]))

    write("projects.html", page(
        slug="projects.html",
        title="Solar Installation Projects &amp; Case Studies in Nigeria | Solar World",
        description="Residential, commercial, industrial and infrastructure solar case studies — system "
                    "specifications, the loads they carry and what each customer achieved. 60,000+ powered.",
        body=B.projects(), og_image="assets/img/project-ground-array-1.jpg",
        schema=[breadcrumbs([("Home", ""), ("Projects", "projects.html")])] + case_schema()))

    write("reviews.html", page(
        slug="reviews.html",
        title="Customer Reviews &amp; Testimonials | Solar World Electric Nigeria",
        description="Unedited WhatsApp messages from Solar World Electric customers across Nigeria — "
                    "homeowners, offices and businesses, weeks and years after installation.",
        body=B.reviews(), og_image="assets/img/install-room-stack1.jpg",
        schema=[breadcrumbs([("Home", ""), ("Reviews", "reviews.html")]), review_schema()]))

    write("faq.html", page(
        slug="faq.html",
        title="Solar Energy FAQ Nigeria — Cost, Sizing, Warranty &amp; Financing",
        description="Straight answers on solar system cost in Nigeria, what size you need, what it can run, "
                    "battery life, warranties, installation time and financing.",
        body=B.faq(),
        schema=[breadcrumbs([("Home", ""), ("FAQ", "faq.html")]), faq_schema(FAQ_GROUPS)]))

    write("financing.html", page(
        slug="financing.html",
        title="Solar Financing in Nigeria — 30% Deposit Payment Plan | Solar World",
        description="Pay 30% upfront and spread the balance over 3, 6, 9 or 12 months. Fixed 4% monthly "
                    "interest, no bank queues, financing disbursed in 24–48 hours.",
        body=B.financing(), og_image="assets/img/install-room-dual.jpg",
        schema=[breadcrumbs([("Home", ""), ("Financing", "financing.html")]),
                faq_schema([g for g in FAQ_GROUPS if g["key"] == "cost"])]))

    write("calculator.html", page(
        slug="calculator.html",
        title="Solar Calculator — What Size Solar System Do I Need? | Solar World",
        description="Select your appliances and get an estimate of the inverter size, battery capacity and "
                    "panel count your Nigerian home or business needs.",
        body=B.calculator(),
        schema=[breadcrumbs([("Home", ""), ("Calculator", "calculator.html")]),
                faq_schema([g for g in FAQ_GROUPS if g["key"] == "sizing"])]))

    write("contact.html", page(
        slug="contact.html",
        title="Contact Solar World Electric — 9 Offices in Abuja, Lagos &amp; Port Harcourt",
        description="Call or WhatsApp +234 906 331 5492, email solarworldes@gmail.com, or visit any of our "
                    "eleven offices across Abuja, Lagos and Port Harcourt for a free solar consultation.",
        body=B.contact(), og_image="assets/img/store-front-2.jpg",
        schema=[breadcrumbs([("Home", ""), ("Contact", "contact.html")])] + local_business_schema()))

    write("blog.html", page(
        slug="blog.html",
        title="Solar Knowledge Centre — Guides on Solar in Nigeria | Solar World",
        description="Practical guides on solar system cost, sizing, equipment and financing in Nigeria, "
                    "written by the engineers who install them.",
        body=blog_index(),
        schema=[breadcrumbs([("Home", ""), ("Knowledge centre", "blog.html")])]))

    for p in POSTS:
        write(p["slug"] + ".html", page(
            slug=p["slug"] + ".html", active="blog.html",
            title=strip_tags(p["title"]) + " | Solar World Electric",
            description=strip_tags(p["excerpt"]),
            body=blog_post(p), og_image="assets/img/" + p["img"],
            schema=[breadcrumbs([("Home", ""), ("Knowledge centre", "blog.html"),
                                 (strip_tags(p["title"]), p["slug"] + ".html")]),
                    {"@type": "Article",
                     "headline": strip_tags(p["title"]),
                     "description": strip_tags(p["excerpt"]),
                     "image": SITE + "/assets/img/" + p["img"],
                     "author": {"@id": SITE + "/#organization"},
                     "publisher": {"@id": SITE + "/#organization"}}]))

    write("robots.txt", robots_txt())
    write("sitemap.xml", sitemap_xml())
    write("llms.txt", llms_txt())

    # legacy URL kept alive
    write("blog-post.html", page(
        slug="blog-post.html", active="blog.html",
        title=strip_tags(POSTS[0]["title"]) + " | Solar World Electric",
        description=strip_tags(POSTS[0]["excerpt"]),
        body=blog_post(POSTS[0]), og_image="assets/img/" + POSTS[0]["img"]))

    print("\nDone.")


if __name__ == "__main__":
    main()
