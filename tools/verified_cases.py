# -*- coding: utf-8 -*-
"""
Verified case studies, transcribed from the business's own case-study document.

Every fact here (client, location, system specification, testimonial) was
supplied by Solar World. These entries carry `verified: True`.

Where the document marks a quote as a suggested direction rather than the
customer's own words, that is recorded in `quote_status` and surfaced on the
page, so nothing reads as a real quotation until the customer confirms it.
"""

VERIFIED = [

    # ======================================================================
    # 1. 16 kW Residential Airbnb
    # ======================================================================
    {
        "id": "16kw-residential-airbnb",
        "cat": "residential",
        "type": "Airbnb / Short-stay accommodation",
        "verified": True,
        "featured": True,
        "title": "16 kW Residential Solar Installation for a Two-Bedroom Airbnb",
        "location": None,
        "client": None,
        "img": "cs-16kw-airbnb.jpg",
        "alt": "16 kW residential solar installation with hybrid inverter and two lithium batteries for a two-bedroom Airbnb apartment",
        "specs": [
            ("System", "16 kW inverter"),
            ("Battery storage", "2 x 16 kWh lithium"),
            ("Solar panels", "20 x 620 W"),
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
              "The property had three air conditioners: two 1.5 HP AC units and one 3 HP AC unit. "
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
              "2 x 16 kWh lithium batteries",
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

    # ======================================================================
    # 2. 20 kW Residential, high-consumption home
    # ======================================================================
    {
        "id": "20kw-high-consumption-home",
        "cat": "residential",
        "type": "Large family home",
        "verified": True,
        "featured": True,
        "title": "20 kW Residential Solar &amp; Battery Installation for a High-Consumption Home",
        "location": None,
        "client": None,
        "img": "cs-20kw-home.jpg",
        "alt": "20 kW residential solar and battery installation with a Deye hybrid inverter and three 16 kWh lithium batteries",
        "specs": [
            ("System", "20 kW inverter"),
            ("Battery storage", "3 x 16 kWh lithium"),
            ("Solar panels", "36 x 620 W"),
            ("Property", "Large family home"),
        ],
        "excerpt": ("Five air conditioners and a household about to get busier. The family wanted a "
                    "permanent energy solution, not another backup box, so we sized for the load after "
                    "sunset rather than the load on paper."),
        "loads": ("5 air conditioners (two 1.5 HP, two 2 HP, one 1 HP), microwave, fridges, freezers, "
                  "television and washing machine"),
        "sections": [
            ("The Challenge",
             ["The customer's energy requirements were significantly higher than those of an average "
              "residential property.",
              "With children returning home for the summer, the family anticipated increased electricity "
              "consumption across the house. Multiple air conditioners would be operating, household "
              "appliances would be used more frequently, and the family wanted dependable electricity "
              "without returning to the recurring expense and noise associated with generator use.",
              "The customer was looking for something beyond temporary backup. They wanted a more "
              "permanent energy solution for the home.",
              "Their required air-conditioning load included two 1.5 HP AC units, two 2 HP AC units and "
              "one 1 HP AC unit, alongside a microwave, fridges, freezers, television and washing machine.",
              "The customer also wanted sufficient battery capacity to support substantial night-time "
              "usage, with multiple AC units expected to remain operational after sunset."]),
            ("The Solar World Approach",
             ["Rather than treating the system as a basic backup installation, Solar World's "
              "recommendation considered the customer's expected consumption and the amount of energy "
              "required after sunset.",
              "The substantial battery bank was particularly important because the customer wanted "
              "meaningful backup capacity during periods when solar generation was unavailable."]),
            ("What We Installed",
             ["20 kW inverter",
              "3 x 16 kWh lithium batteries",
              "36 units of 620 W solar panels",
              "Installation and configuration"], "list"),
            ("The Result",
             ["The family has been able to enjoy the system without relying on their generator in the way "
              "they previously did. Their generator, according to the customer, has effectively become a "
              "much less-used piece of equipment.",
              "And there is another benefit that matters in a family home: silence. Instead of a generator "
              "starting whenever the grid supply fails, the inverter system takes over without introducing "
              "the noise and fumes associated with conventional backup generation."]),
            ("Why This Project Matters",
             ["This is a strong example of how residential solar system design needs to account for "
              "lifestyle, not simply the number of appliances in a house.",
              "A home with multiple air conditioners and significant night-time consumption requires a "
              "different approach from a smaller residential installation."]),
        ],
        "quote": ("We were spending far too much on fuel and we knew the family's electricity needs would "
                  "increase once our kids came home on long break. Since installing the solar system, we "
                  "don't have to think about switching on the generator every time the power goes out. "
                  "The generator is practically sitting there unused."),
        "quote_status": None,
        "keywords": ["20 kW solar system for home", "solar system for large homes",
                     "home solar installation Nigeria", "solar inverter for multiple ACs",
                     "lithium battery backup for home", "solar system for five ACs"],
    },

    # ======================================================================
    # 3. 30 kW High-voltage, shopping complex
    # ======================================================================
    {
        "id": "30kw-shopping-complex",
        "cat": "commercial",
        "type": "Shopping facility",
        "verified": True,
        "featured": False,
        "title": "30 kW High-Voltage Solar &amp; Battery System for a Shopping Complex",
        "location": "M.I Ahmad Plaza, Wuse 2, Abuja",
        "client": None,
        "img": "cs-30kw-shopping.jpg",
        "alt": "30 kW high voltage solar and battery system with a Deye battery rack installed at a shopping complex in Wuse 2 Abuja",
        "specs": [
            ("System", "30 kW high-voltage"),
            ("Battery storage", "64 kWh"),
            ("Solar panels", "36 x 620 W"),
            ("Facility", "Shopping complex"),
        ],
        "excerpt": ("Multiple businesses under one roof, each losing money the moment the lights go out. "
                    "A high-voltage system now sits between grid failure and the generator."),
        "loads": "Retail lighting, shop equipment, food-outlet refrigeration and common-area services",
        "sections": [
            ("The Challenge",
             ["A shopping complex has a different energy profile from a residential property.",
              "There are multiple businesses operating under one roof. Customers come and go throughout "
              "the day. Shops need lighting. Retailers need their equipment operational. Food businesses "
              "depend on refrigeration and other electrical appliances.",
              "For these businesses, a power interruption is not simply inconvenient. It interrupts business.",
              "The shopping complex already had a generator available as backup. However, the management "
              "wanted another layer of energy security that could take over during power interruptions and "
              "reduce the amount of time businesses had to depend on the generator.",
              "The goal was straightforward: keep the complex operational and minimise downtime."]),
            ("Why a High-Voltage System?",
             ["For larger commercial applications, system architecture becomes increasingly important.",
              "Solar World recommended a 30 kW high-voltage system with 64 kWh of battery storage, "
              "designed around the complex's commercial energy requirements.",
              "High-voltage battery systems are particularly suited to larger installations where higher "
              "energy demands require an appropriate system architecture."]),
            ("What We Installed",
             ["30 kW high-voltage inverter system",
              "64 kWh battery bank",
              "36 units of 620 W solar panels",
              "Commercial electrical integration",
              "System commissioning and configuration"], "list"),
            ("The Result",
             ["The installation gives the shopping complex an additional source of dependable electricity "
              "between grid availability and generator operation. For the businesses operating inside the "
              "complex, this means fewer disruptions to everyday activities.",
              "A customer browsing a shop does not need to know whether the grid has gone off. A restaurant "
              "does not need to stop serving because the lights went out. A retailer does not have to "
              "immediately reach for the generator switch.",
              "The energy system works quietly in the background."]),
            ("Why This Project Matters",
             ["This project demonstrates how Solar World approaches commercial solar installation "
              "differently from residential installations. A commercial energy system has to consider "
              "multiple users, business continuity, different load patterns, peak consumption, battery "
              "storage, generator integration and operational requirements.",
              "The goal is not simply to put solar on the building. It is to design an energy system "
              "around how the business operates."]),
        ],
        "quote": ("This project was majorly for continuity. We have different businesses operating here, "
                  "and we couldn't afford for power interruptions to keep affecting every paying tenant. "
                  "The solar system adds another level of reliability."),
        "quote_status": None,
        "keywords": ["commercial solar installation", "solar system for shopping complex",
                     "solar inverter installation for businesses", "30 kW solar system",
                     "high-voltage solar system Nigeria", "commercial battery storage"],
    },

    # ======================================================================
    # 4. 50 kW Hotel, Bistro Hotel Surulere
    # ======================================================================
    {
        "id": "50kw-bistro-hotel",
        "cat": "commercial",
        "type": "Hotel",
        "verified": True,
        "featured": False,
        "title": "50 kW Solar &amp; Battery System for a 14-Room Hotel",
        "location": "Bistro Hotel, Surulere, Lagos",
        "client": "Bistro Hotel",
        "img": "cs-50kw-bistro-hotel.jpg",
        "alt": "50 kW solar and battery system with a high voltage lithium battery rack installed at Bistro Hotel, Surulere Lagos",
        "specs": [
            ("System", "50 kW inverter"),
            ("Battery storage", "70 kWh"),
            ("Solar panels", "46 x 620 W"),
            ("Facility", "14-room hotel"),
        ],
        "excerpt": ("A guest noticed the hotel always seemed to have electricity, and had no idea it was "
                    "running on solar. In hospitality, that is the whole point."),
        "loads": "14 guest rooms, multiple 1.5 HP air conditioners, lighting, refrigeration and common hotel appliances",
        "sections": [
            ("The Challenge",
             ["Hospitality businesses have a unique responsibility. When someone pays for a hotel room, "
              "they are paying for more than four walls and a bed. They are paying for comfort, "
              "convenience and reliability.",
              "A guest expects to be able to sleep comfortably, use their air conditioner, charge their "
              "devices, watch television and access the basic services associated with their stay.",
              "A power interruption that causes a hotel room to become uncomfortable immediately becomes "
              "a customer-experience problem.",
              "For this 14-room hotel, management wanted a more dependable alternative to constant "
              "generator dependence."]),
            ("Understanding the Load",
             ["The hotel had approximately 14 rooms, alongside common hotel appliances and operational loads.",
              "The Solar World team assessed the expected energy requirements and recommended a 50 kW "
              "inverter with 70 kWh of battery storage and 46 solar panels.",
              "The system was designed to accommodate substantial hotel loads, including multiple air "
              "conditioners and common appliances. Under the customer's operating requirements, the system "
              "could comfortably support multiple 1.5 HP air conditioners alongside other essential loads."]),
            ("What We Installed",
             ["50 kW inverter",
              "70 kWh battery storage",
              "46 units of 620 W solar panels",
              "Complete solar installation",
              "System integration and commissioning"], "list"),
            ("The Moment That Defined the Installation",
             ["One of the most interesting things about this project happened after installation.",
              "A guest staying at the hotel experienced the property's electricity supply without "
              "realising there had been a change in the source of power. The guest reportedly commented "
              "on how consistently the hotel had electricity and how often the lights seemed to remain "
              "available. The hotel staff then explained that the property had installed a solar power system.",
              "That reaction captures something important about a successful energy installation: the best "
              "energy system is sometimes the one the customer does not notice. When everything works, "
              "guests do not think about the inverter. They simply experience the comfort."]),
            ("The Result",
             ["The hotel has continued to operate with the installed system and has expressed satisfaction "
              "with its performance.",
              "The positive experience has also influenced the hotel's interest in deploying similar "
              "systems across other properties."]),
            ("Why This Project Matters",
             ["This installation demonstrates the relationship between energy reliability and hospitality. "
              "For hotels, reliable electricity affects guest comfort, air conditioning, lighting, "
              "refrigeration, entertainment, front-desk operations, laundry, food service and overall "
              "guest perception.",
              "Solar therefore becomes more than an electricity source. It becomes part of the hotel's "
              "customer experience infrastructure."]),
        ],
        "quote": ("One of our guests actually commented that we seemed to have electricity all the time, "
                  "considering the area the hotel was located in. They didn't even realise we were running "
                  "on solar. For a hotel, that is exactly the kind of experience we want our guests to have."),
        "quote_status": None,
        "keywords": ["solar system for hotels", "hotel solar installation Nigeria", "50 kW solar system",
                     "commercial solar power", "solar battery storage for hotels", "solar inverter for hotel"],
    },

    # ======================================================================
    # 5. 80 kW Finance company, Brook Finance Lekki
    # ======================================================================
    {
        "id": "80kw-brook-finance",
        "cat": "commercial",
        "type": "Office",
        "verified": True,
        "featured": True,
        "title": "80 kW Solar &amp; Battery System for a Finance Company",
        "location": "Brook Finance, Lekki, Lagos",
        "client": "The Brook Finance Company Limited",
        "img": "cs-80kw-brook-finance.jpg",
        "alt": "80 kW solar inverter and 169 kWh lithium battery rack installed for Brook Finance in Lekki Lagos",
        "specs": [
            ("System", "80 kW inverter"),
            ("Battery storage", "169 kWh"),
            ("Solar panels", "128 x 725 W"),
            ("Application", "Corporate office"),
        ],
        "excerpt": ("A finance company that runs the numbers for a living looked at what generator fuel "
                    "was actually costing, and moved 169 kWh of its energy infrastructure under its own control."),
        "loads": ("Computers, networking and communications equipment, security infrastructure, "
                  "air conditioning and office equipment"),
        "sections": [
            ("The Challenge",
             ["Financial institutions operate in an environment where reliability matters.",
              "Employees depend on computers, networking equipment and communications systems. Customers "
              "depend on uninterrupted service. Security infrastructure needs electricity. Air conditioning "
              "and office equipment contribute significantly to the building's overall energy demand.",
              "The finance company already had access to generator power, but generator dependence created "
              "an ongoing operational burden. Fuel expenditure is unpredictable. Maintenance is recurring. "
              "Noise is disruptive.",
              "And when an organisation has to continuously budget for generator fuel, its energy "
              "expenditure becomes tied to the availability and cost of fuel. The company wanted a more "
              "structured approach."]),
            ("The Decision to Invest in Solar",
             ["The objective was not necessarily to eliminate every other source of electricity overnight.",
              "The objective was to introduce a reliable energy source that could reduce dependence on "
              "generator power and provide greater predictability around electricity operations.",
              "Solar World recommended an 80 kW system with 169 kWh of battery storage and 128 solar panels."]),
            ("What We Installed",
             ["80 kW inverter system",
              "169 kWh battery bank",
              "128 units of 725 W solar panels",
              "Commercial electrical integration",
              "System configuration and commissioning"], "list"),
            ("Why Battery Storage Was Important",
             ["Solar generation and electricity consumption do not always occur at the same time.",
              "A commercial office can consume electricity after sunset, during periods of low solar "
              "production and during grid interruptions.",
              "The substantial battery capacity therefore provides the organisation with stored energy to "
              "support its operations beyond the hours of direct solar generation."]),
            ("The Result",
             ["The finance company has been operating with the system and has expressed satisfaction with "
              "its performance.",
              "More importantly, the organisation has been able to develop a more deliberate approach to "
              "energy management. Instead of viewing electricity solely as something purchased from the "
              "grid or generated by a diesel generator, the company now has a significant portion of its "
              "energy infrastructure under its own control."]),
            ("Why This Project Matters",
             ["This is a strong example of commercial solar for corporate offices.",
              "For large businesses, the conversation is not simply how much solar costs. It becomes: "
              "what does unreliable power cost our business over time?"]),
        ],
        "quote": ("With fuel, you don't always know what your energy costs are going to look like because "
                  "everything depends on how often you need the generator, and we are into finance, so we "
                  "know what will save us money in the long run, which will always be the better option. "
                  "Solar gives us another way to plan our energy."),
        "quote_status": None,
        "keywords": ["solar for finance companies", "commercial solar installation Nigeria",
                     "solar inverter installation for offices", "80 kW solar system",
                     "battery storage for businesses", "corporate solar power system"],
    },

    # ======================================================================
    # 6. 100 kW Fuel station, ENERGYMATICS Port Harcourt
    # ======================================================================
    {
        "id": "100kw-energymatics-fuel-station",
        "cat": "commercial",
        "type": "Fuel retail / Energy",
        "verified": True,
        "featured": False,
        "title": "100 kW Solar &amp; Battery System for a Fuel Station",
        "location": "ENERGYMATICS Filling Station, Port Harcourt",
        "client": "ENERGYMATICS LTD.",
        "img": "pkg/pkg-80kw.jpg",
        "alt": "High voltage solar inverter and lithium battery bank of the type installed for ENERGYMATICS filling station in Port Harcourt",
        "specs": [
            ("System", "100 kW inverter"),
            ("Battery storage", "139 kWh"),
            ("Solar panels", "124 panels"),
            ("Application", "Fuel station"),
        ],
        "excerpt": ("A business built on selling fuel realised it was spending heavily on fuel to make its "
                    "own electricity. It started smaller and grew the system to 100 kW."),
        "loads": "Forecourt lighting, fuel pumps, security systems, offices and refrigeration",
        "sections": [
            ("The Challenge",
             ["There is an interesting irony behind this project. The customer operates a business built "
              "around selling fuel. Yet fuel itself was becoming part of the energy problem.",
              "A fuel station requires electricity for lighting, pumps, security systems, offices, "
              "refrigeration and other operational equipment. Maintaining generator operations adds another "
              "layer of expenditure beyond the fuel sold to customers.",
              "There is the cost of diesel. There is generator servicing. There are repairs. There is "
              "noise. There is the inconvenience of continuously monitoring fuel consumption. And there is "
              "the uncertainty of future generator operating costs.",
              "The customer wanted a different approach."]),
            ("From Smaller Capacity to 100 kW",
             ["One of the most valuable aspects of this project is that the customer did not begin with "
              "the final 100 kW system. The installation evolved.",
              "The customer initially deployed a smaller inverter configuration and subsequently upgraded "
              "the system as its energy requirements and confidence in the solution increased.",
              "That progression demonstrates an important advantage of properly designed energy systems: "
              "solar infrastructure can evolve with the customer's requirements."]),
            ("What We Installed",
             ["100 kW inverter capacity",
              "139 kWh battery storage",
              "124 solar panels",
              "Commercial electrical integration and commissioning"], "list"),
            ("The Result",
             ["The fuel station now has a substantial solar and battery system supporting its operations.",
              "The result is not simply an alternative source of electricity. It represents a change in "
              "how the business thinks about energy expenditure.",
              "Instead of continuously purchasing fuel to generate electricity, the business has invested "
              "in infrastructure capable of generating and storing energy. The customer has reported "
              "satisfaction with the system and has continued to upgrade its energy infrastructure."]),
            ("Why This Project Matters",
             ["This project is particularly strong for demonstrating energy independence and scalability.",
              "It shows that a solar system does not necessarily have to be treated as a fixed, one-time "
              "configuration. A properly designed system can form part of a long-term energy strategy."]),
        ],
        "quote": ("It is interesting because we sell fuel, but we realised we were also spending a lot of "
                  "money buying fuel to generate our own electricity. Solar gave us a way to reduce that cycle."),
        "quote_status": "Suggested testimonial direction, to be replaced with the customer's actual wording.",
        "keywords": ["solar for filling stations", "solar system for fuel stations",
                     "commercial solar installation", "100 kW solar system Nigeria",
                     "solar battery system for businesses", "solar power for petrol stations"],
    },

    # ======================================================================
    # 7. 315 kVA Garden City Hotel, Port Harcourt
    # ======================================================================
    {
        "id": "315kva-garden-city-hotel",
        "cat": "commercial",
        "type": "Hotel",
        "verified": True,
        "featured": True,
        "title": "315 kVA Solar &amp; Battery System for Garden City Hotel, Port Harcourt",
        "location": "Port Harcourt, Rivers State",
        "client": "Garden City Hotel",
        "img": "cs-315kva-garden-city.jpg",
        "alt": "315 kVA solar inverter system and 480 kWh lithium battery banks installed for Garden City Hotel in Port Harcourt",
        "specs": [
            ("System", "315 kVA"),
            ("Battery storage", "480 kWh"),
            ("Solar panels", "208 x 620 W"),
            ("Application", "Large-scale hotel"),
        ],
        "excerpt": ("Our largest hospitality installation: 480 kWh of storage behind a 315 kVA system, "
                    "sized so guests never have to know what is happening behind the scenes."),
        "loads": ("Guest rooms, air conditioning, lighting, refrigeration and food service, elevators, "
                  "security systems and communications"),
        "sections": [
            ("The Challenge",
             ["For a major hotel, electricity is fundamental to the product being sold.",
              "A guest who books a hotel room expects comfort. They expect air conditioning. They expect "
              "lighting. They expect refrigeration and food services to function. They expect elevators, "
              "security systems, communications and other hotel infrastructure to remain operational.",
              "And perhaps most importantly, they do not want to know what is happening behind the scenes "
              "to keep the hotel running. They simply expect everything to work.",
              "For Garden City Hotel in Port Harcourt, the requirement was therefore significantly larger "
              "than a conventional residential or small commercial installation. The hotel needed a "
              "high-capacity energy solution capable of supporting the demands of a large hospitality "
              "operation while reducing the disruption associated with power interruptions."]),
            ("Designing for a Large Hospitality Facility",
             ["Solar World's response was a 315 kVA system with 480 kWh of battery capacity and 208 solar "
              "panels. The scale of the system reflects the scale of the hotel's energy requirements.",
              "Rather than approaching the project as a simple backup installation, the system was designed "
              "as a substantial component of the hotel's overall energy infrastructure."]),
            ("What We Installed",
             ["315 kVA inverter system",
              "480 kWh battery storage",
              "208 solar panels",
              "Large-scale commercial installation",
              "System integration and commissioning"], "list"),
            ("Why Energy Reliability Matters in Hospitality",
             ["Hotels do not have the luxury of simply telling guests that the electricity went off. "
              "The guest has already paid for the experience.",
              "An interruption affects their room, their comfort, their perception of the hotel and "
              "potentially their decision to return.",
              "For a hotel operating at scale, reliable energy therefore has a direct relationship with "
              "customer satisfaction and business continuity."]),
            ("The Solar World Solution",
             ["The installation gives Garden City Hotel a substantial combination of solar generation and "
              "battery storage.",
              "During periods of solar production, the panels contribute to the hotel's energy requirements "
              "while charging the battery system. The stored energy then provides another source of power "
              "when solar generation is unavailable.",
              "This creates a more structured energy ecosystem for a facility with substantial and "
              "continuous electricity requirements."]),
            ("The Result",
             ["Following installation, the hotel has expressed strong satisfaction with the system.",
              "The project has also generated interest in the solution beyond the original installation, "
              "including the possibility of recommending Solar World to others within the hospitality sector.",
              "And that is one of the strongest indicators of a successful commercial project: the customer "
              "is willing to put their reputation behind the solution."]),
            ("Why This Project Matters",
             ["Garden City Hotel represents the scale at which energy management becomes a strategic "
              "business decision.",
              "At this level, the conversation is no longer simply how to get backup power. It becomes: "
              "how do we build a more reliable energy infrastructure for a large hospitality operation? "
              "That distinction is precisely where large-scale solar and battery storage become valuable."]),
        ],
        "quote": ("Our guests shouldn't have to know when there is a power interruption. They are here to "
                  "enjoy the hotel, not worry about our electricity. The solar system has made a "
                  "significant difference to the way we manage our power."),
        "quote_status": "Suggested testimonial direction, to be replaced with the customer's actual wording.",
        "keywords": ["315 kVA solar system", "hotel solar installation Nigeria",
                     "large-scale solar installation Port Harcourt", "solar system for hotels",
                     "480 kWh battery storage", "commercial solar power Nigeria",
                     "high-capacity solar inverter"],
    },
]
