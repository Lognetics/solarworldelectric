const assert = require('node:assert/strict');
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const base = process.env.SOLAR_TEST_URL || 'http://127.0.0.1:8080/';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({reducedMotion:'reduce'});
  for (const width of [1440, 390, 320]) {
    await page.setViewportSize({width, height:900});
    await page.goto(base + 'index.html');
    if (width < 1081) await page.locator('#navToggle').click();
    await page.locator('#navLinks').getByRole('link', {name:'Product Prices', exact:true}).click();
    assert.equal(new URL(page.url()).pathname, '/pricing.html', 'Product Prices must open the same charts as home pricing links');
    for (const line of ['deye', 'solis', 'standard']) {
      const chart = page.locator('#chart-' + line);
      const table = chart.locator('.ptable');
      if (width <= 760) {
        assert.equal(await chart.locator('.ptable-wrap').evaluate(el => el.scrollWidth > el.clientWidth + 1), false, line + ' requires sideways scrolling');
        for (const row of [table.locator('tbody tr').first(), table.locator('tbody tr').last()]) {
          for (const cell of await row.locator('td').all()) {
            const box = await cell.boundingBox();
            assert.ok(box.x >= 0 && box.x + box.width <= width + 1, line + ' cell clipped');
          }
        }
      }
    }
    if (width === 390) {
      await page.locator('#chart-deye .ptable tbody tr').first().scrollIntoViewIfNeeded();
      await page.screenshot({path:'/private/tmp/solar-mobile-price-followup.png'});
    }
    await page.goto(base + 'projects.html');
    for (const id of ['[id="80kw-brook-finance"]', '[id="cs-80kw-brook-finance"]']) {
      const text = await page.locator(id).innerText();
      assert.ok(text.includes('620 W')); assert.ok(!text.includes('725 W'));
    }
  }
  await page.setViewportSize({width:1000,height:1000});
  await page.goto(base + 'reviews.html');
  const cards = page.locator('.wa-card');
  assert.equal(await cards.count(),9);
  for (let i = 0; i < 9; i++) {
    const shot = cards.nth(i).locator('.wa-card__shot');
    await shot.scrollIntoViewIfNeeded();
    await shot.screenshot({path:'/private/tmp/solar-testimonial-'+i+'.png'});
  }
  await browser.close();
  console.log('Pricing navigation, mobile price rows, Brook Finance and testimonial screenshots checked.');
})().catch(error => {console.error(error);process.exit(1)});
