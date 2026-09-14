# Website corrections implementation plan

Goal: Apply the September 14 screenshot corrections and supplied Stratford article to the published website.
Architecture: Keep the Python static generator. Use one audited package catalog and one browser matcher for all three calculator interfaces. Keep documented prices separate from estimated runtime.
Sources: IMG_4619–IMG_4631, the three supplied price PDFs, and the user-supplied Stratford article.

- [x] Audit all price rows and complete packages against PDFs; add the missing Standard 15kVA solar row.
- [x] Make Deye, Solis and Standard charts visible via direct section links, downloads, and product-page links; render every row's included equipment and appliances explicitly.
- [x] Reproduce wrong calculator output for five lights; add regression cases for actual package specs/price, brand selection, battery requirements, unsupported appliances, zero inputs, and oversized demand. Implement a shared matcher in assets/js/package-matcher.js and generated assets/js/package-catalog.js; wire the home, full-page, and floating calculators.
- [x] Remove the About group photo; state 21 operations across three cities, split PH into five independent branches, correct SPAR, and remove general 125kW business limits in source copy/metadata.
- [x] Replace the large-facility entry with the supplied Stratford article; correct EV to 160kW; remove project editorial manufacturer labels while preserving price-chart brands.
- [x] Crop the review contact header and keyboard out of the displayed testimonial.
- [x] Update central management after the user resolves the Chioma conflict and identifies the pink-jacket profile; add Ejike using the existing business-supplied profile photo if no new file is present.
- [ ] Rebuild, check desktop/mobile screens and all calculator variants, review diffs, push to main under the existing publishing instruction, and verify production HTML/assets.

Do not invent person identities, unpublished prices, runtime guarantees, branch numbers or equipment details. Missing source counts require an engineer review, rather than silently unlimited capacity. Actual 125kW packages remain in pricing; broader business capability is 1MW and beyond.

Latest supplied PDFs are byte-identical to the audited charts. IMG_4640 identifies Alexia Ilo, Head of Business and Protocol, as the replacement for the removed Regional Director. IMG_4641 adds Kamsy Joe’Chubilo, Assistant, Head Legal and Compliance. Central management is Charles, Adanna, Alexia, Ejike, Favour, Gloria. The two new portraits use the supplied screenshots framed to show only their photographs; Ejike uses the previous website portrait. All 39 profiles are retained in the appropriate role groups.

Validation: 10 package matching tests; Playwright checks eight pages at 1440px and 390px, all three calculators, 54 visible chart rows, 32 complete package cards, team order, project facts, and local assets. Final review found and corrected the pricing article’s stale complete-system range.
