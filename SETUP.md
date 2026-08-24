# Setup

How this profile repository works, and what has to be configured once.

## What runs here

| Workflow | Trigger | What it does |
| --- | --- | --- |
| [`metrics.yml`](.github/workflows/metrics.yml) | daily + manual | Renders GitHub stats to `assets/metrics.{light,dark}.svg` and commits them |
| [`quality.yml`](.github/workflows/quality.yml) | push, PR, weekly | Lints Markdown, verifies every link resolves, checks the four READMEs are in sync |
| [`snake.yml`](.github/workflows/snake.yml) | manual (opt-in) | Generates the contribution-graph snake animation |

Dependabot ([`dependabot.yml`](.github/dependabot.yml)) opens a monthly PR when a
pinned action needs bumping.

## One-time configuration

### 1. Create a token for metrics

The metrics action talks to the GitHub GraphQL API, which **classic** personal
access tokens can use - fine-grained tokens cannot.

1. <https://github.com/settings/tokens> → *Generate new token (classic)*
2. Name it `METRICS_TOKEN`, set an expiry you'll actually remember to renew
3. Scopes: `read:user`. Add `repo` only if you want private-repository activity
   included in the stats
4. Copy the token

### 2. Store it as a repository secret

`Settings → Secrets and variables → Actions → New repository secret`

- Name: `METRICS_TOKEN`
- Value: the token from step 1

### 3. Allow workflows to push

`Settings → Actions → General → Workflow permissions` → *Read and write
permissions*. The metrics workflow commits the rendered SVGs back to the repo.

### 4. Run it once

`Actions → metrics → Run workflow`. After ~1 minute the placeholder SVGs in
`assets/` are replaced with real renders. Nothing else needs to happen; the
schedule takes over from there.

## Editing the README

There are four language versions and CI checks they stay parallel:

- same number of `##` sections in each file
- each file links to the other three
- every local path referenced (`assets/…`) actually exists

So when you add a section to `README.md`, add it to `README.fr.md`,
`README.ru.md` and `README.ua.md` too - otherwise `quality` goes red.

Run the same checks locally before pushing:

```bash
python .github/scripts/check_i18n.py
npx markdownlint-cli2
```

## Housekeeping

- `lychee.toml` excludes `github.com/DmytroPalahin/uvkit` while that repo is
  still private. Remove that line once it's public.
- The **Selected work** table is manual on purpose. A hand-picked list of four
  projects with one honest sentence each reads better than an auto-generated
  list of everything you've ever pushed.
