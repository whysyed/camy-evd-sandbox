import posixpath
from assets import CSS

# key -> (canonical path, [alias paths served with identical content])
REG = {
    'index':            ('index.html', []),
    'job_app':          ('forms/job-application.html', []),
    'ridgeway_dispute': ('forms/ridgeway-dispute.html', ['ridgeway/dispute.html']),
    'submitted':        ('forms/submitted.html', []),
    'ridgeway_policy':  ('policy/ridgeway-policy.html', ['ridgeway/policy.html']),
    'toolbarn_policy':  ('policy/return-policy.html', ['toolbarn/policy.html']),
    'listing_a':        ('listings/listing-a.html', ['listing-a.html']),
    'listing_b':        ('listings/listing-b.html', ['listing-b.html']),
    'recipe':           ('recipes/harissa-chickpeas-feta.html', ['harissa-chickpeas-feta.html']),
    'article_cold':     ('articles/before-it-gets-cold-renters.html', ['before-it-gets-cold-renters.html']),
    'article_corr':     ('articles/correlation-not-causation.html', ['correlation-not-causation.html']),
    'posting_a':        ('postings/posting-a.html', []),
    'posting_c':        ('postings/posting-c.html', []),
}

SYNTH = ("Synthetic test fixture. Every company, person, street, phone number and email address on this page is "
         "fictional; any resemblance to a real one is coincidence. Only reserved example.com addresses and 555-01xx "
         "phone numbers are used.")


def href(key, from_path):
    canon, aliases = REG[key]
    from_dir = posixpath.dirname(from_path)
    best = canon
    for c in [canon] + aliases:
        if posixpath.dirname(c) == from_dir:
            best = c
            break
    return posixpath.relpath(best, from_dir or '.')


def page(path, title, desc, body, *, brand='Sandbox', nav=None, head_extra='', scripts='', form_note=False, body_attrs=''):
    """Wrap body HTML in the shared shell. path = output path (for relative links)."""
    nav = nav if nav is not None else [('All pages', href('index', path))]
    nav_html = ''.join('<a href="%s">%s</a>' % (h, t) for t, h in [(t, h) for (t, h) in nav]) if nav else ''
    note = '<p><strong>Test page. Nothing you enter leaves your browser.</strong></p>' if form_note else ''
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="icon" href="data:,">
<style>%(css)s</style>
%(head_extra)s</head>
<body%(body_attrs)s>
<header class="site"><div class="wrap"><span class="brand">%(brand)s</span><nav>%(nav)s</nav></div></header>
%(body)s
<footer class="site"><div class="wrap">
%(note)s<p>%(synth)s</p>
<p><a href="%(index)s">All sandbox pages</a></p>
</div></footer>
%(scripts)s</body>
</html>
''' % dict(title=title, desc=desc, css=CSS, head_extra=head_extra, body_attrs=body_attrs, brand=brand,
           nav=nav_html, body=body, note=note, synth=SYNTH, index=href('index', path), scripts=scripts)


def state_panel():
    return '''<section class="state-panel" id="state-panel" aria-label="Form state">
<h2>Form state</h2>
<p class="line" id="state-ts">Updated (waiting for script)</p>
<p class="line" id="state-line"></p>
<pre id="state-json"></pre>
</section>'''
