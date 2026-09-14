const assert=require('node:assert/strict');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const base=process.env.SOLAR_TEST_URL || 'http://127.0.0.1:8080/';
(async()=>{
 const browser=await chromium.launch();
 const page=await browser.newPage({reducedMotion:'reduce'});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 for(const width of [1440,390]){
  await page.setViewportSize({width,height:1000});
  for(const filename of ['pricing.html','products.html','about.html','contact.html','projects.html','reviews.html','calculator.html','index.html']){
   await page.goto(base+filename);
   await page.locator('.cfab').waitFor();
   assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,filename+' overflows at '+width);
   if(filename==='pricing.html'){
    for(const [line,count] of [['deye',20],['solis',12],['standard',22]]){
     const chart=page.locator('#chart-'+line);assert.equal(await chart.isVisible(),true);
     assert.equal(await chart.locator('tbody tr').count(),count);
     assert.equal((await chart.innerText()).includes('Same as above'),false);
     const pdf=await page.request.get(base+'assets/docs/'+line+'-price-chart.pdf');assert.equal(pdf.status(),200);
    }
   }
   if(filename==='products.html')assert.equal(await page.locator('.catalog-card').count(),32);
   if(filename==='about.html'){
    assert.equal(await page.locator('img[src$="team-group.jpg"]').count(),0);
    assert.match(await page.locator('.facts').first().innerText(),/21 across 3 cities/);
    assert.equal(await page.locator('.team__card').count(),39);
    assert.deepEqual(await page.locator('.team-group').first().locator('.team__name').allTextContents(),['Mr Charles Abia','Adanna Felix','Alexia Ilo','Ejike Okoli','Favour Yiliye Austine','Gloria Iwuchukwu']);
    assert.equal(await page.getByRole('heading',{name:'Chioma Uga',exact:true}).count(),0);
    assert.equal(await page.getByRole('heading',{name:'Kamsy Joe’Chubilo',exact:true}).count(),1);
   }
   if(filename==='contact.html'){
    const locations=await page.locator('#offices').innerText();
    assert.match(locations,/Port Harcourt \(5 branches\)/);assert.match(locations,/Sani Abacha 3/);assert.match(locations,/SPAR PH/);
   }
   if(filename==='projects.html'){
    const hotel=page.locator('[id="50kw-large-scale-facility"]');
    assert.equal(await hotel.getAttribute('data-cat'),'commercial');assert.match(await hotel.innerText(),/250 kW/);
    assert.match(await page.locator('#cs-50kw-large-scale-facility').innerText(),/480kWh/);
    assert.match(await page.locator('#ev-charging-infrastructure').innerText(),/160 kW/);
    assert.equal(await page.locator('.cs-article h3').filter({hasText:/^$/}).count(),0);
   }
   if(filename==='reviews.html'){
    const crops=page.locator('svg.review-crop');assert.equal(await crops.count(),7);const crop=crops.first();
    await crop.scrollIntoViewIfNeeded();await crop.screenshot({path:'/private/tmp/solar-review-crop-'+width+'.png'});
   }
   if(filename==='calculator.html'){
    await page.getByRole('button',{name:'Add one LED bulb / light point',exact:true}).click();
    let out=page.locator('#calcResult');let text=await out.innerText();
    for(const expected of ['3 kVA','2.5 kWh','4 × 460 W','₦2,350,000']) assert.ok(text.includes(expected),expected);
    await page.locator('#calcLine').selectOption('solis');assert.match(await out.innerText(),/₦6,870,000/);
    await page.locator('#calcLine').selectOption('deye');assert.match(await out.innerText(),/₦4,760,000/);
    await page.locator('#calcReset').click();assert.equal(await out.locator('[data-package-id]').count(),0);
    await page.getByRole('button',{name:'Add one Computer / office point',exact:true}).click();assert.match(await out.innerText(),/Engineer assessment needed/);
    await page.locator('#calcReset').click();await page.locator('#calcLine').selectOption('all');
    await page.getByRole('button',{name:'Add one LED bulb / light point',exact:true}).click();
    await out.scrollIntoViewIfNeeded();await out.screenshot({path:'/private/tmp/solar-full-calc-'+width+'.png'});
    await page.getByRole('button',{name:'Open the solar and finance calculator',exact:true}).click();
    await page.locator('.cfab').getByRole('button',{name:'Add one Light points',exact:true}).click();
    assert.match(await page.locator('#cfFoot').innerText(),/4 × 460 W/);
    await page.locator('#cfLine').selectOption('solis');assert.match(await page.locator('#cfFoot').innerText(),/14.3 kWh/);
    await page.locator('.cfab__panel').screenshot({path:'/private/tmp/solar-popup-calc-'+width+'.png'});
   }
   if(filename==='index.html'){
    const result=page.locator('#sizerOut');assert.equal(await result.locator('[data-package-id]').count(),1);
    await page.locator('#sizerHours').selectOption('6');await page.locator('#sizerLine').selectOption('solis');assert.equal(await result.locator('[data-package-id]').count(),1);
    assert.match(await result.innerText(),/Solis/);
   }
  }
  console.log('Passed desktop/mobile page and calculator checks at '+width+'px');
 }
 assert.deepEqual(errors,[]);await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
