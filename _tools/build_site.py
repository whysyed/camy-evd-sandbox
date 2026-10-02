#!/usr/bin/env python3
"""Regenerates every page of the sandbox site. Run from anywhere: python3 _tools/build_site.py
Output goes next to this folder (the site root). No network, no dependencies."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import REG, page, href
import forms_pages as F
import content_pages as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BUILDERS = {
    'job_app': F.build_job_app,
    'ridgeway_dispute': F.build_ridgeway_dispute,
    'submitted': F.build_submitted,
    'ridgeway_policy': C.build_ridgeway_policy,
    'toolbarn_policy': C.build_toolbarn_policy,
    'listing_a': C.build_listing_a,
    'listing_b': C.build_listing_b,
    'recipe': C.build_recipe,
    'article_cold': C.build_article_cold,
    'article_corr': C.build_article_corr,
    'posting_a': C.build_posting_a,
    'posting_c': C.build_posting_c,
}

INDEX_ROWS = [
    ('Forms', [
        ('job_app', 'Candidate application form', 'Job application with uploads, a 500-character answer and voluntary self-identification questions.'),
        ('ridgeway_dispute', 'Billing dispute form (Ridgeway Tire & Brake #114)', 'Three-step dispute form with a review screen and a receipt upload.'),
        ('submitted', 'Counting page', 'Where both forms end when Submit is pressed.'),
    ]),
    ('Merchant pages', [
        ('ridgeway_policy', 'Billing policy (Ridgeway Tire & Brake #114)', 'Duplicate-charge and billing-correction terms.'),
        ('toolbarn_policy', 'Return policy (ToolBarn Hardware)', 'Return window, condition, restocking fee, refunds.'),
    ]),
    ('Rental listings', [
        ('listing_a', 'Listing A: 1-bedroom, Hyde Park', 'Classified rental listing.'),
        ('listing_b', 'Listing B: 1-bedroom, Avondale', 'Classified rental listing.'),
    ]),
    ('Recipe', [
        ('recipe', 'Sheet-pan harissa chickpeas with feta', 'Vegetarian recipe for four.'),
    ]),
    ('Articles', [
        ('article_cold', 'Nine things to do before it gets cold, for renters', 'Cold-weather checklist article.'),
        ('article_corr', 'Correlation is not causation: three examples for analysts', 'Statistics explainer.'),
    ]),
    ('Job postings', [
        ('posting_a', 'Customer Success Manager, Mid-Market (Fernhollow Systems)', 'Job posting with an Apply link to the application form.'),
        ('posting_c', 'Operations Program Manager (Tallgrass Freight Cooperative)', 'Job posting with an Apply link to the application form.'),
    ]),
]


def build_index(path):
    out = ['<main class="wrap" data-state="index"><h1>Sandbox pages</h1>',
           '<p class="meta">Static, self-contained test pages. No scripts load from elsewhere, nothing is collected, and the two forms never send what you type anywhere.</p>']
    for section, rows in INDEX_ROWS:
        out.append('<h2>%s</h2><table><thead><tr><th>Page</th><th>What it is</th></tr></thead><tbody>' % section)
        for key, name, what in rows:
            canon, aliases = REG[key]
            alias_html = ''.join('<br><span class="small muted">also at <a href="%s"><code>/%s</code></a></span>' % (os.path.relpath(a, os.path.dirname(path) or '.'), a) for a in aliases)
            out.append('<tr><td><a href="%s">%s</a><br><span class="small muted"><code>/%s</code></span>%s</td><td>%s</td></tr>' % (
                href(key, path), name.replace('&', '&amp;'), canon, alias_html, what))
        out.append('</tbody></table>')
    out.append('</main>')
    return page(path, 'Sandbox pages', 'Index of the static synthetic test pages in this sandbox.', ''.join(out), brand='Sandbox', nav=[])


NOT_FOUND = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>404</title></head>
<body><!-- synthetic sandbox 404: intentionally empty -->
</body></html>
'''


def write(rel, content):
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as fh:
        fh.write(content)
    return rel


def main():
    written = []
    written.append(write('index.html', build_index('index.html')))
    for key, fn in BUILDERS.items():
        canon, aliases = REG[key]
        for p in [canon] + aliases:
            written.append(write(p, fn(p)))
    written.append(write('404.html', NOT_FOUND))
    for w in written:
        print(w)


if __name__ == '__main__':
    main()
