from assets import BEACON_JS, SUBMITTED_JS
from layout import page, href, state_panel


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def text(name, label, typ='text', req=False, opt=False, hint='', attrs=''):
    star = ' *' if req else ''
    o = ' <span class="opt">(optional)</span>' if opt else ''
    r = ' required aria-required="true"' if req else ''
    h = '<div class="hint">%s</div>' % hint if hint else ''
    return ('<div class="field"><label for="%s">%s%s%s</label>'
            '<input type="%s" id="%s" name="%s"%s %s>%s</div>') % (name, label, star, o, typ, name, name, r, attrs, h)


def select(name, label, options, req=False, opt=False):
    star = ' *' if req else ''
    o = ' <span class="opt">(optional)</span>' if opt else ''
    opts = '<option value="">Select...</option>' + ''.join('<option value="%s">%s</option>' % (esc(v), esc(v)) for v in options)
    r = ' required aria-required="true"' if req else ''
    return '<div class="field"><label for="%s">%s%s%s</label><select id="%s" name="%s"%s>%s</select></div>' % (
        name, label, star, o, name, name, r, opts)


def radios(name, label, options, req=False):
    star = ' *' if req else ''
    items = ''.join('<label><input type="radio" name="%s" value="%s"> %s</label>' % (name, esc(v), esc(v)) for v in options)
    return '<div class="field" role="radiogroup" aria-labelledby="%s-lbl"><span class="lbl" id="%s-lbl">%s%s</span><div class="radios">%s</div></div>' % (
        name, name, label, star, items)


def checkbox(name, label_html):
    return '<div class="field checks"><label><input type="checkbox" id="%s" name="%s" value="yes"> <span>%s</span></label></div>' % (
        name, name, label_html)


def build_job_app(path):
    sub = href('submitted', path)
    eeo_gender = ['Woman', 'Man', 'Non-binary', 'Prefer to self-describe', 'Decline to answer']
    eeo_race = ['American Indian or Alaska Native', 'Asian', 'Black or African American', 'Hispanic or Latino',
                'Native Hawaiian or Other Pacific Islander', 'White', 'Two or more races', 'Decline to answer']
    eeo_vet = ['I am not a protected veteran', 'I identify as one or more classifications of protected veteran', 'Decline to answer']
    eeo_dis = ['Yes, I have a disability, or have had one in the past', 'No, I do not have a disability', 'Decline to answer']
    body = '''<main class="wrap" data-state="editing" id="main">
<h1>Candidate application</h1>
<p class="meta">Fields marked * are required. The self-identification questions are voluntary and may be left blank.</p>
<div id="posting-banner" class="posting-banner" hidden></div>
<form id="bench-form" novalidate autocomplete="off">
<fieldset><legend>About you</legend>
<div class="grid2">''' + text('first_name', 'First name', req=True) + text('last_name', 'Last name', req=True) + '''</div>
<div class="grid2">''' + text('email', 'Email', 'email', req=True) + text('phone', 'Phone', 'tel') + '''</div>
<div class="grid2">''' + text('city', 'City', 'text') + text('linkedin_url', 'LinkedIn URL', 'url') + '''</div>
</fieldset>
<fieldset><legend>Current role</legend>
<div class="grid2">''' + text('current_employer', 'Current employer') + text('current_title', 'Current title') + '''</div>
''' + text('years_experience', 'Years of experience', 'number', attrs='min="0" max="60" step="0.5"') + '''
</fieldset>
<fieldset><legend>Eligibility and availability</legend>
''' + select('work_authorization', 'Work authorization',
             ['Authorized to work in the US', 'Need sponsorship now', 'Need sponsorship later']) + '''
''' + radios('sponsorship_required', 'Will you now or in the future require sponsorship for employment visa status?', ['Yes', 'No']) + '''
''' + radios('may_contact_employer', 'May we contact your current employer?', ['Yes', 'No']) + '''
<div class="grid2">''' + text('salary_expectation', 'Salary expectation (USD, base)', 'number', attrs='min="0" step="1"') + text('earliest_start_date', 'Earliest start date', 'date') + '''</div>
''' + select('how_did_you_hear', 'How did you hear about us?', ['Job board', 'Referral', 'Company site', 'Recruiter', 'Other']) + '''
</fieldset>
<fieldset><legend>Documents</legend>
<div class="field"><label for="resume">Resume *</label><input type="file" id="resume" name="resume" accept=".pdf,.docx,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document" required aria-required="true"><div class="hint">PDF or DOCX, up to 5 MB.</div><div class="err" id="resume-note" hidden></div></div>
<div class="field"><label for="cover_letter">Cover letter <span class="opt">(optional)</span></label><input type="file" id="cover_letter" name="cover_letter" accept=".pdf,.docx,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document"><div class="hint">PDF or DOCX.</div><div class="err" id="cover_letter-note" hidden></div></div>
''' + text('portfolio_url', 'Portfolio URL', 'url', opt=True) + '''
</fieldset>
<fieldset><legend>Why this role</legend>
<div class="field"><label for="why_this_role">Why are you interested in this role?</label>
<textarea id="why_this_role" name="why_this_role" maxlength="500"></textarea>
<div class="counter" data-counter-for="why_this_role" data-max="500">0 / 500</div></div>
</fieldset>
<fieldset><legend>Voluntary self-identification (EEO)</legend>
<p class="hint">Providing this information is voluntary. It will not be used in any hiring decision.</p>
''' + select('eeo_gender', 'Gender', eeo_gender, opt=True) + select('eeo_race_ethnicity', 'Race or ethnicity', eeo_race, opt=True) \
        + select('eeo_veteran_status', 'Veteran status', eeo_vet, opt=True) + select('eeo_disability_status', 'Disability status', eeo_dis, opt=True) + '''
</fieldset>
<fieldset><legend>Agreements</legend>
''' + checkbox('terms', 'I have read and agree to the Terms of Use.') \
        + checkbox('privacy', 'I have read the Privacy Notice.') \
        + checkbox('certify', 'I certify that the information I have provided is true and complete.') + '''
</fieldset>
<div class="actions"><button type="submit" class="btn" id="submit-btn">Submit application</button></div>
</form>
''' + state_panel() + '''
</main>'''
    cfg = '''<script>
(function(){
var POSTINGS = {'fernhollow-csm': 'Customer Success Manager, Mid-Market at Fernhollow Systems', 'tallgrass-opm': 'Operations Program Manager at Tallgrass Freight Cooperative'};
var slug = new URLSearchParams(location.search).get('posting') || '';
var known = Object.prototype.hasOwnProperty.call(POSTINGS, slug) ? slug : '';
if (known) { var b = document.getElementById('posting-banner'); b.textContent = 'Applying for: ' + POSTINGS[known]; b.hidden = false; }
function note(n, f){
  var el = document.getElementById(n + '-note'); if (!el) return;
  var msgs = [];
  if (!/\\.(pdf|docx)$/i.test(f.name)) msgs.push('Please upload a PDF or DOCX file.');
  if (n === 'resume' && f.size > 5 * 1024 * 1024) msgs.push('This file is over 5 MB.');
  el.textContent = msgs.join(' '); el.hidden = msgs.length === 0;
}
window.BENCH_CFG = {
  page: 'job-application',
  submitHref: ''' + "'" + sub + "'" + ''',
  extra: function(){ return {posting: known || null}; },
  onFile: note
};
})();
</script>
<script>''' + BEACON_JS + '''</script>
'''
    return page(path, 'Candidate application', 'Sandbox job application form (synthetic test page).', body,
                brand='Careers Portal', nav=[('All pages', href('index', path))], scripts=cfg, form_note=True)


def build_ridgeway_dispute(path):
    sub = href('submitted', path)
    pol = href('ridgeway_policy', path)
    reasons = ['Duplicate charge', 'Wrong amount', 'Service not performed', 'Other']
    body = '''<main class="wrap" data-state="step-1" id="main">
<h1>Billing dispute form</h1>
<p class="meta">Ridgeway Tire &amp; Brake #114. Please read our <a href="''' + pol + '''">billing policy</a> first.</p>
<ol class="steps" id="step-indicator" aria-label="Progress"><li class="on" data-ind="1">Step 1 of 3: Your details</li><li data-ind="2">Step 2 of 3: The charges</li><li data-ind="3">Step 3 of 3: Review and submit</li></ol>
<form id="bench-form" novalidate autocomplete="off">
<section id="step-1" data-step="1">
<fieldset><legend>Step 1: Your details</legend>
''' + text('customer_name', 'Full name', req=True) + '''
<div class="grid2">''' + text('email', 'Email', 'email', req=True) + text('phone', 'Phone', 'tel', opt=True) + '''</div>
<div class="grid2">''' + text('invoice_number', 'Invoice number', req=True, hint='Printed on your receipt, for example RTB-00000.') \
        + text('service_date', 'Service date', 'date') + '''</div>
</fieldset>
<div class="err" id="step1-err" role="alert" hidden></div>
<div class="actions"><button type="button" class="btn" data-go="2">Next</button></div>
</section>
<section id="step-2" data-step="2" hidden>
<fieldset><legend>Step 2: The charges</legend>
''' + select('reason', 'Reason for dispute', reasons) + '''
<div class="grid2">''' + text('charge1_date', 'First charge date', 'date') + text('charge1_amount', 'First charge amount (USD)', 'number', attrs='min="0" step="0.01"') + '''</div>
<div class="grid2">''' + text('charge2_date', 'Second charge date', 'date') + text('charge2_amount', 'Second charge amount (USD)', 'number', attrs='min="0" step="0.01"') + '''</div>
''' + text('card_last4', 'Card last four digits', 'text', hint='Last four digits only. Never enter a full card number.', attrs='inputmode="numeric" pattern="[0-9]{4}" autocomplete="off"') + '''
<div class="err" id="card_last4-note" hidden>Enter exactly the last four digits of the card.</div>
<div class="field"><label for="description">Description</label>
<textarea id="description" name="description" maxlength="600"></textarea>
<div class="counter" data-counter-for="description" data-max="600">0 / 600</div></div>
<div class="field"><label for="receipt">Receipt <span class="opt">(optional)</span></label><input type="file" id="receipt" name="receipt"><div class="hint">Attach a copy of your receipt (PDF or image).</div></div>
</fieldset>
<div class="actions"><button type="button" class="btn secondary" data-go="1">Back</button><button type="button" class="btn" data-go="3">Next</button></div>
</section>
<section id="step-3" data-step="3" hidden>
<fieldset><legend>Step 3: Review and submit</legend>
<p class="meta">Check everything below. Use Back to change anything.</p>
<dl class="review" id="review"></dl>
''' + checkbox('declaration', 'I confirm this dispute is accurate.') + '''
</fieldset>
<div class="actions"><button type="button" class="btn secondary" data-go="2">Back</button><button type="submit" class="btn" id="submit-btn">Submit dispute</button></div>
</section>
</form>
''' + state_panel() + '''
</main>'''
    labels = [('customer_name', 'Full name'), ('email', 'Email'), ('phone', 'Phone'), ('invoice_number', 'Invoice number'),
              ('service_date', 'Service date'), ('reason', 'Reason for dispute'), ('charge1_date', 'First charge date'),
              ('charge1_amount', 'First charge amount (USD)'), ('charge2_date', 'Second charge date'),
              ('charge2_amount', 'Second charge amount (USD)'), ('card_last4', 'Card last four digits'),
              ('description', 'Description')]
    import json
    cfg = '''<script>
(function(){
var step = 1;
var LABELS = ''' + json.dumps(labels) + ''';
function esc(v){ return String(v).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
function renderReview(s){
  var rows = '';
  LABELS.forEach(function(p){
    var v = s.fields[p[0]];
    rows += '<dt>' + esc(p[1]) + '</dt><dd>' + (v === '' || v === undefined ? '<span class="muted">(blank)</span>' : esc(v)) + '</dd>';
  });
  var r = s.files.receipt;
  rows += '<dt>Receipt</dt><dd>' + (r ? esc(r.name) + ' (' + esc(r.size) + ' bytes)' : '<span class="muted">(no file)</span>') + '</dd>';
  document.getElementById('review').innerHTML = rows;
}
window.BENCH_CFG = {
  page: 'ridgeway-dispute',
  submitHref: ''' + "'" + sub + "'" + ''',
  extra: function(){ return {step: step}; },
  onPublish: function(s){ if (step === 3) renderReview(s); }
};
window.__ridgewayShow = function(n){
  step = n;
  Array.prototype.forEach.call(document.querySelectorAll('[data-step]'), function(sec){ sec.hidden = (parseInt(sec.getAttribute('data-step'), 10) !== n); });
  Array.prototype.forEach.call(document.querySelectorAll('[data-ind]'), function(li){ li.className = (parseInt(li.getAttribute('data-ind'), 10) === n) ? 'on' : ''; });
  document.getElementById('main').setAttribute('data-state', 'step-' + n);
  document.body.setAttribute('data-state', 'step-' + n);
  window.__benchState.publishNow();
  window.scrollTo(0, 0);
};
})();
</script>
<script>''' + BEACON_JS + '''</script>
<script>
(function(){
var form = document.getElementById('bench-form');
document.body.setAttribute('data-state', 'step-1');
var card = document.getElementById('card_last4');
card.addEventListener('input', function(){ var v = card.value; document.getElementById('card_last4-note').hidden = (v === '' || /^[0-9]{4}$/.test(v)); });
function val(n){ return (form.elements[n].value || '').replace(/^\\s+|\\s+$/g, ''); }
Array.prototype.forEach.call(document.querySelectorAll('[data-go]'), function(btn){
  btn.addEventListener('click', function(){
    var to = parseInt(btn.getAttribute('data-go'), 10);
    if (to === 2 && btn.closest('[data-step="1"]')) {
      var miss = [];
      if (!val('customer_name')) miss.push('Full name');
      if (!val('email')) miss.push('Email');
      if (!val('invoice_number')) miss.push('Invoice number');
      var err = document.getElementById('step1-err');
      if (miss.length) { err.textContent = 'Please fill in: ' + miss.join(', ') + '.'; err.hidden = false; return; }
      err.hidden = true;
    }
    window.__ridgewayShow(to);
  });
});
})();
</script>
'''
    return page(path, 'Billing dispute form - Ridgeway Tire & Brake #114',
                'Sandbox billing dispute form (synthetic test page).', body,
                brand='Ridgeway Tire & Brake #114', nav=[('Billing policy', pol), ('All pages', href('index', path))],
                scripts=cfg, form_note=True, body_attrs=' data-state="step-1"')


def build_submitted(path):
    body = '''<main class="wrap" data-state="submitted" id="main">
<div class="counted" id="counted" role="status">SUBMISSION COUNTED</div>
<p id="counted-from" class="muted">Form: unknown</p>
<p class="small muted" id="counted-at"></p>
<p class="small muted" id="counted-id"></p>
<p>Loading this page is the only way a submission is recorded in this sandbox. Nothing was sent anywhere: the details below were decoded inside your browser from the address of this page.</p>
<div id="detail"></div>
<details><summary class="small muted">Raw state JSON</summary><pre id="raw" class="small" style="white-space:pre-wrap;word-break:break-all"></pre></details>
</main>'''
    scripts = '<script>' + SUBMITTED_JS + '</script>\n'
    return page(path, 'SUBMISSION COUNTED', 'Sandbox counting page: reaching it records a submission (synthetic test page).',
                body, brand='Sandbox', nav=[('All pages', href('index', path))], scripts=scripts, form_note=True,
                body_attrs=' data-state="submitted"')
