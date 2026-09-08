# -*- coding: utf-8 -*-
"""
Solar World Electric, FAQs, reviews and reusable copy.

The FAQ set is the core AI-answer asset: each answer is written to stand alone
as a complete response to the question, because that is how an LLM will quote it.
"""

# ---------------------------------------------------------------------------
# FAQS, grouped. Every answer must be self-contained and factual.
# ---------------------------------------------------------------------------
FAQ_GROUPS = [
    {
        "key": "cost",
        "label": "Cost &amp; pricing",
        "items": [
            ("How much does a solar system cost in Nigeria?",
             ["A complete solar and inverter system from Solar World Electric Technology Ltd. ranges from "
              "about <b>₦1.49 million</b> for a 3 kVA inverter package up to <b>₦147 million</b> for a 125 kW "
              "industrial system. Typical Nigerian homes fall between <b>₦3.5 million and ₦16 million</b> "
              "installed, depending on how many air conditioners and refrigeration units the system has to carry.",
              "Prices are quoted in two parts, the <b>inverter package</b> (inverter, lithium battery, cables, "
              "accessories and installation) and the <b>solar package</b> (the panel array, cables, accessories and "
              "installation). Many customers buy the inverter package first and add the solar array later. "
              "Our full published price charts are on the <a href=\"pricing.html\">pricing page</a>."]),
            ("How much does a 5kVA solar system cost in Nigeria?",
             ["A 5 kVA / 48 V inverter package with one 5 kWh lithium battery, cables, accessories and installation "
              "is <b>₦2,820,000</b>. The matching 4-panel 620 W solar package is <b>₦1,120,000</b>, making a complete "
              "5 kVA solar and inverter system approximately <b>₦3,940,000</b> installed.",
              "A larger-storage version using a 15.33 kWh lithium battery is ₦4,300,000 for the inverter package "
              "and ₦1,880,000 for an 8-panel array. A 5 kVA system is rated for around 35 bulbs, 6 fans, "
              "4 television sets, a standard fridge, a freezer, a washing machine, one 1 HP air conditioner "
              "and an electric blender."]),
            ("How much does a 10kW solar system cost?",
             ["A 10 kW / 48 V Deye inverter package with a 16 kWh lithium battery is <b>₦7,000,000</b>, and the "
              "matching 8-panel 620 W solar package is <b>₦2,290,000</b>: approximately <b>₦9,290,000</b> for the "
              "complete installed system.",
              "A 10 kW system is rated for 50 bulbs, 10 fans, 6 television sets, 2 fridges, 2 freezers, a washing "
              "machine, three 1.5 HP air conditioners, a pumping machine, microwave and electric blender. "
              "It suits a duplex or a large family home."]),
            ("Is solar cheaper than a generator in Nigeria?",
             ["Over the life of the system, yes. A generator has a lower purchase price but an unlimited running "
              "cost, fuel, servicing, parts and eventual replacement, and it only produces power while you are "
              "paying for fuel.",
              "A solar system is the opposite: the cost is concentrated upfront, and generation afterwards is "
              "effectively free. Our panels carry a 25-year warranty and our lithium batteries a 10-year warranty, "
              "so the system keeps producing long after a generator bought at the same time would have been "
              "replaced twice.",
              "There are also costs a generator carries that never appear on an invoice: noise, fumes, the "
              "maintenance burden and the risk of being without power when fuel is unavailable."]),
            ("Do you offer payment plans or solar financing?",
             ["Yes. Through our financing partner you pay a <b>30% deposit</b> and spread the remaining balance over "
              "<b>3, 6, 9 or 12 months</b>, with a fixed 4% monthly interest added to the principal.",
              "For example, on a ₦5 million system you pay ₦1.5 million upfront and the financing partner covers "
              "the remaining ₦3.5 million. There are no bank queues: our in-house financing team handles the "
              "process at any of our offices, approved financing is disbursed within <b>24 to 48 hours</b>, and "
              "installation follows immediately."]),
            ("Can I pay in instalments and still get installed quickly?",
             ["Yes. Once your financing application is approved and disbursed, typically within 24 to 48 hours, "
              "installation is scheduled straight away. You do not wait until the instalments are complete. "
              "Most installations are finished within 48 hours of payment confirmation, and larger systems within "
              "one to three working days."]),
        ],
    },
    {
        "key": "sizing",
        "label": "Sizing &amp; what it powers",
        "items": [
            ("What size solar system do I need for my house?",
             ["System size is decided by what you want to run and for how long, not by the size of the building. "
              "As a practical guide, based on our published packages:",
              "<ul>"
              "<li><b>3–5 kVA</b>: lights, fans, TVs, one fridge/freezer, sometimes one 1 HP air conditioner</li>"
              "<li><b>8–10 kW</b>: a full family home with 2 fridges, 2 freezers and two to three 1.5 HP ACs</li>"
              "<li><b>12–16 kW</b>: a large home or duplex with three to five 1.5 HP ACs and a pumping machine</li>"
              "<li><b>20–30 kW</b>: an estate residence, office or small commercial building, often three-phase</li>"
              "<li><b>50 kW and above</b>: hotels, schools, hospitals, warehouses and industrial facilities</li>"
              "</ul>",
              "Air conditioning is almost always the deciding factor. Our engineers carry out a free load "
              "assessment before quoting, so the system is sized against your actual appliances rather than a "
              "guess. You can start with our <a href=\"calculator.html\">solar calculator</a>."]),
            ("How many solar panels do I need to run an air conditioner?",
             ["A 1.5 HP inverter air conditioner draws roughly 1.1–1.3 kW while running. Running one for a normal "
              "day, with battery to cover the night, needs roughly <b>four to six 620 W panels</b> dedicated to "
              "that load once losses are accounted for.",
              "In practice we never size panels per appliance; we size the array against total daily energy use in "
              "kWh and the battery against overnight demand. For reference, our 16 kW package (20 × 620 W panels "
              "and 2 × 16 kWh batteries) is rated for five 1.5 HP air conditioners alongside a full household load."]),
            ("Can solar power run an air conditioner in Nigeria?",
             ["Yes. Every one of our packages from 5 kVA upward is rated to run air conditioning, and our larger "
              "systems run multiple units continuously.",
              "Two things make it work: a hybrid inverter with enough capacity to absorb the compressor's starting "
              "surge, and enough lithium storage to carry the AC through the night. This is why we size against the "
              "specific AC units on site, a 3 HP unit and a 1 HP unit place very different demands on the same "
              "system."]),
            ("What can a 16kW solar system power?",
             ["A 16 kW / 48 V system with two 16 kWh lithium batteries and 20 × 620 W panels is rated for "
              "70 bulbs, 10 fans, 4 fridges and freezers, a washing machine, <b>five 1.5 HP air conditioners</b>, "
              "a pumping machine, a microwave and an electric blender.",
              "We have installed exactly this configuration for a two-bedroom short-stay apartment running three "
              "air conditioners (two 1.5 HP and one 3 HP) plus refrigeration, television and lighting. "
              "See the <a href=\"projects.html#16kw-residential-airbnb\">full case study</a>."]),
            ("Will solar panels work during a power outage?",
             ["Yes. That is the point of a battery-based system. Our installations use hybrid inverters with "
              "lithium battery storage, so when the grid fails the system continues supplying your building from "
              "stored energy and from the panels.",
              "There is no transfer delay and no switchover gap, which is why sensitive equipment such as "
              "medical refrigeration, ICT and POS systems stay online through an outage."]),
            ("Do solar panels work on cloudy days and during the rainy season?",
             ["Yes. Solar panels generate from daylight, not direct sunshine, so they continue producing on cloudy "
              "days, at reduced output.",
              "This is why battery capacity matters as much as panel count in Nigeria. We size the storage so that "
              "a run of overcast days is carried by the battery bank rather than forcing you back onto a generator, "
              "and we oversize arrays relative to storage so the bank refills within a single average solar day."]),
        ],
    },
    {
        "key": "install",
        "label": "Installation &amp; process",
        "items": [
            ("How long does a solar installation take?",
             ["Installation is completed within <b>48 hours of payment confirmation</b> for most systems, except in "
              "rare cases of unforeseen circumstances or delays. Larger commercial and industrial systems typically "
              "take one to three working days.",
              "The full process is: consultation, personalised proposal, site visit where necessary, payment and "
              "agreement, scheduling and installation, testing and commissioning, then after-sales support."]),
            ("What is your installation process from first contact to switch-on?",
             ["<ul>"
              "<li><b>1. Consultation</b>: we discuss your energy needs, current challenges and budget.</li>"
              "<li><b>2. Proposal</b>: a personalised quotation with recommended system size, cost breakdown, "
              "warranty terms and payment plan.</li>"
              "<li><b>3. Site visit</b>: where necessary, a physical inspection of your wiring, roof strength "
              "and energy load.</li>"
              "<li><b>4. Payment &amp; agreement</b>: payment to a company account, with a receipt issued.</li>"
              "<li><b>5. Scheduling &amp; installation</b>: typically completed within 1–3 working days depending "
              "on system size.</li>"
              "<li><b>6. Testing &amp; commissioning</b>: we test the system thoroughly and show you how to use it.</li>"
              "<li><b>7. After-sales support</b>: warranty coverage, priority support and regular system health checks.</li>"
              "</ul>"]),
            ("Will solar panels damage my roof?",
             ["No. Solar panels do not damage roofs when installed properly. In fact they protect the roof surface "
              "beneath them by shielding it from rain, direct sun and debris.",
              "Our installations use engineered mounting rails fixed appropriately to the roof structure. Where roof "
              "condition, orientation or available area is unsuitable, we install a ground-mounted array instead."]),
            ("Do I need to remove my generator or existing wiring?",
             ["No. A hybrid solar installation integrates with your existing distribution board, and your generator "
              "can remain in place as a backup you rarely use. Most of our customers keep the generator for the "
              "first year and then find they no longer start it.",
              "During the site visit we check your existing wiring and flag anything that needs correcting before "
              "the system is connected."]),
            ("Where in Nigeria do you install?",
             ["We operate <b>21 offices across Abuja, Lagos and Port Harcourt</b> and install nationwide.",
              "Port Harcourt: Sani Abacha 1 &amp; 2 (GRA Phase 3), Port Harcourt City Mall (SPAR) and Market Square "
              "GRA Phase 2. Abuja: Jabi Lake Mall, Wuse 2, Silverbird Entertainment Centre (first floor and "
              "basement), Ceddi Plaza and Primus Mall Gwarinpa. Lagos: Lekki Phase 1 and The Circle Mall, Jakande. "
              "Full addresses are on our <a href=\"contact.html\">contact page</a>."]),
        ],
    },
    {
        "key": "equipment",
        "label": "Equipment, warranty &amp; maintenance",
        "items": [
            ("What warranty do you offer on solar panels, batteries and inverters?",
             ["On our Deye and Solis product lines: <b>25 years on solar panels</b>, <b>10 years on lithium "
              "batteries</b>, <b>5 years on inverters</b>, plus <b>1 year of free after-sales service support</b>.",
              "On our standard product line: 20 years on solar panels, 5 years on lithium batteries, 2 years on "
              "inverters, 1 year on SMF/tubular batteries, 1 year on charge controllers and 1 year of free "
              "after-sales support."]),
            ("How long do solar panels and batteries last?",
             ["Solar panels typically last <b>25 to 30 years</b>, with warranties guaranteeing performance for at "
              "least 20 to 25 years.",
              "Battery life depends on the chemistry. <b>Lithium batteries last 10 to 15 years.</b> Drycell and "
              "tubular batteries last 2 to 3 years, which is why we specify lithium on virtually every system we "
              "install, the higher upfront cost is recovered several times over across the life of the installation."]),
            ("How much maintenance does a solar system need?",
             ["Very little. Regular cleaning of the panels so they are not obstructed by dust or dirt, plus "
              "occasional checks, is usually all that is required.",
              "Every installation includes one year of free after-sales service support, and we carry out regular "
              "system health checks. There are no filters to change, no oil to top up and no fuel to buy."]),
            ("What components make up a complete solar system?",
             ["A complete solar system has five parts:",
              "<ul>"
              "<li><b>Solar panels</b>: photovoltaic modules that capture sunlight and convert it into direct "
              "current (DC) electricity.</li>"
              "<li><b>Inverter</b>: converts DC electricity into the alternating current (AC) your appliances use.</li>"
              "<li><b>Battery storage</b>: stores excess energy for use at night or on cloudy days.</li>"
              "<li><b>MPPT charge controller</b>: regulates voltage and current from the panels to prevent battery "
              "overcharging.</li>"
              "<li><b>Mounting structures</b>: secure the panels in place at the optimum angle for sunlight.</li>"
              "</ul>",
              "Buying an inverter alone gives you backup. Buying the full system gives you generation."]),
            ("Which inverter brands do you supply?",
             ["We supply and install <b>Deye</b>, <b>Solis</b> and <b>ALP Solar</b> hybrid inverters, alongside "
              "Bauman Energy, BICODI and SRNE equipment, with lithium battery storage from tier-1 manufacturers.",
              "We publish separate price charts for our Deye and Solis product lines so you can compare "
              "configurations and pricing directly on our <a href=\"pricing.html\">pricing page</a>."]),
            ("Do you supply anything besides solar and inverters?",
             ["Yes. Alongside solar panels, hybrid inverters, lithium batteries and MPPT charge controllers we "
              "supply and install <b>solar water heaters, submersible pumps, inverter air conditioners and solar "
              "street lighting systems</b>.",
              "All are installed by our own teams and covered by the same after-sales support."]),
        ],
    },
    {
        "key": "company",
        "label": "About Solar World",
        "items": [
            ("Who is Solar World Electric Technology Ltd.?",
             ["Solar World Electric Technology Limited (RC 1684774) is a Nigerian renewable energy company founded "
              "in <b>2015</b>, specialising in the sales, installation and maintenance of solar power systems for "
              "residential, commercial, industrial and government customers.",
              "We have powered <b>over 60,000 homes, offices, hotels, businesses and communities</b> across Nigeria "
              "and operate 21 offices across Abuja, Lagos and Port Harcourt. Our clients include the NDDC, the "
              "Nigerian Army, GIG Logistics, Woodhall Capital, The Brook Finance Company, ENERGYMATICS, "
              "EngenderHealth, Riders for Health, the National Malaria Elimination Programme and the Maritime "
              "Academy of Nigeria, Oron."]),
            ("Why should I buy from Solar World rather than a cheaper supplier?",
             ["Because with solar, who you buy from matters as much as what you buy; that is our stated belief as "
              "a company.",
              "A solar system is a 25-year asset installed into your building. If it is undersized, badly configured "
              "or installed by a team that disappears afterwards, the components' warranties are worthless to you. "
              "We size against your actual load, publish our prices openly, install with our own teams, operate "
              "nine physical offices you can walk into, and back every installation with warranty coverage and a "
              "year of free after-sales support."]),
            ("Do you work with businesses and government institutions?",
             ["Yes. We deliver commercial, industrial and public-sector projects from 20 kW up to 125 kW and beyond, "
              "including offices, hotels, schools, hospitals, warehouses, factories, community projects and street "
              "lighting schemes.",
              "Public and institutional clients we have worked with include the NDDC, the Nigerian Army, the "
              "National Malaria Elimination Programme (Federal Ministry of Health), the Maritime Academy of Nigeria "
              "(Oron), EngenderHealth and Riders for Health."]),
            ("How do I get a quote?",
             ["Message us on WhatsApp at <b>+234 906 331 5492</b>, email <b>solarworldes@gmail.com</b>, or walk into "
              "any of our 21 offices in Abuja, Lagos or Port Harcourt.",
              "Tell us what you want to power, the appliances, how many air conditioners and whether you need it "
              "day and night, and we will size the system and send a costed proposal with warranty terms and "
              "payment options. The consultation and load assessment are free."]),
        ],
    },
    {
        "key": "myths",
        "label": "Solar myths",
        "items": [
            ("Is solar energy too expensive for the average Nigerian?",
             ["No. Solar energy is becoming increasingly affordable, with financing options and payment plans "
              "available to suit different budgets. Our entry-level 3 kVA inverter package starts at ₦1,490,000, "
              "and with our 30% deposit financing plan you can start with ₦447,000 and spread the balance over up "
              "to 12 months.",
              "It is an investment that pays off over time by removing your fuel and electricity costs."]),
            ("Do solar panels only work in sunny climates?",
             ["No. Solar panels still generate power on cloudy days. While sunlight is essential, modern "
              "monocrystalline panels are designed to work efficiently in a variety of weather conditions, "
              "including the Nigerian rainy season."]),
            ("Do solar systems require a lot of maintenance?",
             ["No. Solar systems require minimal maintenance. Regular cleaning of the panels and occasional checks "
              "are usually all that is needed to keep them functioning efficiently. There are no moving parts in a "
              "panel and no fuel system to service."]),
            ("Will a solar system add value to my property?",
             ["Yes. A properly installed solar system with lithium storage is a permanent building improvement with "
              "a 25-year panel warranty. It removes the property's dependence on grid availability and diesel, "
              "which in Nigeria is a material factor for buyers and tenants, particularly for rental apartments, "
              "short-stay properties and commercial premises."]),
        ],
    },
]

# ---------------------------------------------------------------------------
# REVIEWS: WhatsApp screenshots supplied by the business.
# `shot` files live in assets/img/reviews/
# ---------------------------------------------------------------------------
WA_REVIEWS = [
    {"cat": "residential", "shot": "wa-seun-oniru.jpg", "who": "Mr Seun O.", "where": "Residential customer",
     "alt": "WhatsApp review from a Solar World Electric customer praising the professionalism of the installation team",
     "quote": "On a more serious note… Thanks for your professionalism. Much appreciated. I liked the way you "
              "handled every part of the process."},
    {"cat": "longterm", "shot": "wa-two-years.jpg", "who": "Long-term customer", "where": "Two years after installation",
     "alt": "WhatsApp message from a Solar World Electric customer two years after their solar system installation",
     "quote": "It's been almost two years since I got my system and I can't complain."},
    {"cat": "residential", "shot": "wa-wolerus.jpg", "who": "Mr Wolerus A.", "where": "Residential customer",
     "alt": "WhatsApp testimonial showing an AlpSolar inverter and BICODI lithium battery installed by Solar World Electric",
     "quote": "I appreciate the great service rendered. Everything looks good. You are a very good sales person."},
    {"cat": "commercial", "shot": "wa-mr-paul-office.jpg", "who": "Mr Paul", "where": "Office installation",
     "alt": "WhatsApp review from an office customer two weeks after a Solar World Electric solar inverter installation",
     "quote": "About the system, nothing untoward has been reported to me so I can firmly say the office is "
              "enjoying your services. You have been a great help."},
    {"cat": "residential", "shot": "wa-prof-isaac.jpg", "who": "Prof. Isaac", "where": "Residential customer",
     "alt": "WhatsApp testimonial from a professor who installed a solar system with Solar World Electric",
     "quote": "For now, there's no issue and I wish it will remain so for a reasonable period. I'm committed to "
              "doing business with Solar World and we'll keep our mutual trust."},
    {"cat": "residential", "shot": "wa-mr-wole.jpg", "who": "Mr Wole", "where": "Residential customer",
     "alt": "WhatsApp review of a completed AlpSolar and BICODI solar inverter installation by Solar World Electric",
     "quote": "I appreciate the great service rendered. You have an excellent team. The installation was completed "
              "today. All indications show that the equipment is working satisfactorily."},
    {"cat": "residential", "shot": "wa-freezer.jpg", "who": "Verified customer", "where": "Home installation",
     "alt": "WhatsApp feedback from a customer whose solar system successfully ran a freezer and lighting circuits",
     "quote": "The system worked well with the freezer. I'm impressed. It's an amazing experience. Thank you."},
    {"cat": "residential", "shot": "wa-can-attest.jpg", "who": "Verified customer", "where": "Home installation",
     "alt": "WhatsApp message praising Solar World Electric's service delivery and confirming the home solar system is performing",
     "quote": "I can attest! The solar at home here is really serving its purpose."},
    {"cat": "longterm", "shot": "wa-mrs-ijeoma.jpg", "who": "Mrs Ijeoma", "where": "Residential customer",
     "alt": "WhatsApp check-in showing a satisfied Solar World Electric solar installation customer",
     "quote": "No complaints so far. Thanks a lot."},
]

# Photo testimonials: real installation photography with SEO captions
PHOTO_REVIEWS = [
    {"img": "project-ground-array-1.jpg",
     "title": "Ground-mounted solar array, Port Harcourt",
     "cap": "Affordable solar installation for a residential compound, a ground-mounted monocrystalline array "
            "sited for full-day sun where roof orientation was unsuitable.",
     "alt": "Ground-mounted monocrystalline solar array installed by Solar World Electric in Port Harcourt"},
    {"img": "pkg/pkg-25kw.jpg",
     "title": "25 kW high-voltage battery rack",
     "cap": "Solar inverter installation for offices, a stackable high-voltage lithium rack with battery "
            "management, sized for a full commercial load.",
     "alt": "25kW high voltage stackable lithium battery rack and Deye inverter installed by Solar World Electric"},
    {"img": "pkg/pkg-80kw.jpg",
     "title": "80 kW (100 kVA) dual-inverter bank",
     "cap": "Industrial solar system for a large facility, twin Deye inverters feeding a 100 kWh lithium bank "
            "across two stacked cabinets.",
     "alt": "80kW 100kVA dual inverter bank and lithium battery cabinets installed by Solar World Electric"},
    {"img": "install-deye-3batt.jpg",
     "title": "Deye hybrid inverter with three-battery bank",
     "cap": "Solar system for home, a Deye hybrid inverter, surge protection and a three-module lithium bank "
            "installed in a residential utility space.",
     "alt": "Deye hybrid inverter and three lithium batteries installed in a Nigerian home by Solar World Electric"},
    {"img": "project-rooftop-lekki.jpg",
     "title": "Rooftop array, Lekki, Lagos",
     "cap": "Residential solar installation in Lagos, a full-pitch rooftop array delivering generation across "
            "the whole roof plane.",
     "alt": "Rooftop monocrystalline solar panel array installed in Lekki Lagos by Solar World Electric"},
    {"img": "pkg/pkg-50kw-b.jpg",
     "title": "50 kW high-voltage commercial system",
     "cap": "Commercial solar installation, a 50 kW high-voltage package with combiner box, busbar and "
            "battery management for continuous trading hours.",
     "alt": "50kW high voltage commercial solar and inverter installation by Solar World Electric"},
]

# ---------------------------------------------------------------------------
# WHY US
# ---------------------------------------------------------------------------
WHY_US = [
    ("Unmatched expertise &amp; experience",
     "Ten years of hands-on solar work in Nigerian conditions. From system design to after-sales support, "
     "our engineers guide every step, and install every system themselves.",
     "shield"),
    ("We are in your city, and growing",
     "21 offices across Abuja, Lagos and Port Harcourt, with nationwide installation. Wherever you are, "
     "a team is within reach for consultation, installation and support.",
     "pin"),
    ("Customised solutions for every need",
     "No two buildings use power the same way. We assess your actual appliances and load profile, then design "
     "a system that fits, rather than a package pulled off a shelf.",
     "sliders"),
    ("Dedicated support that actually answers",
     "Our job does not end at installation. You get warranty coverage, priority technical support, routine "
     "maintenance and regular system health checks.",
     "headset"),
    ("Flexible payment options",
     "Start with a 30% deposit and spread the balance over 3, 6, 9 or 12 months through our financing partner. "
     "Approved financing is disbursed in 24–48 hours.",
     "wallet"),
    ("Tier-1 components, real warranties",
     "Deye, Solis and ALP hybrid inverters with lithium storage. 25 years on panels, 10 years on lithium "
     "batteries, 5 years on inverters, and a year of free after-sales service.",
     "badge"),
]

# ---------------------------------------------------------------------------
# PROCESS (profile page 24)
# ---------------------------------------------------------------------------
PROCESS = [
    ("Consultation",
     "We start with a conversation to understand your energy needs, your current challenges and your budget. "
     "This helps us propose the right solution for you."),
    ("Proposal",
     "Based on our discussion we send a personalised quotation including recommended system size, cost breakdown, "
     "warranty terms and conditions, and payment plan."),
    ("Site visit",
     "Where necessary we schedule a physical inspection to check your wiring, roof strength and energy load, "
     "confirming the proposal is technically suitable for your space."),
    ("Payment &amp; agreement",
     "Once you have read and agreed our terms of delivery and service, payment is made to a company account and "
     "a receipt is issued. We then prepare for delivery and installation."),
    ("Scheduling &amp; installation",
     "Our team schedules your installation and carries it out on the agreed day, typically within 1–3 working "
     "days depending on system size."),
    ("Testing &amp; commissioning",
     "After installation we test the system thoroughly and show you how to use it, and give you a guide so you "
     "always know what to do."),
    ("After-sales support",
     "Even after installation we stay with you. You enjoy warranty coverage, priority support and regular system "
     "health checks from our team."),
]

# ---------------------------------------------------------------------------
# FINANCING STEPS (profile page 11)
# ---------------------------------------------------------------------------
FINANCE_STEPS = [
    ("Tell us what you need",
     "Let us know what you want to power, a cosy apartment, a business workspace or an industrial facility. "
     "We recommend the ideal system and send a detailed quotation."),
    ("Get your pro-forma invoice",
     "Once your solar package is finalised we issue a pro-forma invoice, a breakdown of your total system cost. "
     "This document is used to process your financing application."),
    ("Let our partner handle it",
     "No long queues at the bank and no paperwork headaches. At any of our locations, our in-house financing team "
     "walks you through the entire loan process."),
    ("Make a deposit",
     "To get started, all you need is an initial deposit of 30% of your system's total cost. On a ₦5 million "
     "system that is ₦1.5 million, with our financing partner covering the remaining ₦3.5 million."),
    ("Fast loan disbursement",
     "No waiting for weeks. Once your application is approved, financing is disbursed within 24 to 48 hours, so "
     "installation can move forward almost immediately."),
    ("Flexible repayment options",
     "The balance is split into smaller payments over 3, 6, 9 or 12 months, whichever works best for you. "
     "A fixed 4% interest is added to the principal each month, with no hidden charges."),
    ("Seamless installation",
     "Once payment is confirmed, our professional team schedules and carries out your installation right away. "
     "No more fuel costs and no more blackouts."),
]

# ---------------------------------------------------------------------------
# LEADERSHIP (profile pages 4–8)
# ---------------------------------------------------------------------------
TEAM = [
    ("Mr. Charles Abia", "Chairman, Solar World Group", "team-1.jpg"),
    ("Abigail Felix", "Managing Director", "team-abigail.jpg"),
    ("Raphael Duru", "General Manager, Operations", "team-raphael.jpg"),
    ("Ejike Okoli", "Head of Sales &amp; Business, Abuja Region", "team-ejike.jpg"),
    ("Esther Olufunke", "Head of Sales &amp; Business, Lagos Region", "team-esther.jpg"),
    ("Chioma Uga", "Head of Sales &amp; Business, Port Harcourt Region", "team-chioma.jpg"),
    ("Maureen Okoli", "Head of Strategy &amp; Business Development", "team-maureen.jpg"),
    ("Alexia Ilo", "Head of Business Coordination", "team-alexia.jpg"),
    ("Esema Essienubong", "Head of Legal &amp; Administration", "team-esema.jpg"),
    ("Favour Austine", "Head of Human Capital / HR", "team-favour.jpg"),
    ("Ezeh Nmesoma", "Head of Corporate Sales, Abuja Region", "team-ezeh.jpg"),
    ("Deborah Simeon", "Head of Media", "team-deborah.jpg"),
    ("Monebi Rachael", "Head of Administration, Lagos Region", "team-monebi.jpg"),
    ("Abidemi Owolabi", "Branch Manager, Lekki Phase 1, Lagos", "team-abidemi.jpg"),
    ("Okpalaojimmadu Ogechi", "Branch Manager, Port Harcourt City Mall (SPAR)", "team-ogechi.jpg"),
]
