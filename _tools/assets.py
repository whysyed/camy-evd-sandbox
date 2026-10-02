# Shared CSS and JS strings for the sandbox pages. Everything is inlined into each page.

CSS = r'''
:root{--fg:#1c2230;--muted:#5a6272;--line:#d8dce4;--soft:#f4f5f8;--accent:#1d4f91;--warn:#8a4b00;--bad:#a12626;--ok:#1d6b3a}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:#fff;color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:780px;margin:0 auto;padding:0 20px}
header.site{border-bottom:1px solid var(--line);background:var(--soft)}
header.site .wrap{padding-top:12px;padding-bottom:12px;display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}
header.site .brand{font-weight:700;letter-spacing:.2px}
header.site nav a{margin-right:14px;color:var(--accent);text-decoration:none;font-size:14px}
main.wrap{padding-top:24px;padding-bottom:36px}
h1{font-size:28px;line-height:1.2;margin:0 0 8px}
h2{font-size:20px;margin:28px 0 8px}
h3{font-size:17px;margin:20px 0 6px}
p{margin:0 0 12px}
a{color:var(--accent)}
.muted{color:var(--muted)}
.small{font-size:13px}
.meta{color:var(--muted);font-size:14px;margin-bottom:16px}
table{border-collapse:collapse;width:100%}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:600;background:var(--soft)}
code,pre{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
/* forms */
fieldset{border:1px solid var(--line);border-radius:6px;margin:0 0 18px;padding:12px 16px 6px}
legend{font-weight:600;padding:0 6px}
.field{margin:0 0 12px}
.field>label,.field>.lbl{display:block;font-weight:600;font-size:14px;margin-bottom:4px}
.field .opt{font-weight:400;color:var(--muted)}
input[type=text],input[type=email],input[type=tel],input[type=url],input[type=number],input[type=date],select,textarea{width:100%;padding:8px 10px;border:1px solid #b9bfcb;border-radius:4px;font:inherit;background:#fff;color:inherit}
input[type=file]{font:inherit;max-width:100%}
textarea{min-height:120px;resize:vertical}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:0 16px}
@media (max-width:600px){.grid2{grid-template-columns:1fr}}
.radios label,.checks label{display:flex;gap:8px;align-items:flex-start;font-weight:400;margin:0 0 6px}
.radios label{display:inline-flex;margin-right:18px}
.hint{font-size:13px;color:var(--muted);margin-top:3px}
.counter{font-size:13px;color:var(--muted);text-align:right}
.counter.over{color:var(--bad)}
.err{color:var(--bad);font-size:14px;margin:6px 0}
.btn{display:inline-block;padding:10px 20px;border:1px solid var(--accent);border-radius:4px;background:var(--accent);color:#fff;font:inherit;font-weight:600;cursor:pointer;text-decoration:none}
.btn.secondary{background:#fff;color:var(--accent)}
.actions{display:flex;gap:12px;margin:20px 0}
.steps{display:flex;gap:8px;margin:0 0 16px;padding:0;list-style:none;font-size:14px}
.steps li{padding:4px 10px;border:1px solid var(--line);border-radius:14px;color:var(--muted)}
.steps li.on{background:var(--accent);border-color:var(--accent);color:#fff}
dl.review{display:grid;grid-template-columns:200px 1fr;gap:0;margin:0 0 16px;border-top:1px solid var(--line)}
dl.review dt,dl.review dd{margin:0;padding:6px 8px;border-bottom:1px solid var(--line)}
dl.review dt{font-weight:600;background:var(--soft)}
@media (max-width:600px){dl.review{grid-template-columns:1fr}}
.posting-banner{background:var(--soft);border:1px solid var(--line);border-radius:6px;padding:8px 12px;margin:0 0 16px;font-size:14px}
/* state panel */
.state-panel{margin:32px 0 0;padding:10px 12px;border:1px dashed #b9bfcb;border-radius:6px;background:#fafafb;color:#4a5160;font-size:12px}
.state-panel h2{font-size:12px;margin:0 0 4px;text-transform:uppercase;letter-spacing:.6px;color:#4a5160}
.state-panel .line{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;margin:0 0 4px}
.state-panel pre{margin:6px 0 0;white-space:pre-wrap;word-break:break-all;font-size:11px;line-height:1.4}
/* footer */
footer.site{border-top:1px solid var(--line);background:var(--soft);color:var(--muted);font-size:13px}
footer.site .wrap{padding-top:16px;padding-bottom:20px}
footer.site p{margin:0 0 6px}
/* listings */
.crumbs{font-size:13px;color:var(--muted);margin-bottom:10px}
.ad{border:1px solid var(--line);border-radius:6px;padding:20px}
.ad .price{font-size:30px;font-weight:700;margin:4px 0}
.ad .price small{font-size:15px;font-weight:400;color:var(--muted)}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0 14px}
.chips span{border:1px solid var(--line);background:var(--soft);border-radius:14px;padding:3px 12px;font-size:14px}
.ad dl{display:grid;grid-template-columns:170px 1fr;margin:12px 0}
.ad dt,.ad dd{margin:0;padding:6px 0;border-bottom:1px solid var(--line)}
.ad dt{font-weight:600;color:var(--muted)}
@media (max-width:600px){.ad dl{grid-template-columns:1fr}.ad dt{border-bottom:0;padding-bottom:0}}
.contact{background:var(--soft);border-radius:6px;padding:12px 16px;margin-top:16px;font-size:15px}
/* recipe */
.recipe-meta{display:flex;gap:20px;flex-wrap:wrap;margin:8px 0 16px;font-size:14px;color:var(--muted)}
.recipe-meta b{color:var(--fg)}
ul.ingredients{padding-left:20px}
ul.ingredients li{margin:3px 0}
ol.steps-list li{margin:0 0 10px}
/* articles */
article.piece{font-size:17px;line-height:1.65}
article.piece h2{margin-top:30px}
.sponsored{border:1px solid #e3c98a;background:#fff8e6;border-radius:6px;padding:12px 16px;margin:24px 0}
.sponsored .tag{font-size:12px;text-transform:uppercase;letter-spacing:.8px;color:var(--warn);font-weight:700}
/* postings */
.posting h2{font-size:18px}
.posting ul{padding-left:22px}
.apply-box{margin:20px 0}
/* submitted */
.counted{font-size:clamp(2.2rem,9vw,4.6rem);line-height:1.05;font-weight:800;letter-spacing:.5px;margin:24px 0 12px;padding:18px 20px;border:4px solid var(--ok);color:var(--ok);border-radius:8px;text-align:center}
@media print{header.site nav{display:none}}
'''

# SHA-256 (pure JS fallback when Web Crypto is unavailable) plus the state beacon.
# Each form page defines window.BENCH_CFG = {page, submitHref, extra()} before this runs.
BEACON_JS = r'''
(function(){
'use strict';
var CFG = window.BENCH_CFG || {};
var form = document.getElementById('bench-form');
var panelTs = document.getElementById('state-ts');
var panelLine = document.getElementById('state-line');
var panelJson = document.getElementById('state-json');
var seq = 0, fileInfo = {}, fileTokens = {}, pending = {}, timer = null;

function hex(buf){
  var b = new Uint8Array(buf), s = '';
  for (var i = 0; i < b.length; i++) s += (b[i] < 16 ? '0' : '') + b[i].toString(16);
  return s;
}
function sha256Fallback(data){
  var K = new Uint32Array([0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2]);
  var H = new Uint32Array([0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]);
  var l = data.length;
  var padLen = ((l + 9 + 63) >> 6) << 6;
  var buf = new Uint8Array(padLen);
  buf.set(data); buf[l] = 0x80;
  var dv = new DataView(buf.buffer);
  dv.setUint32(padLen - 8, Math.floor(l / 0x20000000));
  dv.setUint32(padLen - 4, (l << 3) >>> 0);
  var w = new Uint32Array(64), i, off;
  for (off = 0; off < padLen; off += 64) {
    for (i = 0; i < 16; i++) w[i] = dv.getUint32(off + i * 4);
    for (i = 16; i < 64; i++) {
      var x = w[i-15], y = w[i-2];
      var s0 = ((x>>>7)|(x<<25)) ^ ((x>>>18)|(x<<14)) ^ (x>>>3);
      var s1 = ((y>>>17)|(y<<15)) ^ ((y>>>19)|(y<<13)) ^ (y>>>10);
      w[i] = (w[i-16] + s0 + w[i-7] + s1) >>> 0;
    }
    var a=H[0],b=H[1],c=H[2],d=H[3],e=H[4],f=H[5],g=H[6],h=H[7];
    for (i = 0; i < 64; i++) {
      var S1 = ((e>>>6)|(e<<26)) ^ ((e>>>11)|(e<<21)) ^ ((e>>>25)|(e<<7));
      var ch = (e & f) ^ (~e & g);
      var t1 = (h + S1 + ch + K[i] + w[i]) >>> 0;
      var S0 = ((a>>>2)|(a<<30)) ^ ((a>>>13)|(a<<19)) ^ ((a>>>22)|(a<<10));
      var maj = (a & b) ^ (a & c) ^ (b & c);
      var t2 = (S0 + maj) >>> 0;
      h=g; g=f; f=e; e=(d + t1) >>> 0; d=c; c=b; b=a; a=(t1 + t2) >>> 0;
    }
    H[0]=(H[0]+a)>>>0; H[1]=(H[1]+b)>>>0; H[2]=(H[2]+c)>>>0; H[3]=(H[3]+d)>>>0;
    H[4]=(H[4]+e)>>>0; H[5]=(H[5]+f)>>>0; H[6]=(H[6]+g)>>>0; H[7]=(H[7]+h)>>>0;
  }
  var out = new Uint8Array(32), ov = new DataView(out.buffer);
  for (i = 0; i < 8; i++) ov.setUint32(i * 4, H[i]);
  return out;
}
function sha256(file){
  return file.arrayBuffer().then(function(buf){
    if (window.crypto && window.crypto.subtle && window.crypto.subtle.digest) {
      return window.crypto.subtle.digest('SHA-256', buf).then(hex).catch(function(){
        return hex(sha256Fallback(new Uint8Array(buf)));
      });
    }
    return hex(sha256Fallback(new Uint8Array(buf)));
  });
}
function utf8b64(str){
  var bytes = new TextEncoder().encode(str), bin = '';
  for (var i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
  return btoa(bin);
}
function collect(){
  var fields = {}, files = {}, filled = 0, total = 0, seen = {};
  var els = form.elements;
  for (var i = 0; i < els.length; i++) {
    var el = els[i], n = el.name;
    if (!n || el.type === 'button' || el.type === 'submit' || el.type === 'reset') continue;
    if (el.type === 'file') {
      total++;
      var fi = fileInfo[n] || null;
      files[n] = fi ? {name: fi.name, size: fi.size, sha256: fi.sha256} : null;
      if (fi) filled++;
    } else if (el.type === 'radio') {
      if (seen[n]) continue;
      seen[n] = 1; total++;
      var sel = form.querySelector('input[type=radio][name="' + n + '"]:checked');
      fields[n] = sel ? sel.value : '';
      if (sel) filled++;
    } else if (el.type === 'checkbox') {
      total++; fields[n] = !!el.checked;
      if (el.checked) filled++;
    } else {
      total++; fields[n] = el.value;
      if (el.value !== '') filled++;
    }
  }
  return {fields: fields, files: files, filled: filled, total: total};
}
function buildState(){
  var c = collect();
  var s = {v: 1, page: CFG.page, ts: new Date().toISOString(), seq: ++seq};
  var ex = CFG.extra ? CFG.extra() : {};
  for (var k in ex) if (Object.prototype.hasOwnProperty.call(ex, k)) s[k] = ex[k];
  s.filled = c.filled; s.total = c.total; s.fields = c.fields; s.files = c.files;
  return s;
}
function fmtSize(n){ return n.toLocaleString('en-US') + ' B'; }
function publishNow(){
  if (timer) { clearTimeout(timer); timer = null; }
  var s = buildState(), json = JSON.stringify(s), b64 = utf8b64(json);
  try { history.replaceState(null, '', location.pathname + location.search + '#' + b64); } catch (e) {}
  var parts = ['seq ' + s.seq, 'filled ' + s.filled + '/' + s.total];
  for (var fn in s.files) {
    if (s.files[fn]) parts.push(fn + ': ' + s.files[fn].name + ', ' + fmtSize(s.files[fn].size) + ', sha256 ' + s.files[fn].sha256);
  }
  if (panelTs) panelTs.textContent = 'Updated ' + s.ts;
  if (panelLine) panelLine.textContent = parts.join(' | ');
  if (panelJson) panelJson.textContent = json;
  window.__benchState.last = {state: s, json: json, b64: b64};
  if (typeof CFG.onPublish === 'function') CFG.onPublish(s);
  return b64;
}
function schedule(){
  if (timer) clearTimeout(timer);
  timer = setTimeout(publishNow, 150);
}
function onFile(input){
  var n = input.name, f = input.files && input.files[0];
  fileTokens[n] = (fileTokens[n] || 0) + 1;
  var token = fileTokens[n];
  if (!f) { delete fileInfo[n]; delete pending[n]; return; }
  var info = {name: f.name, size: f.size, sha256: 'pending'};
  fileInfo[n] = info;
  pending[n] = sha256(f).then(function(h){ if (fileTokens[n] === token) info.sha256 = h; })
    .catch(function(){ if (fileTokens[n] === token) info.sha256 = 'error'; })
    .then(function(){ if (fileTokens[n] === token) publishNow(); });
  if (typeof CFG.onFile === 'function') CFG.onFile(n, f);
}
window.__benchState = {last: null, publishNow: publishNow, sha256Fallback: sha256Fallback, sha256: sha256, pending: pending, fileInfo: fileInfo};

form.addEventListener('input', schedule);
form.addEventListener('change', function(e){
  if (e.target && e.target.type === 'file') onFile(e.target);
  publishNow();
});
form.addEventListener('keydown', function(e){
  if (e.key === 'Enter' && e.target && e.target.tagName !== 'TEXTAREA' && e.target.tagName !== 'BUTTON') e.preventDefault();
});
form.addEventListener('submit', function(e){
  e.preventDefault();
  var waits = [];
  for (var k in pending) waits.push(pending[k]);
  Promise.all(waits).then(function(){
    var b64 = publishNow();
    window.location.href = CFG.submitHref + '?from=' + encodeURIComponent(CFG.page) + '#' + b64;
  });
});
// textarea counters
var counters = form.querySelectorAll('[data-counter-for]');
Array.prototype.forEach.call(counters, function(c){
  var ta = document.getElementById(c.getAttribute('data-counter-for'));
  var max = parseInt(c.getAttribute('data-max'), 10);
  function upd(){ c.textContent = ta.value.length + ' / ' + max; c.className = 'counter' + (ta.value.length >= max ? ' over' : ''); }
  ta.addEventListener('input', upd); upd();
});
publishNow();
})();
'''

SUBMITTED_JS = r'''
(function(){
'use strict';
var REQUIRED = {
  'job-application': {fields: ['first_name','last_name','email'], files: ['resume'], checks: ['terms','privacy','certify']},
  'ridgeway-dispute': {fields: ['customer_name','email','invoice_number'], files: [], checks: ['declaration']}
};
var q = new URLSearchParams(location.search);
var from = q.get('from') || '';
var h = location.hash.replace(/^#/, '');
var state = null;
function decode(s){
  try { s = decodeURIComponent(s); } catch (e) {}
  var bin = atob(s), bytes = new Uint8Array(bin.length);
  for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return JSON.parse(new TextDecoder().decode(bytes));
}
try { if (h) state = decode(h); } catch (e) { state = null; }
function el(id){ return document.getElementById(id); }
function esc(v){ return String(v).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
var now = new Date().toISOString();
el('counted-at').textContent = 'Counted at ' + now;
el('counted-from').textContent = 'Form: ' + (from || 'unknown');
document.body.setAttribute('data-from', from || 'unknown');
var rows = '';
if (!state) {
  el('detail').innerHTML = '<p class="muted">No form state was found in the URL, so only the visit itself is recorded.</p>';
} else {
  var req = REQUIRED[from] || {fields: [], files: [], checks: []};
  var f = state.fields || {}, files = state.files || {};
  var missing = req.fields.filter(function(k){ return !f[k]; });
  var missingFiles = (req.files || []).filter(function(k){ return !files[k]; });
  var unchecked = req.checks.filter(function(k){ return !f[k]; });
  var out = '<h2>State at the moment of submit</h2>';
  out += '<p class="small muted">Last form update ' + esc(state.ts || '?') + ' | sequence ' + esc(state.seq) + ' | ' + esc(state.filled) + ' of ' + esc(state.total) + ' fields filled' + (state.posting ? ' | posting ' + esc(state.posting) : '') + (state.step ? ' | step ' + esc(state.step) : '') + '</p>';
  out += '<p><b>Required fields empty at submit:</b> ' + (missing.concat(missingFiles).length ? esc(missing.concat(missingFiles).join(', ')) : 'none') + '<br><b>Checkboxes not ticked:</b> ' + (unchecked.length ? esc(unchecked.join(', ')) : 'none') + '</p>';
  out += '<table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody>';
  Object.keys(f).forEach(function(k){
    var v = f[k];
    var shown = (v === '' || v === false) ? (v === false ? 'not ticked' : '(blank)') : (v === true ? 'ticked' : v);
    out += '<tr><td><code>' + esc(k) + '</code></td><td>' + esc(shown) + '</td></tr>';
  });
  Object.keys(files).forEach(function(k){
    var x = files[k];
    out += '<tr><td><code>' + esc(k) + '</code></td><td>' + (x ? esc(x.name) + ' (' + esc(x.size) + ' bytes), sha256 <code>' + esc(x.sha256) + '</code>' : '(no file)') + '</td></tr>';
  });
  out += '</tbody></table>';
  el('detail').innerHTML = out;
  el('raw').textContent = JSON.stringify(state);
}
// short submission id: first 12 hex of SHA-256 over "<hash>|<time>"
function shortId(){
  var data = new TextEncoder().encode(h + '|' + now);
  if (window.crypto && window.crypto.subtle) {
    return window.crypto.subtle.digest('SHA-256', data).then(function(b){
      var a = new Uint8Array(b), s = '';
      for (var i = 0; i < 6; i++) s += (a[i] < 16 ? '0' : '') + a[i].toString(16);
      return s;
    });
  }
  return Promise.resolve('nohash');
}
shortId().then(function(id){ el('counted-id').textContent = 'Count ID SUB-' + id.toUpperCase(); }).catch(function(){});
})();
'''
