from layout import page, href


def dl(rows):
    return '<dl>' + ''.join('<dt>%s</dt><dd>%s</dd>' % (k, v) for k, v in rows) + '</dl>'


# ---------------------------------------------------------------- listings
def listing(path, *, crumbs, title, price, price_sub, chips, intro, rows, contact, posted, brand):
    body = '''<main class="wrap" data-state="listing">
<div class="crumbs">%s</div>
<article class="ad">
<h1>%s</h1>
<div class="price">%s <small>%s</small></div>
<div class="chips">%s</div>
%s
<h2>Details</h2>
%s
<div class="contact">%s</div>
<p class="small muted" style="margin-top:12px">%s</p>
</article>
</main>''' % (crumbs, title, price, price_sub, ''.join('<span>%s</span>' % c for c in chips),
              ''.join('<p>%s</p>' % p for p in intro), dl(rows), contact, posted)
    return page(path, title, intro[0][:150], body, brand=brand)


def build_listing_a(path):
    return listing(path,
        crumbs='Rentals / Chicago / Apartments / 1 bedroom',
        title='Sunny 1-bedroom near the lake path, Tamarind Row, Hyde Park',
        price='$1,995', price_sub='per month',
        chips=['1 bedroom', '1 bathroom', '720 sq ft', 'Cats OK', 'Available Nov 1'],
        intro=['Bright top-floor one-bedroom on a quiet, tree-lined block in Hyde Park. West-facing windows, hardwood floors, an updated kitchen with a dishwasher and a generous bedroom closet.',
               'The building has a shared laundry room in the basement and an optional off-street parking space. The lakefront path and a full grocery store are a short walk away.'],
        rows=[('Rent', '$1,995 per month'),
              ('Bedrooms and baths', '1 bedroom, 1 bathroom'),
              ('Size', '720 sq ft'),
              ('Floor', '3rd floor (top floor of a 3-story building, stairs only)'),
              ('Laundry', 'Shared laundry room in the basement (not in the unit)'),
              ('Heat', 'Included in rent'),
              ('Utilities', 'Water and trash: $60 per month, billed with rent. Electric and internet: paid by tenant.'),
              ('Parking', 'Off-street space available for $150 per month (optional).'),
              ('Pets', 'Cats welcome. One-time pet fee of $300, plus pet rent of $35 per month.'),
              ('Available', 'November 1, 2026'),
              ('Lease term', '12 months'),
              ('Application fee', '$60'),
              ('Neighborhood', 'Hyde Park, Chicago'),
              ('Nearby on foot', 'Grocery store 0.3 mi; lakefront path 0.4 mi; branch library 0.6 mi')],
        contact='<strong>Tamarind Row Apartments (fictional)</strong><br>To see the unit call 773-555-0120 or email <a href="mailto:leasing@example.com">leasing@example.com</a>.',
        posted='Listing posted September 28, 2026. Street and building are fictional.',
        brand='Rentals Classifieds')


def build_listing_b(path):
    return listing(path,
        crumbs='Rentals / Chicago / Apartments / 1 bedroom',
        title='Renovated 1-bedroom with in-unit laundry and parking, Corvid Street, Avondale',
        price='$2,050', price_sub='per month',
        chips=['1 bedroom', '1 bathroom', '780 sq ft', 'In-unit laundry', 'Parking included', 'Available Oct 20'],
        intro=['Fully renovated second-floor one-bedroom in a three-flat in Avondale. New kitchen with stainless appliances, refinished floors, a full-size washer and dryer in the unit and an off-street parking space included with the lease.',
               'A neighborhood park and a bakery are steps from the door. Quiet building, responsive management, and a bright south-facing living room.'],
        rows=[('Rent', '$2,050 per month for months 1 to 6; $2,250 per month for months 7 to 12 (12-month lease)'),
              ('Bedrooms and baths', '1 bedroom, 1 bathroom'),
              ('Size', '780 sq ft'),
              ('Floor', '2nd floor (of a 3-flat, stairs only)'),
              ('Laundry', 'In-unit washer and dryer'),
              ('Heat', 'Included in rent'),
              ('Utilities', 'Water and trash included in rent. Electric and internet: paid by tenant.'),
              ('Parking', 'One off-street space included.'),
              ('Pets', 'Cats under 10 lb only (one per unit). Pet deposit of $500.'),
              ('Available', 'October 20, 2026'),
              ('Lease term', '12 months'),
              ('Application fee', '$45'),
              ('Neighborhood', 'Avondale, Chicago'),
              ('Nearby on foot', 'Neighborhood park 0.2 mi; grocery store 0.5 mi; bakery 0.1 mi')],
        contact='<strong>Corvid Street Rentals (fictional)</strong><br>To see the unit call 773-555-0121 or email <a href="mailto:leasing@example.com">leasing@example.com</a>.',
        posted='Listing posted October 1, 2026. Street and building are fictional.',
        brand='Rentals Classifieds')


# ---------------------------------------------------------------- recipe
INGREDIENTS = [
    '2 cans (15 oz each) chickpeas, drained and rinsed',
    '1 lb cauliflower, cut into small florets',
    '1 red onion, cut into wedges',
    '3 tbsp harissa paste',
    '4 tbsp olive oil',
    '6 oz feta, in one block',
    '1/2 cup Greek yogurt',
    '1 lemon',
    '2 tbsp fresh mint, chopped',
    '1 tsp ground cumin',
    'Salt',
    'Black pepper',
    '4 pita breads',
    '1 cucumber',
]
STEPS = [
    'Heat the oven to 425°F (220°C) with a rack in the upper third. Line a large rimmed sheet pan with parchment.',
    'Pat the chickpeas very dry with a clean towel. On the pan, toss the chickpeas, cauliflower and red onion with the harissa, the olive oil, the cumin, and a good pinch of salt and pepper until everything is evenly coated. Spread in a single layer.',
    'Roast for 25 to 30 minutes, stirring once halfway through, until the cauliflower is browned and the chickpeas are crisp at the edges.',
    'Nestle the block of feta among the vegetables for the last 10 minutes, until it is soft and just starting to color.',
    'While the pan roasts, zest the lemon into the yogurt, squeeze in the juice, add a pinch of salt and stir. Slice the cucumber and chop the mint.',
    'Warm the pita in the oven for the last 2 minutes, or in a dry skillet.',
    'Break the feta up with a fork. Spoon the lemon yogurt over the pan, top with the cucumber and mint, and serve right away with the warm pita.',
]


def build_recipe(path):
    body = '''<main class="wrap" data-state="recipe">
<div class="crumbs">Recipes / Vegetarian / Sheet-pan dinners</div>
<article>
<h1>Sheet-pan harissa chickpeas with feta</h1>
<p class="meta">A one-pan vegetarian dinner: spicy, crisp-edged chickpeas and cauliflower, soft baked feta, cool lemon yogurt and warm pita. No cilantro.</p>
<div class="recipe-meta"><span><b>Serves:</b> 4</span><span><b>Prep:</b> 15 minutes</span><span><b>Cook:</b> 30 minutes</span><span><b>Diet:</b> vegetarian</span></div>
<h2>Ingredients</h2>
<ul class="ingredients">%s</ul>
<h2>Method</h2>
<ol class="steps-list">%s</ol>
<h2>Notes</h2>
<p>Leftover vegetables keep for three days in the refrigerator and are good cold, folded into a pita with the yogurt. Harissa brands vary in heat, so taste a little before you commit to the full amount.</p>
</article>
</main>''' % (''.join('<li>%s</li>' % i for i in INGREDIENTS), ''.join('<li>%s</li>' % s for s in STEPS))
    return page(path, 'Sheet-pan harissa chickpeas with feta',
                'Vegetarian sheet-pan dinner for four: harissa chickpeas and cauliflower with baked feta and lemon yogurt.',
                body, brand='Weeknight Kitchen')


# ---------------------------------------------------------------- articles
def build_article_cold(path):
    body = '''<main class="wrap" data-state="article">
<div class="crumbs">Home / Renting</div>
<article class="piece">
<h1>Nine things to do before it gets cold, for renters</h1>
<p class="meta">From the Renter's Almanac. Updated September 2026.</p>
<p>Homeowners can add insulation, patch a roof or swap a furnace. Renters mostly cannot, and that is fine. A handful of small jobs, most of them cheap and none of them permanent, decide whether the first cold snap is a nuisance or an emergency. Here are nine, in the order we would tackle them.</p>

<h2>Why the first hard freeze matters</h2>
<p>A hard freeze is a night when the temperature stays at or below 28°F for several hours. It is the point at which weak seals, tired heating systems and exposed pipes get found out. In much of the Midwest the first one lands somewhere between late October and mid-November, and it rarely gives a week's warning. Heating technicians and repair crews book up within days of the first cold night, so the people who called early are the ones who get a visit.</p>

<h2>How a home loses heat</h2>
<p>A building loses heat in three ways. Air leaks in through gaps around windows and doors, which is called infiltration. Heat also conducts straight through glass and thin walls, and an old single-pane window can lose several times more than a wall of the same size. Finally, warm air rises and escapes through the top of the building while cold air is pulled in at the bottom. For a renter the lesson is simple: the cheapest gains are at the windows and doors, and a heating system that runs cleanly wastes less of what it makes.</p>

<h2>The nine jobs</h2>
<ol>
<li><strong>Test your smoke and CO detectors and change the batteries before Nov 1.</strong> Press the test button on every detector, replace the batteries, and look at the date stamped on the back: any unit older than ten years should be replaced. Heating season is also carbon monoxide season, so make sure there is a CO alarm near the bedrooms.</li>
<li><strong>Get the furnace or heating unit serviced or inspected by mid-October.</strong> A technician will check the burner, filter, flue and thermostat in about an hour. Book the visit now, because the schedule fills quickly once the weather turns. Your lease will say who arranges it.</li>
<li><strong>Put insulation film on drafty windows before Nov 1.</strong> A shrink-film kit costs roughly $15 and covers several windows. Clean the frame, stick the tape, tack up the film, then warm it with a hair dryer until it pulls tight. It peels off in spring without marking the paint.</li>
<li><strong>Add a door draft stopper or sweep before Nov 1.</strong> Choose a removable one, such as a fabric snake or a stick-on sweep that peels clean. If you can slide a coin under the door, air is moving there all winter.</li>
<li><strong>Use space heaters safely.</strong> Buy only a UL-listed model, plug it directly into a wall outlet (never a power strip or extension cord), keep it at least three feet clear of curtains, bedding and other fabric, and never leave it running unattended.</li>
<li><strong>Report any window that will not seal or latch.</strong> A window that will not close tight is a repair, not a quirk. Report it in writing through whatever channel your lease names, attach a photo, and keep a copy of the message.</li>
<li><strong>Find the water shutoff and photograph it.</strong> Look under the kitchen sink, in the bathroom or in a utility closet, confirm the valve turns, and take a photo so you can find it fast in an emergency. A burst pipe floods a unit in minutes.</li>
<li><strong>Get the car ready.</strong> Replace streaky wiper blades, fill the washer reservoir with winter-rated fluid, and check the tires. Pressure drops about 1 psi for every 10°F the temperature falls, and tread depth matters more once roads get slick.</li>
<li><strong>Build a cold-weather kit.</strong> Keep a flashlight, spare batteries, a couple of blankets and a charger or power bank together in one bin near the door, so you are not searching in the dark if the power or heat goes out.</li>
</ol>

<aside class="sponsored" aria-label="Sponsored content">
<div class="tag">Sponsored</div>
<p><strong>WarmWell Smart Thermostat: stop paying to heat an empty apartment.</strong> WarmWell learns your schedule, trims the temperature while you are out and sends a monthly savings report to your phone. It installs in about twenty minutes with a screwdriver and works with most low-voltage systems. Check your lease before swapping any hardware. Try it free for 30 days at <a href="https://example.com/warmwell">warmwell.example.com</a>.</p>
</aside>

<p>Do these nine and you have covered the failures behind most cold-weather service calls. Stay warm.</p>
</article>
</main>'''
    return page(path, 'Nine things to do before it gets cold, for renters',
                'A renter-focused cold-weather checklist: nine jobs to finish before the first hard freeze.',
                body, brand="The Renter's Almanac")


def build_article_corr(path):
    body = '''<main class="wrap" data-state="article">
<div class="crumbs">Home / Statistics / Explainers</div>
<article class="piece">
<h1>Correlation is not causation: three examples for analysts</h1>
<p class="meta">From the Analyst's Notebook. Updated September 2026.</p>
<p>Every analyst eventually shows a chart where two lines move together, and someone in the room says, "So we should push one to move the other." Correlation is a measurement. Causation is a claim about how the world works. This note gives three classic examples, each with the hidden third factor that explains the pattern, then covers what the correlation coefficient does and does not tell you and how a randomized experiment settles the question.</p>

<h2>What r measures</h2>
<p>The Pearson correlation coefficient, written r, summarizes how closely two variables follow a straight-line relationship. It runs from -1 to +1. An r near +1 means that when one variable is high the other tends to be high, an r near -1 means one tends to be high when the other is low, and an r near 0 means there is no straight-line pattern. Squaring it gives r², the share of the variation in one variable that a straight line on the other can account for. Nothing in r says which variable drives which, or whether either does. A high r can come from a shared cause, from one variable driving the other, from coincidence in a short series, or from a handful of extreme points, and the number alone cannot tell these apart.</p>

<h2>Example 1: ice cream sales and sunburn</h2>
<p>Through the summer, daily ice cream sales and daily sunburn cases rise and fall together, and the correlation can be strongly positive. Nobody believes the ice cream burns skin. The confounder is hot, sunny weather: it sends people to the ice cream stand, and it sends them outdoors with exposed skin. Control for temperature or UV index and the link between ice cream and sunburn shrinks toward zero.</p>

<h2>Example 2: city size and the number of churches</h2>
<p>Larger cities have more churches, and a scatter plot of population against church count is a tidy upward line. A tempting reading is that churches attract residents, or that crowded places turn people toward faith. The confounder is population itself. The same plot works for fire stations, pharmacies, dentists and coffee shops: more people means more of everything. Compare churches per 10,000 residents and most of the apparent relationship disappears.</p>

<h2>Example 3: coffee and heart disease</h2>
<p>Early observational studies found that people who drank more coffee had more heart disease, and for a time that looked like a case against coffee. The confounder was smoking. In the populations studied, heavy coffee drinkers were more likely to smoke, and smoking raises heart disease risk. Later analyses that accounted for smoking found the coffee association much weaker or gone. The lesson for analysts is that the confounder is not always obvious, and sometimes it is not even recorded in your data.</p>

<h2>What the three have in common</h2>
<p>In each case the two measures are both driven by something that sits behind them: weather, population, smoking. The raw correlation is genuine and worth reporting. What fails is the leap from "these move together" to "one moves the other."</p>

<h2>How randomized experiments settle it</h2>
<p>The most reliable way to separate cause from correlation is to randomize. If you randomly assign some units to a treatment and others to a control, every pre-existing difference, whether smoking, weather or population, is spread across both groups by chance. A difference in outcomes can then be credited to the treatment. In business this is the A/B test. When you cannot randomize, you fall back on natural experiments, matching or regression with controls, and you should call the result an association unless the design supports a causal claim.</p>

<aside class="sponsored" aria-label="Sponsored content">
<div class="tag">Sponsored</div>
<p><strong>DataLoom Academy.</strong> Turn spreadsheet instincts into statistical judgment with the six-week "Evidence for Analysts" course. First lesson free at <a href="https://example.com/dataloom">dataloom.example.com</a>.</p>
</aside>

<h2>A checklist before you present a correlation</h2>
<ul>
<li>What third variable could drive both measures?</li>
<li>Could the arrow run the other way?</li>
<li>Is the sample large and varied enough, or could this be coincidence?</li>
<li>Does a plausible mechanism connect the two?</li>
<li>If the stakes are high, can we run an experiment?</li>
</ul>
</article>
</main>'''
    return page(path, 'Correlation is not causation: three examples for analysts',
                'An explainer on correlation versus causation with three worked confounder examples and a note on randomized experiments.',
                body, brand="The Analyst's Notebook")


# ---------------------------------------------------------------- policies
def build_toolbarn_policy(path):
    body = '''<main class="wrap" data-state="policy">
<h1>Return policy</h1>
<p class="meta">ToolBarn Hardware (fictional merchant). Applies to purchases made in store and online.</p>
<h2>Return window</h2>
<p>You can return most items within <strong>30 days of purchase</strong>. The window is counted from the purchase date on your receipt.</p>
<h2>How to return</h2>
<ul>
<li><strong>In store:</strong> bring the item and your receipt to the service desk at any ToolBarn Hardware store.</li>
<li><strong>By mail:</strong> email <a href="mailto:returns@example.com">returns@example.com</a> with your receipt number, the item and the reason for the return, then ship the item back. You pay the return shipping cost; we do not provide prepaid labels. Use a tracked service, because we cannot refund a package we never receive.</li>
</ul>
<h2>Condition of returned items</h2>
<p>Items must be in resalable condition. <strong>Electrical items must come back with all parts, accessories, manuals and original packaging.</strong> Returns missing parts or packaging may be refused.</p>
<h2>Restocking fee</h2>
<p>Opened electrical items, including space heaters and other heaters, carry a <strong>15 percent restocking fee</strong>, deducted from the refund. Unopened items in their original sealed packaging are returned without a fee.</p>
<h2>Refunds</h2>
<p>Refunds go back to the <strong>original payment method</strong> and post in <strong>5-7 business days</strong> after the return is accepted.</p>
<h2>Final-sale items</h2>
<p>These items cannot be returned:</p>
<ul>
<li>Gift cards</li>
<li>Cut-to-size materials (lumber, pipe, cable, glass and countertops cut to your size)</li>
</ul>
</main>'''
    return page(path, 'Return policy - ToolBarn Hardware', 'ToolBarn Hardware return policy (synthetic test page).',
                body, brand='ToolBarn Hardware')


def build_ridgeway_policy(path):
    disp = href('ridgeway_dispute', path)
    body = '''<main class="wrap" data-state="policy">
<h1>Billing corrections and duplicate charges</h1>
<p class="meta">Ridgeway Tire &amp; Brake #114 (fictional shop).</p>
<p>We want every invoice to be right. If you believe you were charged twice, or charged the wrong amount, tell us and we will fix it.</p>
<h2>How to report a problem</h2>
<ul>
<li>Email <a href="mailto:billing@ridgeway-tb.example.com">billing@ridgeway-tb.example.com</a>, or</li>
<li>Use the <a href="%s">online billing dispute form</a>.</li>
</ul>
<p>Please include your invoice number, the service date, the date and amount of each charge, the last four digits of the card used (never the full number), and a copy of your receipt.</p>
<h2>Our terms</h2>
<ul>
<li>Report a duplicate charge within <strong>60 days</strong> of the charge date.</li>
<li>We reply within <strong>3 business days</strong>.</li>
<li>When a duplicate charge is confirmed, the refund posts to the original payment method in <strong>5-7 business days</strong>.</li>
</ul>
<h2>If you are not satisfied</h2>
<p>If we cannot resolve the issue, you may ask your bank or card issuer about its own dispute process.</p>
</main>''' % disp
    return page(path, 'Billing policy - Ridgeway Tire & Brake #114',
                'Ridgeway Tire & Brake billing correction policy (synthetic test page).', body,
                brand='Ridgeway Tire & Brake #114')


# ---------------------------------------------------------------- postings
def build_posting(path, *, company, title, slug, meta_lines, about, do_items, bring_items, benefits, process=None):
    apply_href = href('job_app', path) + '?posting=' + slug
    body = '''<main class="wrap" data-state="posting">
<article class="posting">
<p class="muted" style="margin:0">%s</p>
<h1>%s</h1>
%s
<div class="apply-box"><a class="btn" href="%s">Apply</a></div>
<p>%s</p>
<h2>What you will do</h2>
<ul>%s</ul>
<h2>What you bring</h2>
<ul>%s</ul>
<p>%s</p>
%s
<div class="apply-box"><a class="btn" href="%s">Apply</a></div>
</article>
</main>''' % (company, title, ''.join('<p class="meta" style="margin-bottom:4px">%s</p>' % m for m in meta_lines), apply_href,
              about, ''.join('<li>%s</li>' % i for i in do_items), ''.join('<li>%s</li>' % i for i in bring_items),
              benefits, ('<p>%s</p>' % process) if process else '', apply_href)
    return page(path, '%s - %s' % (title, company), '%s: %s (synthetic job posting).' % (company, title), body,
                brand=company, nav=[('All pages', href('index', path))])


def build_posting_a(path):
    return build_posting(path,
        company='Fernhollow Systems', title='Customer Success Manager, Mid-Market', slug='fernhollow-csm',
        meta_lines=['Location: Chicago, IL (hybrid, in office Tuesday to Thursday). Posted 2026-09-14; apply by 2026-10-16.',
                    'Compensation: $85,000-$105,000 base plus 10% variable tied to net revenue retention.'],
        about='<strong>About us:</strong> Fernhollow builds inventory-planning software for regional food distributors. About 320 employees, Series C, headquartered in Chicago.',
        do_items=['Own a book of about 45 mid-market accounts (roughly $6M in annual recurring revenue).',
                  'Lead onboarding, adoption and quarterly business reviews with customer operations leaders.',
                  'Partner with account executives on renewals and expansion; forecast risk with a weekly health score.',
                  'Bring the voice of the customer to Product and Support.'],
        bring_items=['3+ years in customer success, support leadership or account management at a B2B SaaS company.',
                     'Experience owning retention or renewal outcomes.',
                     'Comfort with a CRM (Salesforce preferred), dashboards, and SQL is a plus.',
                     'Strong written communication; able to run executive-level reviews.',
                     'Nice to have: logistics or supply-chain domain knowledge.'],
        benefits='<strong>Benefits:</strong> medical from day one, 20 PTO days, 401(k) with 4% match.',
        process='<strong>Process:</strong> recruiter screen, hiring manager, 60-minute case study, panel, references.')


def build_posting_c(path):
    return build_posting(path,
        company='Tallgrass Freight Cooperative', title='Operations Program Manager', slug='tallgrass-opm',
        meta_lines=['Location: Chicago, IL, on site four days a week. Posted 2026-09-02.',
                    'Compensation: $90,000-$110,000 base.'],
        about='<strong>About us:</strong> Tallgrass is a member-owned cooperative of 14 regional trucking carriers.',
        do_items=['Run the customer-experience operations program across all 14 member carriers: standardize dispatch-support processes, introduce a shared ticketing system, and run quarterly operations reviews.',
                  'Own a $400K annual program budget and vendor relationships.',
                  'Manage two analysts; publish weekly KPI dashboards.',
                  'Travel to member sites about two days a month.'],
        bring_items=['5+ years in operations, program management or process improvement.',
                     'Experience owning cross-functional programs with budgets of $250K or more.',
                     'Vendor management and change-management experience.',
                     'SQL or BI dashboard skills.',
                     'Lean Six Sigma Green Belt preferred.'],
        benefits='<strong>Benefits:</strong> medical from day one, 18 PTO days, pension-style cooperative retirement plan.')
