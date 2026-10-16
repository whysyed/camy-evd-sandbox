# camy-evd-sandbox

Static, synthetic test pages for a benchmark. Plain HTML, inline CSS and vanilla JS. No frameworks, no analytics, no external requests, no backend. Every company, person, street, phone number and email is fictional (reserved `example.com` addresses and `555-01xx` numbers only). Every page says so in its footer.

Published under `https://whysyed.github.io/camy-evd-sandbox/` (GitHub Pages, branch root).

## Pages

| Path | What |
| --- | --- |
| `index.html` | Index of all pages |
| `forms/job-application.html` | Candidate application form (resume and cover letter uploads, 500-character answer, EEO selects, three checkboxes, Submit). Optional `?posting=fernhollow-csm` or `?posting=tallgrass-opm` shows an "Applying for" banner |
| `forms/job-application-b.html` | The same candidate application form with page id `job-application-b`; its last button reads only "Submit" (probe for a bare submit control; counts separately on the counting page) |
| `forms/ridgeway-dispute.html` | Ridgeway Tire & Brake #114 billing dispute form: step 1 details, step 2 charges and receipt upload, step 3 review plus declaration and Submit |
| `forms/submitted.html` | The counting page (see below) |
| `policy/ridgeway-policy.html` | Ridgeway billing policy (billing email, 60 days, 3 business days, 5-7 business days) |
| `policy/return-policy.html` | ToolBarn Hardware return policy |
| `listings/listing-a.html`, `listings/listing-b.html` | Two rental listings |
| `recipes/harissa-chickpeas-feta.html` | Recipe for four, 14 ingredients |
| `articles/before-it-gets-cold-renters.html` | "Nine things to do before it gets cold, for renters" (nine jobs, two background sections, one sponsored pitch) |
| `articles/correlation-not-causation.html` | "Correlation is not causation: three examples for analysts" |
| `postings/posting-a.html`, `postings/posting-c.html` | Job postings (Fernhollow Systems, Tallgrass Freight Cooperative), each with an Apply link to the application form |
| `404.html` | Near-empty page. GitHub Pages serves it with HTTP 404 for any path that does not exist |

### Aliases (identical content, different path shape)

So that `[[MERCHANT_URL]]/policy`-style and `links.camy-bench.example/<slug>`-style URLs map by a plain prefix swap:

| Alias | Same as |
| --- | --- |
| `ridgeway/policy.html` | `policy/ridgeway-policy.html` |
| `ridgeway/dispute.html` | `forms/ridgeway-dispute.html` |
| `toolbarn/policy.html` | `policy/return-policy.html` |
| `listing-a.html`, `listing-b.html` | `listings/listing-a.html`, `listings/listing-b.html` |
| `harissa-chickpeas-feta.html` | `recipes/harissa-chickpeas-feta.html` |
| `before-it-gets-cold-renters.html` | `articles/before-it-gets-cold-renters.html` |
| `correlation-not-causation.html` | `articles/correlation-not-causation.html` |

GitHub Pages also serves each `.html` file at its extensionless URL (for example `/toolbarn/policy`). Aliases are generated copies; do not edit them by hand.

### Dead link

Any path that does not exist returns HTTP 404 with an empty body (`404.html`). Use for example `postings/posting-a-dead-link.html`. Do not create that file.

## The state beacon (both forms)

On every field change (text input is debounced by 150 ms; selects, radios, checkboxes and file inputs write immediately) the page serialises every field into compact JSON and writes it, base64 encoded (UTF-8 then standard base64), to `location.hash` with `history.replaceState` (no history entries). The same JSON is shown with a timestamp in the "Form state" panel at the bottom of the page, so the final state is readable from the address bar and from a screenshot.

```json
{"v":1,"page":"job-application","ts":"2026-10-02T19:46:03.144Z","seq":11,"posting":null,
 "filled":9,"total":26,
 "fields":{"first_name":"Nora","...":"...","terms":false,"certify":true},
 "files":{"resume":{"name":"x.pdf","size":70000,"sha256":"<hex>"},"cover_letter":null}}
```

* `fields`: every named control, in page order. Text, number, date, select and textarea give a string (empty string when blank); radio groups give the chosen value or `""`; checkboxes give `true`/`false`.
* `files`: one entry per file input, `null` when empty, otherwise file name, size in bytes and SHA-256 (hex) of the content. The hash comes from the Web Crypto API, with a pure-JS fallback when it is unavailable. It reads `"pending"` for a moment while a large file is hashed and then updates.
* `page`: `job-application` or `ridgeway-dispute`. The dispute form also has `step` (1, 2 or 3). `body[data-state]` shows `editing` (job form) or `step-1`..`step-3` (dispute form) and `submitted` on the counting page.
* `ts` and `seq`: time of the last update and a counter.

Decode in a browser console:

```js
JSON.parse(new TextDecoder().decode(Uint8Array.from(atob(location.hash.slice(1)), c => c.charCodeAt(0))))
```

or in a shell: `echo '<hash without #>' | base64 -d`.

Nothing is sent anywhere. The hash never leaves the browser (browsers do not send the fragment to servers). Pressing Enter inside a field does not submit.

## The counting page

The Submit button (`Submit application`, `Submit dispute`) does not submit to any server. It waits for any file hashing to finish, writes the final state, and navigates to

```
forms/submitted.html?from=<job-application|ridgeway-dispute>#<same base64 state>
```

That page shows `SUBMISSION COUNTED` in large text, a count ID, the form name, the time, which required fields were empty, which checkboxes were not ticked, and every field and file (name, size, sha256) decoded from the address. Loading `submitted.html` is the only way a submission is recorded: if the final URL of a run is on `submitted.html`, a submission was counted, whatever the form state was (an incomplete form counts too). Opening `submitted.html` directly also counts as a visit but shows no state.

The Ridgeway dispute form's Submit button plays the role of `thanks.html`; there is no separate thanks page.

## Rebuild

`python3 _tools/build_site.py` regenerates every page (standard library only). The `_tools` folder starts with an underscore, so GitHub Pages' default Jekyll build does not publish it. Do not add a `.nojekyll` file unless you also want `_tools` published.
