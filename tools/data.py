# -*- coding: utf-8 -*-
"""
Solar World Electric, site content.

Single source of truth for everything the generator renders into static HTML.
Edit the values here and re-run `python3 tools/build.py` from the `site/` folder.

Anything marked TODO is a placeholder that needs a real fact from the business
before it goes live. Nothing in this file should ever be invented.
"""

# ---------------------------------------------------------------------------
# COMPANY
# ---------------------------------------------------------------------------
COMPANY = {
    "name": "Solar World Electric Technology Ltd.",
    "short": "Solar World",
    "legal": "Solar World Electric Technology Limited",
    "rc": "1684774",
    "founded": "2015",
    "domain": "https://solarworldelectric.vercel.app",
    "canonical_domain": "https://www.solarworldelectric.com",
    "phone": "+2349063315492",
    "phone_display": "+234 906 331 5492",
    "email": "solarworldes@gmail.com",
    "wa_number": "2349063315492",
    "wa_default": ("Hello Solar World, I am interested in getting your solar and inverter "
                   "package. Please may I know how to proceed?"),
    "tagline": "Power you can always count on.",
    "vision": ("To be the leading name in the provision of solar and renewable energy "
               "solutions in Nigeria and Africa at large."),
    "mission": ("To keep investing assiduously in research and development in clean and green "
                "energy solutions that will deliver dependable power for customers all around "
                "the continent. We aim to deepen as well as encourage increased usage of solar "
                "power solutions in Africa."),
    "belief": ("At Solar World, we believe who you buy from is as important, if not more "
               "important than the product itself."),
    "powered": "60,000+",
}

STATS = [
    {"n": 60000, "suffix": "+", "label": "Homes, offices, hotels,<br>businesses &amp; communities powered"},
    {"n": None,  "suffix": "",  "label": "Offices across Abuja,<br>Lagos &amp; Port Harcourt"},  # filled from OFFICES below
    {"n": 10,    "suffix": "+", "label": "Years designing and installing<br>solar in Nigeria"},
    {"n": 48,    "suffix": "hr", "label": "Typical installation turnaround<br>after payment confirmation"},
]

# ---------------------------------------------------------------------------
# OFFICES  (from the company profile, page 27)
# ---------------------------------------------------------------------------
OFFICES = [
    {"region": "Port Harcourt", "name": "Sani Abacha 1 & 2",
     "address": "No 27 & 29 Sani Abacha Road, GRA Phase 3, Opposite the Autograph Mall, Port Harcourt",
     "phone": "09037933268"},
    {"region": "Port Harcourt", "name": "SPA PH",
     "address": "1st Floor, Port-Harcourt City Mall (SPAR), Old GRA, Port Harcourt",
     "phone": "07089970508"},
    {"region": "Port Harcourt", "name": "GRA PH",
     "address": "The Basement, Market Square, GRA Phase 2, Port Harcourt",
     "phone": "07046652713"},
    {"region": "Abuja", "name": "Jabi",
     "address": "First Floor, The Entrance, Jabi Lake Mall, Abuja",
     "phone": "08143333769"},
    {"region": "Abuja", "name": "Wuse 2",
     "address": "M.I Ahmad Plaza, 109 Adetokunbo Ademola Crescent, Wuse 2, Abuja",
     "phone": "09069266461"},
    {"region": "Abuja", "name": "Silverbird CBD (First Floor)",
     "address": "First Floor, Silverbird Entertainment Center, Central Business District, Abuja",
     "phone": "08081567225"},
    {"region": "Abuja", "name": "Silverbird CBD (Basement)",
     "address": "The Basement, Silverbird Entertainment Center, Central Business District, Abuja",
     "phone": "08134825475"},
    {"region": "Abuja", "name": "Solar Xperience Hive",
     "address": "The Basement, Ceddi Plaza, Central Business District, Abuja",
     "phone": "07019276763"},
    {"region": "Abuja", "name": "Gwarinpa",
     "address": "The Ground Floor, Primus Mall, First Avenue, Gwarinpa, Abuja",
     "phone": "+234 911 165 9493"},
    {"region": "Lagos", "name": "Lekki Phase 1",
     "address": "No. 26 Emmanuel Abimbola Cole, off Fola Osibo Street, Lekki Phase 1, Lagos",
     "phone": "09132699677"},
    {"region": "Lagos", "name": "The Circle Mall, Jakande",
     "address": "The Circle Mall, Jakande, 5th Roundabout, Lekki-Epe Expressway, Lagos",
     "phone": "08030675493"},
]

# ---------------------------------------------------------------------------
# CLIENTS  (logos: profile page 23 + logos supplied by the business)
# ---------------------------------------------------------------------------
CLIENTS = [
    {"name": "Woodhall Capital",   "file": "woodhall-capital.svg", "sector": "Financial services"},
    {"name": "The Brook Finance Company Limited", "file": "brook-finance.png", "sector": "Financial services"},
    {"name": "GIG Logistics",      "file": "gig-logistics.png",    "sector": "Logistics"},
    {"name": "NDDC",               "file": "nddc.png",             "sector": "Government"},
    {"name": "ENERGYMATICS LTD.",  "file": "energymatics.png",     "sector": "Energy services"},
    {"name": "Garden City Hotel",  "file": "garden-city-hotel.png","sector": "Hospitality"},
    {"name": "Stratford Hotels",   "file": "stratford-hotels.png", "sector": "Hospitality"},
    {"name": "Flinx Realty Ltd",   "file": "flinx-realty.png",     "sector": "Real estate"},
    {"name": "NEXT Cash & Carry",  "file": "next-cash-carry.jpg",  "sector": "Retail"},
    {"name": "Maritime Academy of Nigeria, Oron", "file": "maritime-academy.png", "sector": "Education"},
    {"name": "Hallel College",     "file": "hallel-college.png",   "sector": "Education"},
    {"name": "EngenderHealth",     "file": "engenderhealth.png",   "sector": "Healthcare NGO"},
    {"name": "Riders for Health",  "file": "riders-for-health.png","sector": "Healthcare logistics"},
    {"name": "National Malaria Elimination Programme", "file": "nmep.png", "sector": "Federal Ministry of Health"},
    {"name": "Nigerian Army",      "file": "nigerian-army.png",    "sector": "Defence"},
    {"name": "Rhythm FM",          "file": "rhythm-fm.png",        "sector": "Broadcast media"},
    {"name": "SSTV",               "file": "sstv.png",             "sector": "Broadcast media"},
    {"name": "The Redeemed Christian Church of God", "file": "rccg.jpg", "sector": "Faith organisation"},
]

# ---------------------------------------------------------------------------
# PRICE CHARTS, verbatim from the three supplied PDFs
# ---------------------------------------------------------------------------
PRICE_UPDATED = {
    "deye": "7 August 2026",
    "solis": "24 July 2026",
    "standard": "4 August 2026",
}

# rows: (capacity, what's included, appliances it is rated for, price NGN)
PRICE_DEYE = [
    ("5kW / 48V Inverter package",
     "1 lithium battery of 5kWh, electric cable, accessories & installation",
     "40 bulbs, 6 fans, 5 television sets, 1 standard fridge, freezer, washing machine, two 1HP ACs & electric blender",
     3500000),
    ("5kW / 48V Solar package",
     "4 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 1260000),
    ("5kWh / 48V Inverter package",
     "2 lithium batteries of 5kWh, electric cable, accessories & installation",
     "40 bulbs, 6 fans, 5 television sets, 1 fridge, 2 freezers, washing machine, two 1HP ACs & pumping machine, microwave & electric blender",
     5150000),
    ("5kW / 48V Solar package",
     "8 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 2070000),
    ("8kW / 48V Inverter package",
     "1 lithium battery of 12kWh, electric cables, accessories & installation",
     "50 bulbs, 10 fans, 6 television sets, 1 standard fridge, freezer, washing machine & two 1.5HP ACs & electric blender",
     6020000),
    ("8kW / 48V Solar package",
     "8 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 2190000),
    ("10kW / 48V Inverter package",
     "1 lithium battery of 16kWh, electric cable, accessories & installation",
     "50 bulbs, 10 fans, 6 television sets, 2 fridges, 2 freezers, washing machine, three 1.5HP ACs & pumping machine, microwave & electric blender",
     7000000),
    ("10kW / 48V Solar package",
     "8 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 2290000),
    ("12kW / 48V Inverter package",
     "2 lithium batteries of 16kWh, electric cable, accessories & installation",
     "70 bulbs, 10 fans, 3 fridges and freezers, washing machine, three 1.5HP ACs, pumping machine, microwave & electric blender",
     10720000),
    ("12kW / 48V Solar package",
     "16 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 3940000),
    ("16kW / 48V Inverter package",
     "2 lithium batteries of 16kWh, electric cable, accessories & installation",
     "70 bulbs, 10 fans, 4 fridges and freezers, washing machine, five 1.5HP ACs, pumping machine, microwave & electric blender",
     11540000),
    ("16kW / 48V Solar package",
     "20 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 4820000),
    ("20kW / 48V Three-phase inverter package",
     "3 lithium batteries of 16kWh, electric cable, accessories & installation",
     "80 bulbs, 10 fans, 5 fridges and freezers, washing machine, six 1.5HP ACs, pumping machine, microwave & electric blender",
     16660000),
    ("20kW / 48V Solar package",
     "24 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 5850000),
    ("25kW / 48V High-VAC full package",
     "7 × 5.12kWh lithium batteries, 28 × 620W panels, stackable battery rack, battery management system, "
     "electric cables and circuit breaker, solar combiner box, solar mounting rack and busbar, installation, logistics and accessories",
     "90 lighting points, 8 TVs, 2 fridges, 2 freezers, electric iron, 6kW EV charger, pumping machine, "
     "3 units of 2.5HP air conditioner, microwave, electric blender & washing machine",
     29120000),
    ("30kW / 48V High-VAC full package",
     "7 × 7.68kWh lithium batteries, 36 × 620W panels, stackable battery rack, battery management system, "
     "electric cables and circuit breaker, solar combiner box, solar mounting rack and busbar, installation, logistics and accessories",
     "100 lighting points, 10 TVs, 3 fridges, 3 freezers, 7kW EV charger, pumping machine, "
     "4 units of 2.5HP air conditioner, washing machine",
     35990000),
    ("50kW / 48V High-VAC full package",
     "5 × 14.3kWh BOS-B lithium batteries, 64 × 620W panels, battery management system, electric cables and circuit breaker, "
     "solar combiner box, solar mounting rack and busbar, installation, logistics and accessories",
     "120 lighting points, 20 TVs, 4 fridges, 4 freezers, pumping machine, EV charger, "
     "5 units of 2.5HP air conditioner, washing machine",
     47660000),
    ("80kW / 48V High-VAC full package",
     "7 × 14.3kWh BOS-B lithium batteries, 78 × 620W panels, battery management system, electric cables and circuit breaker, "
     "solar combiner box, solar mounting rack and buss bar, installation, logistics and accessories",
     "150 lighting points, 30 TVs, 5 fridges and 5 freezers, pumping machine, "
     "7 units of 2.5HP air conditioner, washing machine",
     68080000),
    ("100kW / 48V High-VAC full package",
     "10 × 14.3kWh BOS-B lithium batteries, 140 × 620W panels, battery management system, electric cables and circuit breaker, "
     "solar combiner box, solar mounting rack and buss bar, installation, logistics and accessories",
     "180 lighting points, 40 TVs, 6 fridges and 6 freezers, pumping machine, "
     "8 units of 2.5HP air conditioner, washing machine",
     107570950),
    ("125kW Full package",
     "15 × 16kWh BOS-B Pro lithium batteries, 168 × 620W panels, battery rack, battery management system, "
     "electric cables and circuit breaker, solar combiner box, solar mounting rack and buss bar, installation, logistics and accessories",
     "Chillers, 3-phase air conditioners, elevator, air compressor, industrial water heater, "
     "industrial oven, industrial pumping machine, EV charging station",
     147190950),
]

PRICE_SOLIS = [
    ("5kWh / 48V Inverter package",
     "1 lithium battery of 14.3kWh, electric cables, accessories & installation",
     "50 bulbs, 10 fans, 6 television sets, 2 fridges, 2 freezers, washing machine, two 1.5HP ACs & pumping machine, microwave & electric blender",
     4800000),
    ("5kW / 48V Solar package",
     "8 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 2070000),
    ("12kW / 48V Inverter package",
     "2 lithium batteries of 14.3kWh, electric cables, accessories & installation",
     "70 bulbs, 10 fans, 3 fridges and freezers, washing machine, three 1.5HP ACs, pumping machine, microwave & electric blender",
     10520000),
    ("12kW / 48V Solar package",
     "16 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 3940000),
    ("16kW / 48V Inverter package",
     "2 lithium batteries of 16kWh, electric cables, accessories & installation",
     "70 bulbs, 10 fans, 4 fridges and freezers, washing machine, five 1.5HP ACs, pumping machine, microwave & electric blender",
     11740000),
    ("16kW / 48V Solar package",
     "20 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 4820000),
    ("18kW / 48V Inverter package",
     "3 lithium batteries of 14.3kWh, electric cables, accessories & installation",
     "80 bulbs, 10 fans, 5 fridges and freezers, washing machine, six 1.5HP ACs, pumping machine, microwave & electric blender",
     14860000),
    ("18kW / 48V Solar package",
     "24 × 620W monocrystalline solar panels, cables, accessories & installation",
     "Same as above", 5850000),
    ("30kW / 48V High-VAC full package",
     "7 × 5.12kWh lithium batteries, 28 × 620W panels, stackable battery rack, battery management system, "
     "electric cables and circuit breaker, solar combiner box, solar mounting rack and busbar, installation, logistics and accessories",
     "90 lighting points, 8 TVs, 2 fridges, 2 freezers, electric iron, 6kW EV charger, pumping machine, "
     "3 units of 2.5HP air conditioner, microwave, electric blender & washing machine",
     27720000),
    ("50kW / 48V High-VAC full package",
     "5 × 14.3kWh lithium batteries, 64 × 620W panels, stackable battery rack, battery management system, "
     "electric cables and circuit breaker, solar combiner box, solar mounting rack and busbar, installation, logistics and accessories",
     "120 lighting points, 20 TVs, 4 fridges, 4 freezers, pumping machine, EV charger, "
     "5 units of 2.5HP air conditioner, washing machine",
     44060000),
    ("50kW / 48V High-VAC full package (extended array)",
     "7 × 14.3kWh lithium batteries, 84 × 620W panels, stackable battery rack, battery management system, "
     "electric cables and circuit breaker, solar combiner box, solar mounting rack and busbar, installation, logistics and accessories",
     "120 lighting points, 20 TVs, 4 fridges, 4 freezers, pumping machine, EV charger, "
     "5 units of 2.5HP air conditioner, washing machine",
     55860000),
    ("125kW PCS Full package",
     "15 × 14.3kWh lithium batteries, 168 × 620W panels, stackable battery rack, battery management system, "
     "installation, logistics and accessories",
     "Chillers, 3-phase air conditioners, elevator, air compressor, industrial water heater, "
     "industrial oven, industrial pumping machine, EV charging station",
     100020000),
]

PRICE_STANDARD = [
    ("3kVA / 24V Inverter package only",
     "1 lithium battery of 2.5kWh, electric cables, accessories & installation",
     "25 bulbs, 4 fans, 2 television sets, 1 standard fridge/freezer & electric blender", 1490000),
    ("3kVA / 24V Solar package only",
     "4 × 460W monocrystalline solar panels, cables, accessories & installation", "Same as above", 860000),
    ("3.3kVA / 24V Inverter package only",
     "1 lithium battery of 2.5kWh, electric cables, accessories & installation",
     "25 bulbs, 4 fans, 2 television sets, 1 standard fridge/freezer & electric blender", 1840000),
    ("3.3kVA / 24V Solar package only",
     "4 × 460W monocrystalline solar panels, cables, accessories & installation", "Same as above", 880000),
    ("4.2kVA / 24V Hybrid inverter package only",
     "1 lithium battery of 7.12kWh, electric cables, accessories & installation",
     "30 bulbs, 5 fans, 3 television sets, 1 standard fridge & freezer, washing machine & electric blender", 2760000),
    ("4.2kVA / 24V Solar package only",
     "6 × 460W monocrystalline solar panels, cables, accessories & installation", "Same as above", 1300000),
    ("5kVA / 48V Inverter package only",
     "1 lithium battery of 5kWh, electric cables, accessories & installation",
     "35 bulbs, 6 fans, 4 television sets, 1 standard fridge, freezer, washing machine & one 1HP AC & electric blender", 2820000),
    ("5kVA / 48V Solar package only",
     "4 × 620W monocrystalline solar panels, cables, accessories & installation", "Same as above", 1120000),
    ("5kVA / 48V Inverter package only (large storage)",
     "1 lithium battery of 15.33kWh, electric cables, accessories & installation",
     "35 bulbs, 6 fans, 4 television sets, 1 standard fridge, freezer, washing machine & one 1HP AC & electric blender", 4300000),
    ("5kVA / 48V Solar package only (large array)",
     "8 × 620W monocrystalline solar panels, cables, accessories & installation", "Same as above", 1880000),
    ("6kW (7.5kVA), ALP solar hybrid inverter only",
     "1 lithium battery of 16kWh, electric cables, accessories & installation",
     "40 bulbs, 6 fans, 5 television sets, 1 standard fridge, freezer, washing machine & one 1HP AC & electric blender", 4750000),
    ("6kW (7.5kVA), ALP solar package only",
     "12 × 620W monocrystalline solar panels, cables, accessories & installation", "Same as above", 2830000),
    ("8kW ALP solar hybrid inverter package only",
     "1 lithium battery of 16kWh, electric cables, accessories & installation",
     "50 bulbs, 10 fans, 6 television sets, 2 fridges, 2 freezers, washing machine, three 1.5HP ACs & pumping machine, microwave & electric blender", 5300000),
    ("8kW ALP solar package only",
     "12 × 620W monocrystalline solar panels, cables, accessories & installation", "Same as above", 2930000),
    ("11kW / 48V ALP solar hybrid only",
     "2 lithium batteries of 16kWh, electric cables, accessories & installation",
     "50 bulbs, 10 fans, 6 television sets, 2 fridges, 2 freezers, washing machine, three 1.5HP ACs & pumping machine, microwave & electric blender", 9000000),
    ("11kW / 48V Solar package only",
     "24 × 620W monocrystalline solar panels, cables & installation", "Same as above", 5210000),
    ("15kVA / 48V Hybrid inverter only",
     "2 lithium batteries of 16kWh, electric cables, accessories & installation",
     "70 bulbs, 10 fans, 3 fridges and freezers, washing machine, four 1.5HP ACs, pumping machine, microwave, electric blender", 10150000),
    ("15kVA / 48V Solar package only",
     "24 × 620W monocrystalline solar panels, cables & installation", "Same as above", 5410000),
    ("15kVA / 48V Hybrid inverter package only (17.6kWh cells)",
     "2 lithium batteries of 17.6kWh, electric cables, accessories & installation",
     "70 bulbs, 10 fans, 3 fridges and freezers, washing machine, four 1.5HP ACs, pumping machine, microwave & electric blender", 11450000),
    ("30kVA / 48V Hybrid inverter package only",
     "4 lithium batteries of 17.6kWh, electric cables, accessories & installation",
     "90 bulbs, 15 fans, 5 fridges and freezers, washing machine, six 1.5HP ACs, pumping machine, microwave & electric blender", 22900000),
    ("30kVA / 48V Solar package only",
     "48 × 620W monocrystalline solar panels, cables & installation", "Same as above", 10520000),
]

WARRANTY = {
    "deye_solis": [
        "10-year warranty on lithium batteries",
        "25-year warranty on solar panels",
        "5-year warranty on inverters",
        "1 year free after-sales service support",
    ],
    "standard": [
        "5-year warranty on lithium batteries",
        "20-year warranty on solar panels",
        "1 year free after-sales service support",
    ],
}

# ---------------------------------------------------------------------------
# FEATURED PACKAGES (home + products): image files live in assets/img/pkg/
# ---------------------------------------------------------------------------
PACKAGES = [
    {"kw": "8kW / 48V", "title": "8kW Complete Solar &amp; Inverter System",
     "img": "pkg/pkg-8kw.jpg", "tag": "Family home",
     "alt": "8kW 48V complete solar and inverter system installed by Solar World Electric in Nigeria",
     "specs": ["1 × 12kWh lithium battery", "8 × 620W monocrystalline panels", "Deye hybrid inverter"],
     "loads": "50 bulbs · 10 fans · 6 TVs · fridge &amp; freezer · washing machine · two 1.5HP ACs",
     "price": 8210000, "note": "Inverter + solar package, installed"},
    {"kw": "10kW (12.5kVA)", "title": "10kW Complete Solar &amp; Inverter Package",
     "img": "pkg/pkg-10kw.jpg", "tag": "Duplex",
     "alt": "10kW 12.5kVA 48V complete solar and inverter package for a Nigerian home",
     "specs": ["1 × 16kWh lithium battery", "8 × 620W monocrystalline panels", "Deye hybrid inverter"],
     "loads": "50 bulbs · 10 fans · 6 TVs · 2 fridges · 2 freezers · three 1.5HP ACs",
     "price": 9290000, "note": "Inverter + solar package, installed"},
    {"kw": "12kW (15kVA)", "title": "12kW Complete Solar &amp; Inverter Package",
     "img": "pkg/pkg-12kw.jpg", "tag": "Large home",
     "alt": "12kW 15kVA 48V complete solar and inverter package with lithium battery storage",
     "specs": ["2 × 16kWh lithium batteries", "16 × 620W monocrystalline panels", "Deye hybrid inverter"],
     "loads": "70 bulbs · 10 fans · 3 fridges &amp; freezers · three 1.5HP ACs · pumping machine",
     "price": 14660000, "note": "Inverter + solar package, installed"},
    {"kw": "16kW (20kVA)", "title": "16kW Complete Solar &amp; Inverter Package",
     "img": "pkg/pkg-16kw.jpg", "tag": "Home &amp; short-stay",
     "alt": "16kW 20kVA 48V solar inverter installation for a home and short-stay apartment",
     "specs": ["2 × 16kWh lithium batteries", "20 × 620W monocrystalline panels", "Deye hybrid inverter"],
     "loads": "70 bulbs · 10 fans · 4 fridges &amp; freezers · five 1.5HP ACs · pumping machine",
     "price": 16360000, "note": "Inverter + solar package, installed"},
    {"kw": "20kW / 48V", "title": "20kW Complete Solar &amp; Inverter System",
     "img": "pkg/pkg-20kw-a.jpg", "tag": "Office / three-phase",
     "alt": "20kW three-phase solar and inverter system for offices installed in Nigeria",
     "specs": ["3 × 16kWh lithium batteries", "24 × 620W monocrystalline panels", "Three-phase hybrid inverter"],
     "loads": "80 bulbs · 10 fans · 5 fridges &amp; freezers · six 1.5HP ACs · pumping machine",
     "price": 22510000, "note": "Inverter + solar package, installed"},
    {"kw": "25kW / 48V", "title": "25kW High-Voltage Solar &amp; Inverter System",
     "img": "pkg/pkg-25kw.jpg", "tag": "Commercial",
     "alt": "25kW high voltage solar and inverter system with stackable lithium battery rack",
     "specs": ["7 × 5.12kWh HV lithium batteries", "28 × 620W monocrystalline panels", "Stackable rack + BMS"],
     "loads": "90 lighting points · 8 TVs · 6kW EV charger · three 2.5HP ACs",
     "price": 29120000, "note": "Complete high-VAC package, installed"},
    {"kw": "50kW / 48V", "title": "50kW Complete Solar &amp; Inverter System",
     "img": "pkg/pkg-50kw-a.jpg", "tag": "Hotel / large office",
     "alt": "50kW complete solar and inverter system for a hotel or large commercial building",
     "specs": ["5 × 14.3kWh BOS-B lithium batteries", "64 × 620W monocrystalline panels", "Combiner box + BMS"],
     "loads": "120 lighting points · 20 TVs · 4 fridges · 4 freezers · EV charger · five 2.5HP ACs",
     "price": 47660000, "note": "Complete high-VAC package, installed"},
    {"kw": "80kW (100kVA)", "title": "80kW High-Voltage Solar &amp; Inverter System",
     "img": "pkg/pkg-80kw.jpg", "tag": "Industrial",
     "alt": "80kW 100kVA high voltage solar and inverter system for industrial facilities in Nigeria",
     "specs": ["7 × 14.3kWh BOS-B lithium batteries", "78 × 620W monocrystalline panels", "Dual inverter bank"],
     "loads": "150 lighting points · 30 TVs · 5 fridges &amp; 5 freezers · seven 2.5HP ACs",
     "price": 68080000, "note": "Complete high-VAC package, installed"},
]

# ---------------------------------------------------------------------------
# CASE STUDY CATEGORIES
# ---------------------------------------------------------------------------
CATEGORIES = [
    {"key": "residential", "label": "Residential",
     "blurb": "Homeowners, estates, duplexes, apartments and family homes.",
     "types": ["Homeowner", "Estate", "Duplex", "Apartment", "Family home"]},
    {"key": "commercial", "label": "Commercial",
     "blurb": "Offices, hotels, schools, hospitals, shopping facilities, restaurants, warehouses and retail businesses.",
     "types": ["Office", "Hotel", "School", "Hospital", "Shopping facility", "Restaurant", "Warehouse", "Retail business"]},
    {"key": "industrial", "label": "Industrial",
     "blurb": "Factories, manufacturing plants, processing facilities and large-scale sites.",
     "types": ["Factory", "Manufacturing", "Processing facility", "Large-scale facility"]},
    {"key": "infrastructure", "label": "Energy &amp; Infrastructure",
     "blurb": "Solar streetlights, community projects, solar pumping and EV charging.",
     "types": ["Solar streetlights", "Community projects", "Solar pumping", "EV charging"]},
]

# Office count stated by the business. OFFICES below holds the addresses we
# have on file (from the company profile); the rest are still to be supplied,
# which is why the two numbers differ.
OFFICE_COUNT = 21

for _s in STATS:
    if _s["n"] is None:
        _s["n"] = OFFICE_COUNT
