const {test}=require('node:test');
const assert=require('node:assert/strict');
const {execFileSync}=require('node:child_process');
const path=require('node:path');
const catalog=JSON.parse(execFileSync('python3',['-c','import sys,json;sys.path.insert(0,"tools");from package_catalog import CATALOG;print(json.dumps(CATALOG))'],{cwd:path.join(__dirname,'..'),encoding:'utf8'}));
const matcher=require('../assets/js/package-matcher.js');
const choose=(counts,hours=10,line='all')=>matcher.recommend(catalog,counts,{hours,line});
test('five lights retain the published 3 kVA battery, panel wattage and price',()=>{
 const r=choose({lights:5});
 assert.equal(r.status,'matched');
 assert.equal(r.package.inverter_unit,'kVA'); assert.equal(r.package.inverter_rating,3);
 assert.equal(r.package.battery_kwh,2.5); assert.equal(r.package.panel_count,4);
 assert.equal(r.package.panel_watts,460); assert.equal(r.package.price,2350000);
});
test('each price line can supply its own smallest matching package',()=>{
 assert.equal(choose({lights:5},10,'deye').package.price,4760000);
 assert.equal(choose({lights:5},10,'solis').package.price,6870000);
 assert.equal(choose({lights:5},10,'standard').package.price,2350000);
});
test('an empty selection has no price or recommendation',()=>{
 assert.equal(choose({lights:0}).status,'empty');assert.equal(choose({}).package,null);
});
test('large unsupported loads require a custom assessment instead of the largest-priced tier',()=>{
 assert.equal(choose({lights:10000}).status,'custom');
 assert.equal(choose({office:2}).package,null);
 assert.equal(choose({ac2:1}).status,'custom');
});
test('three 1.5HP ACs use a documented three-AC package',()=>{
 const p=choose({ac15:3,lights:50,tv:6},1).package;
 assert.equal(p.id,'standard-8kw-16kwh-12panels');assert.equal(p.price,8230000);
});
test('longer backup picks actual larger storage and its associated price',()=>{
 const r=choose({lights:25},24,'standard');
 assert.equal(r.package.battery_kwh,15.33);assert.equal(r.package.price,6180000);
});
test('a shared refrigeration allowance never counts as one of each',()=>{
 const r=choose({fridge:1,freezer:1},1,'standard');
 assert.notEqual(r.package.id,'standard-3kva-2.5kwh-4panels');
 assert.equal(r.status,'review');
});
test('unnumbered loads are marked for review, never silently unlimited',()=>{
 assert.equal(choose({wash:1},1).status,'review');
 assert.equal(choose({wash:6},1).status,'custom');
});
test('invalid counts cannot create a quote',()=>{
 for(const counts of [{lights:-1},{lights:1.5},{lights:NaN}])assert.equal(choose(counts).status,'invalid');
});
test('source capacity uncertainty is retained for engineer confirmation',()=>{
 const r=choose({lights:5},10,'solis');
 assert.equal(r.status,'review');assert.ok(r.notes.some(n=>n.includes('confirm the inverter model')));
});
