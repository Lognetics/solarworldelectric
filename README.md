# Solar World Electric Technology Ltd. — Website

A premium, multi-page redesign built with the company's real photography, brochure
content and brand identity (gold `#F9B000`, orange `#F7931A`, charcoal `#121212`,
green `#32B768`). Static HTML/CSS/JS — no build step required.

## Run it
Open `index.html` in any browser, or serve the folder:

```bash
cd site
python3 -m http.server 8080   # then visit http://localhost:8080
```

## Pages
| File | Purpose |
|------|---------|
| `index.html` | Home — hero, savings calculator, why-us, solutions, products, financing, projects, stats, testimonials, AI chat |
| `about.html` | Story, timeline, vision/mission, values, 37 team profiles grouped by role |
| `solutions.html` | Residential / Commercial / Industrial / Government + delivery process |
| `products.html` | Full-system explainer, product detail blocks, warranty table |
| `financing.html` | 7-step process, live repayment simulator, packages, FAQ |
| `projects.html` | Featured case studies + filterable project gallery |
| `calculator.html` | Smart solar sizing tool (kVA / battery / panels / cost) |
| `contact.html` | 9 office locations, map, booking form, WhatsApp |

## Assets
- `assets/css/styles.css` — full design system
- `assets/js/main.js` — nav, scroll-reveal, counters, all calculators, gallery filter, FAQ, chat
- `assets/img/` — real installation, team and showroom photos (logo recreated as `logo-mark.svg`)

## Notes
- Team portraits, names and roles come from the uploaded `Solar World Teams ` folder.
  The 37 profiles include Amina Addo Franka's PDF portrait and one entry for the two
  Favour Ogochukwu Ayozie photos. Profile details are maintained in `tools/content.py`;
  run `python3 tools/build.py` from `site/` after changing them.
- Showroom shots were extracted from the brochure PDF.
- Calculator outputs are indicative estimates; tune the constants in `main.js` to match
  current pricing before going live.
- The contact form is a front-end demo — connect it to your email/CRM endpoint to receive leads.
