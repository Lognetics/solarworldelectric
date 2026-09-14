/* Package specifications and prices come from the supplied price charts.
 * Watts/duty factors below are illustrative runtime assumptions, not chart ratings.
 * No runtime or simultaneous-operation guarantee is implied by an appliance list. */
(function (root, factory) {
  var api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.SolarPackages = api;
})(typeof window !== 'undefined' ? window : this, function () {
  'use strict';
  var loads = {
    lights:[12,1], fan:[75,.6], tv:[110,.35], fridge:[200,.4], freezer:[250,.45],
    ac1:[900,.55], ac15:[1250,.55], ac2:[1700,.55], ac25:[2100,.55],
    wash:[500,.08], microwave:[1200,.05], blender:[400,.05], pump:[750,.1],
    office:[150,.5], chiller:[1500,.5], sound:[250,.2], iron:[1100,.05],
    heater:[1500,.12], ev:[6000,.2], elevator:[5000,.15]
  };
  var aliases = {bulb:'lights',micro:'microwave',lift:'elevator'};
  function recommend(catalog, input, options) {
    options = options || {};
    var hours = options.hours == null ? 10 : Number(options.hours);
    var line = options.line || 'all';
    var counts = {}, keys = Object.keys(input), invalid = !Number.isFinite(hours) || hours <= 0 || hours > 24;
    keys.forEach(function (key) {
      var value=input[key], normalized=aliases[key] || key;
      if (!Number.isInteger(value) || value < 0) invalid=true;
      counts[normalized]=(counts[normalized] || 0)+value;
    });
    if (invalid) return {status:'invalid',package:null,notes:['Use whole appliance counts and a backup duration between 1 and 24 hours.']};
    keys=Object.keys(counts).filter(function(k){return counts[k]>0;});
    if(!keys.length) return {status:'empty',package:null,notes:[]};
    var connected=0, average=0;
    keys.forEach(function(k){if(loads[k]){connected+=counts[k]*loads[k][0];average+=counts[k]*loads[k][0]*loads[k][1];}});
    var requiredBattery=average*hours/1000/.9;
    var candidates=[];
    catalog.forEach(function(p){
      if(line!=='all' && p.line!==line) return;
      if(p.industrial || p.battery_kwh+1e-8<requiredBattery) return;
      var notes=(p.notes || []).slice(), handled={};
      (p.shared_limits || []).forEach(function(group){
        var total=group.keys.reduce(function(sum,k){return sum+(counts[k] || 0);},0);
        if(!total) return;
        group.keys.forEach(function(k){handled[k]=total<=group.total;});
        if(group.ambiguous) notes.push('Confirm the fridge/freezer allocation with an engineer.');
      });
      var fits=keys.every(function(k){
        if(!loads[k]) return false;
        if(Object.prototype.hasOwnProperty.call(handled,k)) return handled[k];
        if(Object.prototype.hasOwnProperty.call(p.limits,k)) return counts[k]<=p.limits[k];
        if((p.unquantified_loads || []).indexOf(k)!==-1 && counts[k]===1){
          notes.push('The chart names '+k.replace(/_/g,' ')+' without a quantity; confirm its rating and count.');
          return true;
        }
        return false;
      });
      if(!fits) return;
      if(p.inverter_unit==='kW' && connected/1000>p.inverter_rating)
        notes.push('The connected load exceeds inverter output if everything runs together; confirm simultaneous use.');
      if(p.inverter_unit==='kVA') notes.push('Confirm appliance power factor and motor starting loads for this kVA-rated inverter.');
      candidates.push({package:p,notes:notes,review:notes.some(function(n){return n.indexOf('kVA-rated')===-1;})});
    });
    candidates.sort(function(a,b){return a.package.price-b.package.price;});
    var best=candidates[0];
    return {status:best?(best.review?'review':'matched'):'custom',package:best?best.package:null,
      connected_kw:connected/1000,average_kw:average/1000,required_battery_kwh:requiredBattery,
      estimated_backup_hours:best && average>0?best.package.battery_kwh*.9/(average/1000):null,
      notes:best?best.notes:['Your selection needs an engineer assessment; no published package has sufficiently documented appliance ratings and storage for this estimate.']};
  }
  return {recommend:recommend};
});
