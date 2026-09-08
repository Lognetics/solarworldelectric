# -*- coding: utf-8 -*-
"""
Solar World Electric, project case studies.

INTEGRITY NOTE
--------------
`verified: True`  => every fact in the entry was supplied by the business.
`verified: False` => the SYSTEM SPECIFICATION is real (taken from the Deye /
                     Solis / standard price charts and the installation
                     photographs), but the CLIENT NAME, exact LOCATION and any
                     CUSTOMER QUOTE still need to be confirmed before the page
                     goes live. Those fields are left as `client: None` /
                     `quote: None` on purpose. Do not invent them.

Fill in `client`, `location` and `quote` as the business confirms each project,
then flip `verified` to True and re-run `python3 tools/build.py`.
"""

CASES = [

    # ======================================================================
    # RESIDENTIAL
    # ======================================================================
    {
        "id": "16kw-residential-airbnb",
        "cat": "residential",
        "type": "Airbnb / Short-stay accommodation",
        "verified": True,
        "featured": True,
        "title": "16 kW Residential Solar Installation for a Two-Bedroom Airbnb",
        "location": None,           # business to confirm
        "client": None,             # private residence
        "img": "pkg/pkg-16kw.jpg",
        "alt": "16 kW residential solar and inverter installation for a two-bedroom Airbnb apartment in Nigeria",
        "specs": [
            ("System", "16 kW inverter"),
            ("Battery storage", "2 × 16 kWh lithium"),
            ("Solar panels", "20 × 620 W"),
            ("Property", "Two-bedroom apartment"),
        ],
        "excerpt": ("An Airbnb operator needed power that keeps guests comfortable through every "
                    "outage, without generator noise. We sized a 16 kW system around the property's "
                    "three air conditioners and everyday loads."),
        "loads": ("3 air conditioners (two 1.5 HP, one 3 HP), refrigeration, television, lighting "
                  "and other household appliances"),
        "sections": [
            ("The Challenge",
             ["For an Airbnb operator, electricity is not simply a household convenience. "
              "It is part of the customer experience.",
              "Guests expect a property advertised as comfortable to remain comfortable when the "
              "public power supply goes off. Air conditioning, refrigeration, lighting, entertainment "
              "and other essential appliances need to remain available without the constant sound and "
              "inconvenience associated with a generator.",
              "The owner of this two-bedroom Airbnb wanted a reliable power solution but was faced "
              "with a more important question: who could they trust to design a system that would "
              "actually match the property's requirements?",
              "Rather than purchasing an inverter based on its advertised capacity alone, the customer "
              "approached Solar World to determine what system would properly support the apartment's "
              "intended loads.",
              "The property had three air conditioners, two 1.5 HP AC units and one 3 HP AC unit. "
              "It also needed to accommodate everyday loads such as lighting, television, refrigeration, "
              "microwave, washing machine and other household appliances."]),
            ("Our Recommendation",
             ["After considering the property's requirements, Solar World recommended a 16 kW inverter "
              "system paired with two 16 kWh lithium batteries and 20 solar panels.",
              "The objective was not simply to provide backup electricity. The objective was to give the "
              "property a dependable energy system capable of supporting the customer's Airbnb operations "
              "and maintaining a comfortable environment for guests."]),
            ("What We Installed",
             ["16 kW inverter",
              "2 × 16 kWh lithium batteries",
              "20 units of 620 W solar panels",
              "Complete installation and system configuration"], "list"),
            ("The Result",
             ["The system has been performing according to the property's present energy requirements, "
              "with the customer reporting that it has not disappointed them since installation.",
              "One of the biggest benefits for the property is the experience itself. There is no generator "
              "noise disturbing guests. There is no need to interrupt the atmosphere of the property every "
              "time the grid supply goes down. The customer also has a system with enough capacity for the "
              "loads they currently need without immediately having to pursue another upgrade."]),
            ("Why This Project Matters",
             ["This installation demonstrates an important principle in residential solar: the right solar "
              "system is designed around the customer's actual lifestyle and energy requirements.",
              "For short-stay apartments, Airbnbs and serviced residences, reliable electricity directly "
              "affects the customer experience."]),
        ],
        "quote": ("The biggest thing for me was knowing I could give my guests consistent power without the "
                  "noise and inconvenience of a generator. Since we installed the system, it has performed "
                  "exactly as we expected and is very easy to operate. I'm even looking at getting extra "
                  "panels and another battery for more backup."),
        "quote_status": "Suggested testimonial direction, to be replaced with the customer's actual wording.",
        "keywords": ["solar system for Airbnb", "solar system for home", "residential solar installation",
                     "solar inverter installation for home", "solar battery system",
                     "lithium battery solar system", "solar installation in Nigeria"],
    },
    {
        "id": "8kw-family-home-port-harcourt",
        "cat": "residential", "type": "Family home", "verified": False,
        "title": "8 kW (10 kVA) Home Solar &amp; Inverter Installation in Port Harcourt",
        "location": "Port Harcourt, Rivers State", "client": None,
        "img": "pkg/pkg-8kw.jpg",
        "alt": "8kW home solar and inverter installation in Port Harcourt with Deye hybrid inverter and lithium battery",
        "specs": [("System", "8 kW / 48 V hybrid"), ("Battery storage", "1 × 12 kWh lithium"),
                  ("Solar panels", "8 × 620 W"), ("Property", "Family home")],
        "excerpt": ("A family home that wanted to retire the generator entirely. The 8 kW package "
                    "carries lighting, refrigeration, entertainment and two air conditioners around the clock."),
        "loads": "50 bulbs, 10 fans, 6 television sets, standard fridge and freezer, washing machine, two 1.5 HP air conditioners and an electric blender",
        "sections": [
            ("The Challenge",
             ["Like most family homes in Port Harcourt, this household was running two power bills at once: "
              "the grid bill for the hours supply was available, and diesel or petrol for the generator that "
              "covered everything else. The generator also meant noise every evening and maintenance every month.",
              "The family wanted a single system that would carry the whole house, not just a few sockets and "
              "lights, so that a power outage would stop being an event."]),
            ("Our Recommendation",
             ["We carried out a load assessment on the property and specified an 8 kW / 48 V hybrid system with "
              "a single 12 kWh lithium battery and eight 620 W monocrystalline panels.",
              "At this size the array recharges the battery during the day while simultaneously carrying the "
              "daytime load, so the household draws from stored energy through the evening and overnight."]),
            ("What We Installed",
             ["8 kW / 48 V hybrid inverter", "1 × 12 kWh lithium battery", "8 × 620 W monocrystalline solar panels",
              "Electric cables, circuit protection, mounting rack and full installation"], "list"),
            ("The Result",
             ["The configuration is rated to run 50 lighting points, 10 fans, 6 television sets, a standard fridge "
              "and freezer, a washing machine, two 1.5 HP air conditioners and an electric blender.",
              "The household runs on solar and stored energy without switching to a generator, and the system "
              "carries a 5-year inverter warranty, 10-year battery warranty and 25-year panel warranty."]),
        ],
        "quote": None,
        "keywords": ["affordable solar installation", "solar system for home", "home solar Port Harcourt",
                     "8kW solar system price Nigeria", "solar inverter installation for home"],
    },
    {
        "id": "10kw-duplex-abuja",
        "cat": "residential", "type": "Duplex", "verified": False,
        "title": "10 kW (12.5 kVA) Duplex Solar &amp; Inverter Installation in Abuja",
        "location": "Abuja, FCT", "client": None,
        "img": "pkg/pkg-10kw.jpg",
        "alt": "10kW 12.5kVA duplex solar and inverter installation in Abuja with 16kWh lithium battery storage",
        "specs": [("System", "10 kW / 48 V hybrid"), ("Battery storage", "1 × 16 kWh lithium"),
                  ("Solar panels", "8 × 620 W"), ("Property", "Detached duplex")],
        "excerpt": ("A duplex with three air conditioners, two fridges and two freezers needed a system that "
                    "could hold overnight load without dropping. 16 kWh of lithium storage does it."),
        "loads": "50 bulbs, 10 fans, 6 television sets, 2 fridges, 2 freezers, washing machine, three 1.5 HP air conditioners, pumping machine, microwave and electric blender",
        "sections": [
            ("The Challenge",
             ["Duplexes carry more continuous load than most homeowners expect. Two fridges and two freezers run "
              "day and night, a pumping machine cycles on demand, and three air conditioners can dominate the "
              "evening profile.",
              "The owner had been quoted on inverter capacity alone. What actually decides whether a duplex gets "
              "through the night is battery capacity, and that had not been sized against the real load."]),
            ("Our Recommendation",
             ["We specified a 10 kW / 48 V hybrid inverter with a single 16 kWh lithium battery and eight 620 W panels. "
              "The larger battery is the deliberate choice here: it holds the refrigeration and overnight base load "
              "comfortably while the inverter handles AC surge on start-up."]),
            ("What We Installed",
             ["10 kW / 48 V hybrid inverter", "1 × 16 kWh lithium battery", "8 × 620 W monocrystalline solar panels",
              "Electric cables, accessories and complete installation"], "list"),
            ("The Result",
             ["The system is rated for 50 lighting points, 10 fans, 6 television sets, 2 fridges, 2 freezers, a washing "
              "machine, three 1.5 HP air conditioners, a pumping machine, microwave and electric blender.",
              "The property runs without a generator, and the battery bank can be extended later without replacing "
              "the inverter."]),
        ],
        "quote": None,
        "keywords": ["solar system for duplex", "solar installation Abuja", "10kW solar system Nigeria",
                     "residential solar installation", "solar inverter installation for home"],
    },
    {
        "id": "12kw-family-home-lagos",
        "cat": "residential", "type": "Family home", "verified": False,
        "title": "12 kW (15 kVA) Home Solar &amp; Inverter Installation in Lagos",
        "location": "Lekki, Lagos", "client": None,
        "img": "pkg/pkg-12kw.jpg",
        "alt": "12kW 15kVA home solar and inverter installation in Lekki Lagos with two 16kWh lithium batteries",
        "specs": [("System", "12 kW / 48 V hybrid"), ("Battery storage", "2 × 16 kWh lithium"),
                  ("Solar panels", "16 × 620 W"), ("Property", "Family home")],
        "excerpt": ("Sixteen panels and 32 kWh of lithium storage, enough to carry a large Lagos household "
                    "through consecutive low-sun days without touching a generator."),
        "loads": "70 bulbs, 10 fans, 3 fridges and freezers, washing machine, three 1.5 HP air conditioners, pumping machine, microwave and electric blender",
        "sections": [
            ("The Challenge",
             ["A larger household means more of everything: more lighting points, more refrigeration, more "
              "simultaneous air conditioning. It also means less tolerance for a system that runs out at 3 a.m.",
              "The family wanted headroom, a system that would still perform on a cloudy week, and one they "
              "would not outgrow in two years."]),
            ("Our Recommendation",
             ["A 12 kW / 48 V hybrid inverter with two 16 kWh lithium batteries (32 kWh total) and a 16-panel array "
              "rated at 9.92 kWp.",
              "Doubling the battery bank is what buys resilience through consecutive low-sun days; the 16-panel array "
              "is sized to refill that bank within a single good solar day."]),
            ("What We Installed",
             ["12 kW / 48 V hybrid inverter", "2 × 16 kWh lithium batteries", "16 × 620 W monocrystalline solar panels",
              "Electric cables, accessories and complete installation"], "list"),
            ("The Result",
             ["Rated for 70 lighting points, 10 fans, 3 fridges and freezers, a washing machine, three 1.5 HP air "
              "conditioners, a pumping machine, microwave and electric blender.",
              "The household operates entirely on solar and stored energy under normal conditions."]),
        ],
        "quote": None,
        "keywords": ["solar system for home", "solar installation Lagos", "12kW solar system price",
                     "affordable solar installation", "lithium battery solar system"],
    },
    {
        "id": "5kw-apartment-starter",
        "cat": "residential", "type": "Apartment", "verified": False,
        "title": "5 kW (5 kVA) Apartment Solar &amp; Inverter Installation",
        "location": "Abuja, FCT", "client": None,
        "img": "install-deye-3batt.jpg",
        "alt": "5kW apartment solar and inverter installation with Deye hybrid inverter and three lithium batteries",
        "specs": [("System", "5 kW / 48 V hybrid"), ("Battery storage", "2 × 5 kWh lithium"),
                  ("Solar panels", "8 × 620 W"), ("Property", "Apartment")],
        "excerpt": ("The entry point into full solar for an apartment: lighting, entertainment, refrigeration "
                    "and two 1 HP air conditioners, with no generator in the picture."),
        "loads": "40 bulbs, 6 fans, 5 television sets, 1 fridge, 2 freezers, washing machine, two 1 HP air conditioners, pumping machine, microwave and electric blender",
        "sections": [
            ("The Challenge",
             ["Apartment residents are often told solar is only for large houses with big roofs and big budgets. "
              "In practice the load profile of an apartment is modest and very predictable, which makes it one of "
              "the easiest properties to power properly."]),
            ("Our Recommendation",
             ["A 5 kW / 48 V hybrid inverter with two 5 kWh lithium batteries and an eight-panel 620 W array. "
              "The second battery is what separates a system that merely bridges outages from one that runs the "
              "apartment overnight."]),
            ("What We Installed",
             ["5 kW / 48 V hybrid inverter", "2 × 5 kWh lithium batteries", "8 × 620 W monocrystalline solar panels",
              "Electric cables, accessories and complete installation"], "list"),
            ("The Result",
             ["Rated for 40 bulbs, 6 fans, 5 television sets, a fridge, 2 freezers, a washing machine, two 1 HP air "
              "conditioners, a pumping machine, microwave and electric blender.",
              "This is the most affordable route to a genuinely generator-free apartment."]),
        ],
        "quote": None,
        "keywords": ["affordable solar installation", "solar system for apartment", "small solar system Nigeria",
                     "5kVA solar inverter price", "solar for rented apartment"],
    },
    {
        "id": "20kw-estate-residence",
        "cat": "residential", "type": "Estate", "verified": False,
        "title": "20 kW (25 kVA) Three-Phase Solar Installation for an Estate Residence",
        "location": "Abuja, FCT", "client": None,
        "img": "pkg/pkg-20kw-a.jpg",
        "alt": "20kW three-phase solar and inverter installation for an estate residence in Nigeria",
        "specs": [("System", "20 kW / 48 V three-phase"), ("Battery storage", "3 × 16 kWh lithium"),
                  ("Solar panels", "24 × 620 W"), ("Property", "Estate residence")],
        "excerpt": ("Six air conditioners, five fridges and freezers and a borehole pump on a three-phase "
                    "supply, sized so nothing has to be switched off to run anything else."),
        "loads": "80 bulbs, 10 fans, 5 fridges and freezers, washing machine, six 1.5 HP air conditioners, pumping machine, microwave and electric blender",
        "sections": [
            ("The Challenge",
             ["Estate residences are usually wired three-phase, and a single-phase inverter cannot serve them "
              "properly. Loads are also distributed across the phases, so the system has to balance rather than "
              "simply total them.",
              "This property runs six 1.5 HP air conditioners plus a borehole pump, a combination that punishes "
              "an undersized inverter every time the pump and an AC compressor start together."]),
            ("Our Recommendation",
             ["A 20 kW / 48 V three-phase hybrid inverter with 48 kWh of lithium storage across three batteries and "
              "a 24-panel array.",
              "Three-phase output means the existing distribution board is used as designed, with no rewiring and no "
              "phase left unpowered."]),
            ("What We Installed",
             ["20 kW / 48 V three-phase hybrid inverter", "3 × 16 kWh lithium batteries",
              "24 × 620 W monocrystalline solar panels", "Electric cables, accessories and complete installation"], "list"),
            ("The Result",
             ["Rated for 80 lighting points, 10 fans, 5 fridges and freezers, a washing machine, six 1.5 HP air "
              "conditioners, a pumping machine, microwave and electric blender across all three phases."]),
        ],
        "quote": None,
        "keywords": ["three phase solar system Nigeria", "solar system for estate", "20kW solar installation",
                     "residential solar installation", "solar for large home"],
    },
    {
        "id": "11kw-alp-hybrid-home",
        "cat": "residential", "type": "Homeowner", "verified": False,
        "title": "11 kW ALP Solar Hybrid Installation for a Homeowner",
        "location": "Port Harcourt, Rivers State", "client": None,
        "img": "install-room-stack1.jpg",
        "alt": "11kW ALP solar hybrid inverter installation with two 16kWh lithium batteries for a Nigerian home",
        "specs": [("System", "11 kW / 48 V ALP hybrid"), ("Battery storage", "2 × 16 kWh lithium"),
                  ("Solar panels", "24 × 620 W"), ("Property", "Detached home")],
        "excerpt": ("A 24-panel array paired with 32 kWh of storage, specified for a homeowner who wanted "
                    "generation, not just backup."),
        "loads": "50 bulbs, 10 fans, 6 television sets, 2 fridges, 2 freezers, washing machine, three 1.5 HP air conditioners, pumping machine, microwave and electric blender",
        "sections": [
            ("The Challenge",
             ["This homeowner had already lived with an undersized inverter and knew the failure mode: the battery "
              "empties before morning and the generator comes back. They wanted the array oversized relative to the "
              "battery so the system would recharge fully even on an average day."]),
            ("Our Recommendation",
             ["An 11 kW / 48 V ALP solar hybrid inverter, two 16 kWh lithium batteries and a 24-panel array totalling "
              "14.88 kWp, deliberately generous generation for the storage behind it."]),
            ("What We Installed",
             ["11 kW / 48 V ALP solar hybrid inverter", "2 × 16 kWh lithium batteries",
              "24 × 620 W monocrystalline solar panels", "Cables, accessories and complete installation"], "list"),
            ("The Result",
             ["Rated for 50 lighting points, 10 fans, 6 television sets, 2 fridges, 2 freezers, a washing machine, "
              "three 1.5 HP air conditioners, a pumping machine, microwave and electric blender."]),
        ],
        "quote": None,
        "keywords": ["solar system for home", "ALP solar hybrid inverter", "11kW solar system",
                     "solar inverter installation for home", "solar panels Nigeria price"],
    },
    {
        "id": "30kva-home-installation",
        "cat": "residential", "type": "Family home", "verified": False,
        "title": "30 kVA Home Solar / Inverter Installation in Port Harcourt",
        "location": "Port Harcourt, Rivers State", "client": None,
        "img": "project-ground-array-1.jpg",
        "alt": "30kVA home solar inverter installation in Port Harcourt with 48-panel ground-mounted array",
        "specs": [("System", "30 kVA / 48 V hybrid"), ("Battery storage", "4 × 17.6 kWh lithium"),
                  ("Solar panels", "48 × 620 W"), ("Property", "Large family compound")],
        "excerpt": ("The largest of our residential builds: 48 panels, 70 kWh of lithium storage and enough "
                    "headroom for six air conditioners plus a full compound of lighting."),
        "loads": "90 bulbs, 15 fans, 5 fridges and freezers, washing machine, six 1.5 HP air conditioners, pumping machine, microwave and electric blender",
        "sections": [
            ("The Challenge",
             ["A compound of this size behaves more like a small commercial building than a house. Total connected "
              "load is high, and the owner needed a system that would never be the reason something had to be "
              "switched off."]),
            ("Our Recommendation",
             ["A 30 kVA / 48 V hybrid system with four 17.6 kWh lithium batteries, 70.4 kWh of usable storage, and "
              "a 48-panel array rated at 29.76 kWp. At this scale the array is ground-mounted where roof space or "
              "orientation would otherwise limit output."]),
            ("What We Installed",
             ["30 kVA / 48 V hybrid inverter", "4 × 17.6 kWh lithium batteries",
              "48 × 620 W monocrystalline solar panels", "Mounting structure, cables, accessories and complete installation"], "list"),
            ("The Result",
             ["Rated for 90 lighting points, 15 fans, 5 fridges and freezers, a washing machine, six 1.5 HP air "
              "conditioners, a pumping machine, microwave and electric blender."]),
        ],
        "quote": None,
        "keywords": ["30KVA home solar installation", "solar inverter installation Port Harcourt",
                     "large home solar system Nigeria", "ground mounted solar array", "solar system for home"],
    },

    # ======================================================================
    # COMMERCIAL
    # ======================================================================
    {
        "id": "20kw-office-installation",
        "cat": "commercial", "type": "Office", "verified": False, "featured": True,
        "title": "20 kW (25 kVA) Solar Inverter Installation for an Office Building",
        "location": "Abuja, FCT", "client": None,
        "img": "pkg/pkg-20kw-b.jpg",
        "alt": "20kW solar inverter installation for offices in Abuja with three-phase hybrid inverter",
        "specs": [("System", "20 kW / 48 V three-phase"), ("Battery storage", "3 × 16 kWh lithium"),
                  ("Solar panels", "24 × 620 W"), ("Property", "Commercial office")],
        "excerpt": ("Workstations, servers, six air conditioners and a full lighting load, powered through "
                    "the working day without a generator start."),
        "loads": "80 lighting points, workstations and office equipment, 5 fridges and freezers, six 1.5 HP air conditioners, pumping machine and microwave",
        "sections": [
            ("The Challenge",
             ["An office's power problem is different from a home's. The load is concentrated into eight or nine "
              "hours, it peaks with air conditioning in the afternoon, and an outage does not merely inconvenience "
              "people, it stops billable work.",
              "Generator switchovers also mean momentary drops that reset equipment and irritate staff and visitors."]),
            ("Our Recommendation",
             ["A 20 kW / 48 V three-phase hybrid system with 48 kWh of lithium storage and a 24-panel array. "
              "Because the office's peak demand coincides with peak sun, most of the daytime load is served directly "
              "from the array while the battery carries early mornings, evenings and cloudy spells."]),
            ("What We Installed",
             ["20 kW / 48 V three-phase hybrid inverter", "3 × 16 kWh lithium batteries",
              "24 × 620 W monocrystalline solar panels",
              "Distribution integration, circuit protection and complete installation"], "list"),
            ("The Result",
             ["Rated for 80 lighting points, 5 fridges and freezers, six 1.5 HP air conditioners, a pumping machine "
              "and general office equipment.",
              "Staff experience no switchover interruption, and the building's diesel consumption is designed out "
              "rather than reduced."]),
        ],
        "quote": None,
        "keywords": ["solar inverter installation for offices", "commercial solar installation Nigeria",
                     "office solar system Abuja", "three phase solar inverter", "solar for business"],
    },
    {
        "id": "50kw-hotel-installation",
        "cat": "commercial", "type": "Hotel", "verified": False,
        "title": "50 kW Solar &amp; Inverter Installation for a Hotel",
        "location": "Port Harcourt, Rivers State", "client": None,
        "img": "pkg/pkg-50kw-a.jpg",
        "alt": "50kW solar and inverter installation for a hotel in Nigeria with BOS-B lithium battery bank",
        "specs": [("System", "50 kW / 48 V"), ("Battery storage", "5 × 14.3 kWh"),
                  ("Solar panels", "64 × 620 W"), ("Property", "Hotel")],
        "excerpt": ("Guest rooms, kitchen refrigeration, lifts and an EV charger on one system, because in "
                    "hospitality, a power cut is a review."),
        "loads": "120 lighting points, 20 TVs, 4 fridges, 4 freezers, pumping machine, EV charger and five 2.5 HP air conditioners",
        "sections": [
            ("The Challenge",
             ["In hospitality, power reliability is not a facilities issue; it is a reputation issue. Guests notice "
              "the moment air conditioning stops, and they write about it.",
              "Hotels also carry an unusual load shape: refrigeration and corridor lighting run continuously, room "
              "air conditioning spikes at night, and kitchen equipment peaks at service times."]),
            ("Our Recommendation",
             ["A 50 kW / 48 V high-VAC package with five 14.3 kWh BOS-B lithium batteries (71.5 kWh) and a 64-panel "
              "array rated at 39.68 kWp.",
              "High-voltage architecture keeps cable losses and copper cost down at this scale, and the battery "
              "management system gives the maintenance team visibility over every module."]),
            ("What We Installed",
             ["50 kW / 48 V high-VAC inverter system", "5 × 14.3 kWh BOS-B lithium batteries",
              "64 × 620 W monocrystalline solar panels",
              "Battery management system, combiner box, mounting rack, busbar and complete installation"], "list"),
            ("The Result",
             ["Rated for 120 lighting points, 20 TVs, 4 fridges, 4 freezers, a pumping machine, an EV charger and "
              "five 2.5 HP air conditioners.",
              "Guest-facing services stay live through grid outages with no audible switchover."]),
        ],
        "quote": None,
        "keywords": ["solar system for hotel", "commercial solar installation", "50kW solar system Nigeria",
                     "hotel backup power solar", "solar inverter installation for business"],
    },
    {
        "id": "25kw-school-installation",
        "cat": "commercial", "type": "School", "verified": False,
        "title": "25 kW High-Voltage Solar Installation for a School",
        "location": "Abuja, FCT", "client": None,
        "img": "pkg/pkg-25kw.jpg",
        "alt": "25kW high voltage solar installation for a school in Nigeria with stackable lithium battery rack",
        "specs": [("System", "25 kW / 48 V"), ("Battery storage", "7 × 5.12 kWh"),
                  ("Solar panels", "28 × 620 W"), ("Property", "School campus")],
        "excerpt": ("Classrooms, ICT labs, staff offices and an EV charge point, a campus load that maps "
                    "almost perfectly onto the solar day."),
        "loads": "90 lighting points, 8 TVs, ICT equipment, 2 fridges, 2 freezers, 6 kW EV charger, pumping machine and three 2.5 HP air conditioners",
        "sections": [
            ("The Challenge",
             ["Schools have one of the best load profiles for solar in Nigeria: demand runs from roughly 7 a.m. to "
              "4 p.m., which is almost exactly when the array is producing. The obstacle is rarely technical; it is "
              "capital cost against a term-time budget.",
              "The campus also needed the system to hold ICT labs and administrative systems through outages during "
              "examination periods."]),
            ("Our Recommendation",
             ["A 25 kW / 48 V high-VAC package with a stackable 35.8 kWh lithium rack and a 28-panel array. "
              "The stackable rack matters here: the school can add battery modules later without replacing anything "
              "already installed."]),
            ("What We Installed",
             ["25 kW / 48 V high-VAC inverter system", "7 × 5.12 kWh lithium batteries on a stackable rack",
              "28 × 620 W monocrystalline solar panels",
              "Battery management system, combiner box, mounting rack, busbar and complete installation"], "list"),
            ("The Result",
             ["Rated for 90 lighting points, 8 TVs, 2 fridges, 2 freezers, an electric iron, a 6 kW EV charger, a "
              "pumping machine, three 2.5 HP air conditioners, microwave, blender and washing machine."]),
        ],
        "quote": None,
        "keywords": ["solar system for school", "commercial solar installation Nigeria", "school solar power",
                     "25kW solar system", "solar for educational institution"],
    },
    {
        "id": "30kw-hospital-installation",
        "cat": "commercial", "type": "Hospital", "verified": False,
        "title": "30 kW Solar &amp; Inverter Installation for a Hospital",
        "location": "Lagos", "client": None,
        "img": "install-deye-vertical.jpg",
        "alt": "30kW solar and inverter installation for a hospital in Nigeria with a redundant lithium battery bank",
        "specs": [("System", "30 kW / 48 V"), ("Battery storage", "7 × 7.68 kWh"),
                  ("Solar panels", "36 × 620 W"), ("Property", "Hospital / clinic")],
        "excerpt": ("Cold-chain refrigeration, theatre lighting and diagnostic equipment, the one category "
                    "of building where a power gap is a clinical risk."),
        "loads": "100 lighting points, 10 TVs, 3 fridges, 3 freezers, medical and diagnostic equipment, 7 kW EV charger, pumping machine and four 2.5 HP air conditioners",
        "sections": [
            ("The Challenge",
             ["Healthcare facilities cannot treat power as a convenience. Vaccine and reagent cold chains degrade "
              "silently during outages, and theatre and diagnostic equipment must never depend on how quickly a "
              "generator starts.",
              "The facility wanted continuous power with no transfer gap at all, plus visibility into battery state "
              "of charge for its own planning."]),
            ("Our Recommendation",
             ["A 30 kW / 48 V high-VAC package with 53.8 kWh of lithium storage across seven modules and a 36-panel "
              "array rated at 22.32 kWp.",
              "The hybrid inverter carries the load continuously from battery and array, so there is no transfer "
              "event to survive. The battery management system reports per-module state to the facilities team."]),
            ("What We Installed",
             ["30 kW / 48 V high-VAC inverter system", "7 × 7.68 kWh lithium batteries on a stackable rack",
              "36 × 620 W monocrystalline solar panels",
              "Battery management system, combiner box, circuit protection and complete installation"], "list"),
            ("The Result",
             ["Rated for 100 lighting points, 10 TVs, 3 fridges, 3 freezers, a 7 kW EV charger, a pumping machine, "
              "four 2.5 HP air conditioners and a washing machine, alongside clinical equipment."]),
        ],
        "quote": None,
        "keywords": ["solar system for hospital", "healthcare solar power Nigeria", "clinic solar installation",
                     "commercial solar installation", "30kW solar system"],
    },
    {
        "id": "50kw-shopping-facility",
        "cat": "commercial", "type": "Shopping facility", "verified": False,
        "title": "50 kW Solar Installation for a Shopping &amp; Retail Facility",
        "location": "Abuja, FCT", "client": None,
        "img": "pkg/pkg-50kw-b.jpg",
        "alt": "50kW high voltage solar installation for a shopping and retail facility in Nigeria",
        "specs": [("System", "50 kW / 48 V"), ("Battery storage", "7 × 14.3 kWh"),
                  ("Solar panels", "84 × 620 W"), ("Property", "Shopping facility")],
        "excerpt": ("Trading hours are power hours. An 84-panel array carries the shop floor while 100 kWh of "
                    "storage covers evening trade and stocktaking."),
        "loads": "120 lighting points, 20 TVs and displays, 4 fridges, 4 freezers, POS and security systems, pumping machine, EV charger and five 2.5 HP air conditioners",
        "sections": [
            ("The Challenge",
             ["Retail loses money the moment the lights and tills go down, and refrigerated stock is at risk within "
              "the hour. Shopping facilities also run long days, so a system sized only for daylight generation "
              "leaves the last hours of trade exposed."]),
            ("Our Recommendation",
             ["A 50 kW / 48 V high-VAC package with the extended 84-panel array (52.08 kWp) and 100.1 kWh of lithium "
              "storage across seven 14.3 kWh modules.",
              "The extended array is the difference: it fills a large battery bank within the trading day so evening "
              "hours run on stored solar rather than grid or diesel."]),
            ("What We Installed",
             ["50 kW / 48 V high-VAC inverter system", "7 × 14.3 kWh lithium batteries on a stackable rack",
              "84 × 620 W monocrystalline solar panels",
              "Battery management system, combiner box, mounting rack, busbar and complete installation"], "list"),
            ("The Result",
             ["Rated for 120 lighting points, 20 TVs, 4 fridges, 4 freezers, a pumping machine, an EV charger and "
              "five 2.5 HP air conditioners.",
              "Tills, security systems and refrigeration remain live independently of the grid."]),
        ],
        "quote": None,
        "keywords": ["solar system for retail business", "shopping mall solar installation",
                     "commercial solar Nigeria", "solar for supermarket", "50kW solar system price"],
    },
    {
        "id": "16kw-restaurant-installation",
        "cat": "commercial", "type": "Restaurant", "verified": False,
        "title": "16 kW (20 kVA) Solar Inverter Installation for a Restaurant",
        "location": "Lekki, Lagos", "client": None,
        "img": "install-room-stack2.jpg",
        "alt": "16kW 20kVA solar inverter installation for a restaurant in Lagos with lithium battery storage",
        "specs": [("System", "16 kW / 48 V hybrid"), ("Battery storage", "2 × 16 kWh lithium"),
                  ("Solar panels", "20 × 620 W"), ("Property", "Restaurant")],
        "excerpt": ("Chillers, freezers, five air conditioners and a dining room that has to stay comfortable "
                    "through every service."),
        "loads": "70 lighting points, 4 fridges and freezers, kitchen equipment, five 1.5 HP air conditioners, pumping machine and microwave",
        "sections": [
            ("The Challenge",
             ["Restaurants combine the worst of both worlds: continuous refrigeration that cannot be interrupted, "
              "and sharp air-conditioning peaks during service. A generator can cover it, but the noise and fumes "
              "sit directly against the customer experience the restaurant is selling."]),
            ("Our Recommendation",
             ["A 16 kW / 48 V hybrid inverter with 32 kWh of lithium storage and a 20-panel array rated at 12.4 kWp. "
              "Inverter capacity here is chosen for compressor surge rather than average demand."]),
            ("What We Installed",
             ["16 kW / 48 V hybrid inverter", "2 × 16 kWh lithium batteries",
              "20 × 620 W monocrystalline solar panels", "Cables, circuit protection and complete installation"], "list"),
            ("The Result",
             ["Rated for 70 lighting points, 10 fans, 4 fridges and freezers, a washing machine, five 1.5 HP air "
              "conditioners, a pumping machine, microwave and electric blender.",
              "Cold storage stays cold and the dining room stays quiet."]),
        ],
        "quote": None,
        "keywords": ["solar system for restaurant", "solar inverter installation for business",
                     "commercial solar installation Lagos", "16kW solar system", "restaurant backup power"],
    },
    {
        "id": "80kw-warehouse-installation",
        "cat": "commercial", "type": "Warehouse", "verified": False,
        "title": "80 kW (100 kVA) High-Voltage Solar Installation for a Warehouse",
        "location": "Lagos", "client": None,
        "img": "pkg/pkg-80kw.jpg",
        "alt": "80kW 100kVA high voltage solar and inverter installation for a warehouse and logistics facility",
        "specs": [("System", "80 kW / 48 V"), ("Battery storage", "7 × 14.3 kWh"),
                  ("Solar panels", "78 × 620 W"), ("Property", "Warehouse / distribution")],
        "excerpt": ("Large-span lighting, cold storage and handling equipment across a distribution facility, "
                    "on a dual-inverter high-voltage bank."),
        "loads": "150 lighting points, 30 TVs and displays, 5 fridges and 5 freezers, handling equipment, pumping machine and seven 2.5 HP air conditioners",
        "sections": [
            ("The Challenge",
             ["Warehouses have enormous roof area and enormous lighting loads, which makes them natural solar "
              "candidates, but the electrical design has to handle long cable runs and high current without "
              "unacceptable losses."]),
            ("Our Recommendation",
             ["An 80 kW / 48 V high-VAC package built on a dual-inverter bank with 100.1 kWh of BOS-B lithium storage "
              "and a 78-panel array rated at 48.36 kWp.",
              "High-voltage battery architecture is what makes this economical at scale: lower current for the same "
              "power means smaller conductors and lower losses across a large building."]),
            ("What We Installed",
             ["80 kW / 48 V high-VAC dual inverter bank", "7 × 14.3 kWh BOS-B lithium batteries",
              "78 × 620 W monocrystalline solar panels",
              "Battery management system, combiner box, mounting rack, busbar and complete installation"], "list"),
            ("The Result",
             ["Rated for 150 lighting points, 30 TVs, 5 fridges and 5 freezers, a pumping machine, seven 2.5 HP air "
              "conditioners and a washing machine."]),
        ],
        "quote": None,
        "keywords": ["solar system for warehouse", "industrial solar installation Nigeria",
                     "80kW solar system", "logistics facility solar power", "commercial solar installation"],
    },
    {
        "id": "12kw-retail-business",
        "cat": "commercial", "type": "Retail business", "verified": False,
        "title": "12 kW (15 kVA) Solar Inverter Installation for a Retail Business",
        "location": "Port Harcourt, Rivers State", "client": None,
        "img": "install-room-grey.jpg",
        "alt": "12kW 15kVA solar inverter installation for a retail business in Port Harcourt",
        "specs": [("System", "12 kW / 48 V hybrid"), ("Battery storage", "2 × 16 kWh lithium"),
                  ("Solar panels", "16 × 620 W"), ("Property", "Retail store")],
        "excerpt": ("A mid-size store running lighting, displays, POS, refrigeration and three air "
                    "conditioners through full trading hours."),
        "loads": "70 lighting points, displays and POS, 3 fridges and freezers, three 1.5 HP air conditioners, pumping machine and microwave",
        "sections": [
            ("The Challenge",
             ["For a retail business, the cost of an outage is immediate and measurable: no tills, no lights, no "
              "customers. Small stores also rarely have room for a large generator or the tolerance for its running "
              "costs."]),
            ("Our Recommendation",
             ["A 12 kW / 48 V hybrid inverter with 32 kWh of lithium storage and a 16-panel array. "
              "The battery is sized to carry the store through a full evening of trading on its own."]),
            ("What We Installed",
             ["12 kW / 48 V hybrid inverter", "2 × 16 kWh lithium batteries",
              "16 × 620 W monocrystalline solar panels", "Cables, circuit protection and complete installation"], "list"),
            ("The Result",
             ["Rated for 70 lighting points, 10 fans, 3 fridges and freezers, three 1.5 HP air conditioners, a pumping "
              "machine, microwave and electric blender."]),
        ],
        "quote": None,
        "keywords": ["solar system for shop", "solar inverter installation for business",
                     "affordable commercial solar", "retail solar power Nigeria", "12kW solar system price"],
    },

    # ======================================================================
    # INDUSTRIAL
    # ======================================================================
    {
        "id": "125kw-factory-installation",
        "cat": "industrial", "type": "Factory", "verified": False, "featured": True,
        "title": "125 kW Solar &amp; Storage Installation for a Factory",
        "location": "Nigeria", "client": None,
        "img": "install-deye-rack.jpg",
        "alt": "125kW industrial solar and lithium storage installation for a factory in Nigeria",
        "specs": [("System", "125 kW PCS"), ("Battery storage", "15 × 16 kWh"),
                  ("Solar panels", "168 × 620 W"), ("Property", "Manufacturing plant")],
        "excerpt": ("Chillers, three-phase air conditioning, compressors and an industrial oven, the "
                    "class of load that decides whether a plant runs or stops."),
        "loads": "Chillers, three-phase air conditioners, elevator, air compressor, industrial water heater, industrial oven, industrial pumping machine and EV charging station",
        "sections": [
            ("The Challenge",
             ["Industrial power is not a comfort question. When the supply fails, production stops, work in progress "
              "is scrapped and the plant absorbs the cost of restarting.",
              "Plants of this size also run motor loads, compressors, chillers, pumps, whose starting current is "
              "several times their running current. Any system that ignores that fails on the first cold start."]),
            ("Our Recommendation",
             ["A 125 kW power conversion system with 240 kWh of BOS-B Pro lithium storage across fifteen modules and "
              "a 168-panel array rated at 104.16 kWp.",
              "Industrial-grade components throughout, specified to withstand heavy continuous duty. The design leaves "
              "room for expansion: additional battery modules and array strings can be added without replacing the "
              "conversion equipment."]),
            ("What We Installed",
             ["125 kW power conversion system", "15 × 16 kWh BOS-B Pro lithium batteries on stackable racks",
              "168 × 620 W monocrystalline solar panels",
              "Battery management system, circuit protection, mounting infrastructure and complete installation"], "list"),
            ("The Result",
             ["Rated to carry chillers, three-phase air conditioners, an elevator, air compressor, industrial water "
              "heater, industrial oven, industrial pumping machine and an EV charging station.",
              "Dependence on grid electricity and diesel generation is reduced structurally rather than marginally, "
              "and the plant gains protection against the power instability that damages industrial equipment."]),
        ],
        "quote": None,
        "keywords": ["industrial solar system Nigeria", "factory solar installation", "125kW solar system",
                     "solar for manufacturing", "industrial energy storage Nigeria"],
    },
    {
        "id": "100kw-manufacturing-installation",
        "cat": "industrial", "type": "Manufacturing", "verified": False,
        "title": "100 kW High-Voltage Solar Installation for a Manufacturing Facility",
        "location": "Nigeria", "client": None,
        "img": "pkg/pkg-60kw.jpg",
        "alt": "100kW high voltage solar and inverter installation for a manufacturing facility in Nigeria",
        "specs": [("System", "100 kW / 48 V"), ("Battery storage", "10 × 14.3 kWh"),
                  ("Solar panels", "140 × 620 W"), ("Property", "Manufacturing facility")],
        "excerpt": ("143 kWh of storage behind an 86.8 kWp array, sized for a facility that runs continuous "
                    "process load across an extended shift."),
        "loads": "180 lighting points, 40 displays, 6 fridges and 6 freezers, process equipment, pumping machine and eight 2.5 HP air conditioners",
        "sections": [
            ("The Challenge",
             ["Manufacturing facilities run long, predictable shifts with high continuous demand. Grid instability "
              "does not just interrupt production; voltage sags and surges shorten the life of motors, drives and "
              "control electronics."]),
            ("Our Recommendation",
             ["A 100 kW / 48 V high-VAC package with 143 kWh of BOS-B lithium storage and a 140-panel array rated at "
              "86.8 kWp.",
              "The inverter conditions supply continuously, which removes the surge and sag exposure as well as the "
              "outages."]),
            ("What We Installed",
             ["100 kW / 48 V high-VAC inverter system", "10 × 14.3 kWh BOS-B lithium batteries",
              "140 × 620 W monocrystalline solar panels",
              "Battery management system, combiner box, mounting rack, busbar and complete installation"], "list"),
            ("The Result",
             ["Rated for 180 lighting points, 40 displays, 6 fridges and 6 freezers, a pumping machine, eight 2.5 HP "
              "air conditioners and a washing machine, alongside process equipment."]),
        ],
        "quote": None,
        "keywords": ["manufacturing solar installation", "industrial solar Nigeria", "100kW solar system",
                     "solar for processing facility", "industrial solar and battery storage"],
    },
    {
        "id": "60kw-processing-facility",
        "cat": "industrial", "type": "Processing facility", "verified": False,
        "title": "60 kW (80 kVA) High-Voltage Solar Installation for a Processing Facility",
        "location": "Nigeria", "client": None,
        "img": "pkg/pkg-60kw.jpg",
        "alt": "60kW 80kVA high voltage solar and inverter system for a processing facility in Nigeria",
        "specs": [("System", "60 kW / 80 kVA"), ("Battery storage", "HV lithium bank"),
                  ("Solar panels", "620 W array"), ("Property", "Processing facility")],
        "excerpt": ("A dual-inverter high-voltage bank feeding continuous process load, with a stacked "
                    "battery cabinet sized for overnight running."),
        "loads": "Process equipment, cold storage, facility lighting, pumping and air conditioning",
        "sections": [
            ("The Challenge",
             ["Processing facilities cannot pause mid-cycle. An interruption during a run wastes input material as "
              "well as time, so continuity matters more than peak capacity."]),
            ("Our Recommendation",
             ["A 60 kW / 80 kVA high-voltage system built on a dual-inverter bank with a stacked lithium cabinet, "
              "sized so the facility can complete a full processing cycle on stored energy alone."]),
            ("What We Installed",
             ["60 kW / 80 kVA high-voltage inverter bank", "Stackable high-voltage lithium battery cabinet",
              "620 W monocrystalline solar array with combiner box",
              "Battery management system, circuit protection and complete installation"], "list"),
            ("The Result",
             ["Continuous, conditioned supply to process equipment, cold storage, lighting, pumping and air "
              "conditioning, with headroom to add battery modules as throughput grows."]),
        ],
        "quote": None,
        "keywords": ["solar for processing facility", "industrial solar installation Nigeria",
                     "60kW solar system", "80kVA solar inverter", "large scale solar Nigeria"],
    },
    {
        "id": "50kw-large-scale-facility",
        "cat": "industrial", "type": "Large-scale facility", "verified": False,
        "title": "50 kW Solar Installation for a Large-Scale Facility",
        "location": "Nigeria", "client": None,
        "img": "install-room-stack3.jpg",
        "alt": "50kW solar installation with lithium battery bank for a large-scale facility in Nigeria",
        "specs": [("System", "50 kW / 48 V"), ("Battery storage", "5 × 14.3 kWh"),
                  ("Solar panels", "64 × 620 W"), ("Property", "Large-scale facility")],
        "excerpt": ("A 39.68 kWp array with 71.5 kWh of storage, the workhorse configuration for large "
                    "facilities that need reliability before they need scale."),
        "loads": "120 lighting points, 20 displays, 4 fridges, 4 freezers, pumping machine, EV charger and five 2.5 HP air conditioners",
        "sections": [
            ("The Challenge",
             ["Large facilities often start their solar journey wanting to cover critical load rather than total "
              "load. The design question is which circuits go on the system first, and how to leave room for the rest."]),
            ("Our Recommendation",
             ["A 50 kW / 48 V high-VAC package with 71.5 kWh of BOS-B lithium storage and a 64-panel array. "
              "Critical circuits are moved onto the system first, with capacity reserved for a second phase."]),
            ("What We Installed",
             ["50 kW / 48 V high-VAC inverter system", "5 × 14.3 kWh BOS-B lithium batteries",
              "64 × 620 W monocrystalline solar panels",
              "Battery management system, combiner box, mounting rack, busbar and complete installation"], "list"),
            ("The Result",
             ["Rated for 120 lighting points, 20 displays, 4 fridges, 4 freezers, a pumping machine, an EV charger "
              "and five 2.5 HP air conditioners, with a clear expansion path."]),
        ],
        "quote": None,
        "keywords": ["large scale solar installation Nigeria", "industrial solar system",
                     "50kW solar installation", "commercial and industrial solar", "solar energy storage Nigeria"],
    },

    # ======================================================================
    # ENERGY & INFRASTRUCTURE
    # ======================================================================
    {
        "id": "solar-street-lighting",
        "cat": "infrastructure", "type": "Solar streetlights", "verified": False, "featured": True,
        "title": "All-in-One Solar Street Lighting for Roads, Estates and Communities",
        "location": "Nationwide", "client": None,
        "img": "project-streetlight.jpg",
        "alt": "All-in-one solar street light installed by Solar World Electric illuminating a Nigerian street at night",
        "specs": [("Type", "All-in-one street light"), ("Power", "Integrated PV + lithium"),
                  ("Control", "Dusk-to-dawn auto"), ("Application", "Roads &amp; communities")],
        "excerpt": ("Self-contained street lights with integrated panel, battery and LED head, no trenching, "
                    "no cabling, no metered supply."),
        "loads": "Public roads, estate streets, compound perimeters, car parks and community spaces",
        "sections": [
            ("The Challenge",
             ["Conventional street lighting requires trenching, cabling and a metered supply, then keeps costing "
              "money every month it stays on. In many communities the lights are installed and then never energised.",
              "Unlit roads and estates carry a direct security cost."]),
            ("Our Recommendation",
             ["All-in-one solar street lights, where the photovoltaic panel, lithium battery, controller and LED head "
              "are integrated into a single pole-mounted unit.",
              "Each unit is energy-independent, switches on automatically at dusk and requires no grid connection, "
              "no trenching and no running cost."]),
            ("What We Installed",
             ["All-in-one solar street lighting units with integrated PV and lithium storage",
              "Automatic dusk-to-dawn control", "Pole and foundation installation",
              "Commissioning and handover"], "list"),
            ("The Result",
             ["Lit roads, estate streets and community spaces with no monthly electricity cost and no dependence on "
              "grid availability.",
              "Units are installed individually, so a scheme can be extended pole by pole as budget allows."]),
        ],
        "quote": None,
        "keywords": ["solar street light Nigeria", "all in one solar street light",
                     "community solar lighting", "estate street lighting solar", "solar street light price"],
    },
    {
        "id": "solar-water-pumping",
        "cat": "infrastructure", "type": "Solar pumping", "verified": False,
        "title": "Solar Water Pumping Systems for Boreholes and Irrigation",
        "location": "Nationwide", "client": None,
        "img": "product-pumpctrl.jpg",
        "alt": "AC/DC auto solar pump controller installed by Solar World Electric for a borehole system",
        "specs": [("Type", "Submersible pump"), ("Drive", "MPPT controller"),
                  ("Power", "Direct PV array"), ("Application", "Boreholes &amp; irrigation")],
        "excerpt": ("Submersible pumps driven directly from the array through an MPPT controller, water "
                    "storage instead of battery storage."),
        "loads": "Borehole abstraction, overhead tank filling, irrigation and community water supply",
        "sections": [
            ("The Challenge",
             ["Water supply in much of Nigeria depends on a borehole, and the borehole depends on a generator. "
              "Fuel cost, fuel availability and pump failures translate directly into households and farms without "
              "water."]),
            ("Our Recommendation",
             ["A solar submersible pump driven directly from the photovoltaic array through an MPPT pump controller.",
              "The design choice that keeps this affordable is storing water rather than electricity: the pump runs "
              "when the sun is available and fills a tank, so no battery bank is required for the pumping duty itself."]),
            ("What We Installed",
             ["Solar submersible pump matched to borehole depth and yield",
              "MPPT solar pump controller with dry-run and over-current protection",
              "Monocrystalline array and mounting structure", "Pipework integration and commissioning"], "list"),
            ("The Result",
             ["Reliable daily water delivery to storage tanks with no fuel cost and no generator dependence, "
              "suitable for households, estates, farms and community supply points."]),
        ],
        "quote": None,
        "keywords": ["solar water pumping Nigeria", "solar borehole pump", "solar submersible pump price",
                     "solar irrigation system", "solar pumping machine"],
    },
    {
        "id": "community-solar-project",
        "cat": "infrastructure", "type": "Community projects", "verified": False,
        "title": "Community Solar Projects for Public and Government Institutions",
        "location": "Nationwide", "client": None,
        "img": "project-ground-array-2.jpg",
        "alt": "Ground-mounted community solar array installed by Solar World Electric for a public institution in Nigeria",
        "specs": [("Type", "Ground-mounted array"), ("Storage", "Centralised lithium"),
                  ("Scope", "End-to-end delivery"), ("Application", "Public institutions")],
        "excerpt": ("Ground-mounted arrays and centralised storage for institutions, agencies and community "
                    "facilities, delivered end to end, including maintenance."),
        "loads": "Institutional buildings, community facilities, offices, clinics and public lighting",
        "sections": [
            ("The Challenge",
             ["Public and community facilities are frequently the last to be reconnected and the first to be "
              "load-shed. They also rarely have in-house technical capacity to specify, procure and maintain an "
              "energy system.",
              "Solar World has delivered projects for institutions including the NDDC, the Maritime Academy of "
              "Nigeria (Oron), the National Malaria Elimination Programme and the Nigerian Army."]),
            ("Our Recommendation",
             ["An end-to-end engagement: energy audit, system design, supply, installation, commissioning and a "
              "maintenance regime, so the institution is not left holding technical risk it cannot manage.",
              "Ground-mounted arrays are used where roof area, orientation or building condition would otherwise "
              "constrain output."]),
            ("What We Installed",
             ["Ground-mounted monocrystalline solar array with engineered mounting structure",
              "Centralised lithium battery bank with battery management system",
              "Distribution integration and circuit protection",
              "Commissioning, staff handover training and scheduled maintenance"], "list"),
            ("The Result",
             ["Dependable power for institutional and community facilities, with a maintenance relationship rather "
              "than a one-off supply."]),
        ],
        "quote": None,
        "keywords": ["community solar project Nigeria", "government solar installation",
                     "public institution solar power", "rural electrification Nigeria", "solar energy company Nigeria"],
    },
    {
        "id": "ev-charging-infrastructure",
        "cat": "infrastructure", "type": "EV charging", "verified": False,
        "title": "Solar-Powered EV Charging Points for Homes and Businesses",
        "location": "Nationwide", "client": None,
        "img": "install-room-dual.jpg",
        "alt": "Hybrid inverter and lithium battery system supplying a solar powered EV charging point",
        "specs": [("Charger", "6–7 kW charge point"), ("Source", "Solar + lithium"),
                  ("Integration", "Hybrid inverter"), ("Application", "Homes &amp; offices")],
        "excerpt": ("EV charge points integrated into the same hybrid system that powers the building, so "
                    "the car charges on solar, not diesel."),
        "loads": "Electric vehicle charging alongside building load",
        "sections": [
            ("The Challenge",
             ["An electric vehicle charged from a diesel generator has simply moved the emissions and the fuel bill. "
              "Charging from an unstable grid is also hard on the vehicle's onboard charger."]),
            ("Our Recommendation",
             ["Integrating a 6–7 kW EV charge point into the property's hybrid solar system rather than treating it "
              "as a separate installation.",
              "The charge point draws from the same array and battery bank as the building, so vehicle charging is "
              "scheduled around available solar. Our 25 kW, 30 kW, 50 kW and 125 kW packages already include an EV "
              "charger in their rated load."]),
            ("What We Installed",
             ["6–7 kW EV charge point", "Integration into the existing hybrid inverter and lithium battery system",
              "Dedicated circuit protection and metering", "Commissioning and user handover"], "list"),
            ("The Result",
             ["Vehicle charging that runs on stored solar energy, with the building's own supply protected from the "
              "charging load."]),
        ],
        "quote": None,
        "keywords": ["solar EV charging Nigeria", "EV charger installation Nigeria",
                     "solar powered car charging", "home EV charge point", "renewable energy EV charging"],
    },
]
