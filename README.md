# fieldnotes

**A template for building a knowledge graph that follows AI — and gets richer every time you add to it.**

Field notes on a field that will not hold still. Not a clipping service, not a summary pile — a vault where the connections between the things you read are maintained deliberately, so that after a few months you can see patterns that were not visible in any individual piece.

---

## The problem

Following AI properly means following it across a dozen channels at once. The research blogs. The newsletters nobody outside the field reads. Three-hour podcast interviews where someone concedes something they would never write down. Lab reports, system cards, arXiv papers, conference talks, long YouTube explainers. Most of the signal is not in the news — it is in the quiet voices, and it arrives as audio and video as often as text.

Two things then go wrong.

**Summaries decay.** You read a good piece, extract the gist, and three months later you have a sentence that has lost everything that made it useful — the number, the mechanism, the specific concession, the thing you disagreed with.

**Nothing connects.** Each piece lands in isolation. You never notice that the person confidently arguing X in March quietly abandoned it by August. You never notice that two researchers who appear to disagree actually share a premise and differ on one narrow empirical question. You never notice the same mechanism showing up in four unrelated places. Those are the only observations worth having, and they are invisible if every note is a dead end.

What you end up with is a database of things you have encountered. Which is not understanding.

## What this is instead

A vault designed so that **every addition increases the value of what is already there.** Four mechanisms do that work, and they are the actual content of this repo:

### 1. Distillation, not summary

Notes are held to a standard: a **core claim** stated as an argument you could disagree with, a **Mermaid diagram** of the mechanism, named subsections with specific numbers and direct quotes, and genuine **open questions**. A note that merely describes its source has failed — the test is whether the note is more useful than re-reading the original.

### 2. Backfill — the step that compounds

This is the one that matters most and the one no tool does for you.

When a new note is filed, the agent goes **back into the five to ten most related existing notes** and appends a line to each where the new material adds something non-obvious. Obsidian gives you backlinks from the new note outward for free. What it will not do is patch the old notes to point *forward*.

Done on every pass, the corpus densifies rather than just growing. A note written in March keeps acquiring context through October. This is the difference between a collection and a graph, and it costs about fifteen minutes per refresh.

### 3. Threads — where patterns become visible

A thread tracks a long-lived **question**, not a topic. Each one holds:

- **Key notes** — every note in the thread, each with its specific finding
- **Observations over time** — *dated* entries, appended never overwritten, written only when several notes together say something no single note says
- **Current tensions** — live disagreements, revised in place as evidence arrives, with revisions marked

The dated observations are the payload. Read three of them in sequence and you are looking at your own understanding changing over months, with the evidence attached. You cannot get that from any individual note, and you cannot reconstruct it later from memory.

### 4. Person notes — catching people change their minds

A note per person you follow, holding their work **chronologically by publication date**, and a section most people never think to create: **Positions they have publicly revised.**

Following a field means watching smart people update. Almost nobody records it, so the revision dissolves into a vague sense that someone's view "shifted". Written down with both sides, both dates, and the trigger, it becomes the most valuable thing in the vault — and it makes you a much better reader of everyone else.

### And one honesty mechanism

Three statuses, because an agent can hand you a hundred accurate notes in a week and you will know almost none of it:

```yaml
status: foreign      # an agent captured this. No human has read it.
status: understood   # I have read it and written down what I think.
status: fluent       # I can reason from this without re-reading it.
```

New notes are *always* `foreign` — the agent cannot mark its own output as read. Advancement is manual and requires writing a position in the note's **My take** section. If you can't write the take, you didn't understand it.

`READING-QUEUE.md` is a live Dataview query listing everything still `foreign`, so the gap between what you have captured and what you have absorbed is visible every time you open the vault. There is no setting to hide it.

---

## What's here

```
VAULT.md                 the agent's operating manual — the core artifact
CONTEXT.template.md      who you are; what the agent must not re-explain (onboarding fills this)
SOURCES.template.md      tracked-source registry, fetch gotchas, backlog (onboarding fills this)
READING-QUEUE.md         the Dataview query that surfaces unread notes
check.py                 vault integrity check — run before every commit
.templates/              7 note templates — concept, paper, podcast, repo, person, thread, exploration
claude/commands/vault.md the /vault slash command
claude/README.md         wiring it to Claude Code, or another runtime
MOBILE.md                optional: a second clone on your phone
examples/                annotated examples showing the quality bar
```

Three directories you create on first run:

| | What it holds | Who writes it |
|---|---|---|
| `notes/` | atomic notes — one source or one concept each | the agent |
| `threads/` | living documents tracking long-lived questions | **you** |
| `explorations/` | session journals: what you built, ran, got wrong | you, with the agent |

Notes link *to* threads; threads link *to* notes. The asymmetry is deliberate — it makes a thread a view over the corpus rather than a folder.

### Note types

**concept** and **paper** for ideas and research. **podcast** for interviews, which is where the vault earns its keep, because long-form audio reliably contains claims that exist nowhere else and are unsearchable until someone extracts them. **repo** for code worth understanding. **person** for people you follow. **thread** and **exploration** as above.

---

## A refresh, in practice

The recurring operation. You run `/vault` and the agent:

1. **Pulls** (so a second clone on your phone hasn't left it stale), then reads `CONTEXT.md`, `SOURCES.md`, and the queue
2. **Sweeps your tracked sources** for anything published since the last pass — and `SOURCES.md` records the last filed note per source, so it doesn't re-discover the same archive URLs and paywalls every time
3. **Presents what it found** before writing anything, so you choose what gets filed
4. **Writes notes** to the quality standard, each with a diagram and links to the relevant threads
5. **Backfills connections** into related existing notes — step 2 above
6. **Updates threads**: new notes into Key notes, a dated observation if a cross-note pattern emerged, tensions revised if something shifted
7. **Overwrites the "Last session" section** of `CONTEXT.md` so the next session — or a fresh agent with no memory — knows where things stand, including what it got wrong
8. **Commits and pushes**, after validating frontmatter

Steps 5 and 6 are the compounding. Skip them and you have a note-generation script.

---

## Getting started

Two manual steps, then the agent sets the vault up by interviewing you.

```bash
git clone https://github.com/qsomethingk/fieldnotes.git my-vault
cd my-vault
rm -rf .git && git init                      # make it yours

cp claude/commands/vault.md ~/.claude/commands/   # resolves to your cwd if it holds VAULT.md
```

Open the folder in Obsidian and install the **Dataview** plugin — without it `READING-QUEUE.md` renders as a code block rather than a live query.

Then:

```
/vault
```

It detects that the vault is unconfigured and runs onboarding instead of a normal session.

### What onboarding does

A short interview, in small batches rather than one long questionnaire — then it files for a while:

1. **Who you are** — your background, and specifically **what you already know and don't want re-explained.** This answer affects note quality more than anything else in the system.
2. **What you're following** — turned into two or three threads. Long-lived *questions*, not topics. It won't create more than three.
3. **Sources** — either you list the people and shows you already follow, or you ask for suggestions and it researches candidates for your stated domains, presenting 8–12 as a table with cadence and access so you can pick. Either way it resolves the archive URLs, checks what's paywalled, and writes `SOURCES.md`.
4. **Seed hydration** — it finds what your chosen sources published recently, **shows you everything before writing anything**, and files the 4–6 you pick: person notes first, then content notes, then your threads with their Key notes populated and a first observation where two or more notes actually interact. Then it backfills connections and runs `check.py`.
5. **Hands over** — tells you what exists, how many notes are `foreign`, and that the next move is to read one and write a take, not to capture more.

The questions take a few minutes; the filing takes a while longer. You end with a vault that already has a graph in it. That matters more than it sounds: the usual failure mode for systems like this is that the first few notes feel like expensive summaries, because there's nothing to connect them to and the threads have no observations yet. Seeding past that point is the difference between the thing clicking in an evening and being abandoned in a fortnight.

Re-run it any time with `/vault init` — useful if your interests move and the vault's scope needs resetting.

### After that

`/vault` with no arguments reads the queue and asks what you want to do. Or be specific:

```
/vault add this https://example.com/some-essay
/vault what's foreign?
/vault connect                     # surface non-obvious links across recent notes
/vault update <note>               # deepen a note, write a take, advance its status
```

---

## Optional: your phone

The vault is a git repo, so a second clone on a phone works, and the division of labour is a happy accident — a phone cannot run a coding agent, but it is well suited to the thing a vault is always behind on, which is reading. Setup, including one security trap worth knowing about, is in `MOBILE.md`.

One rule: on mobile, only ever edit `notes/`. A refresh rewrites `threads/` and `CONTEXT.md` wholesale.

---

## What this doesn't do

- **It does not make you read.** It makes not-reading visible. Those are different.
- **The queue will grow faster than you process it.** Capture is cheap and reading is not. Expect to schedule processing sessions deliberately, and expect to resist the temptation to capture instead.
- **Onboarding is an interview, not a script.** It needs you present, and cannot be run unattended.
- **Quality depends on a capable model.** The standard means reconstructing an argument, not summarising it. Weaker models fail recognisably: correct section headings, bullet-point filler underneath.
- **It needs a quality exemplar.** The standard is enforced by pointing at concrete notes. Delete `examples/` before you have replacements and output drifts toward summary.
- **Threads need you.** Notes can be generated; the dated observations that make threads valuable cannot. This is the first thing to lapse and the most expensive to lose.
- **Dense notes accumulate verbatim quotation.** Fine privately; audit before publishing a corpus.
- **There is no measure of comprehension.** `understood` means you wrote something down, not that it was any good.

---

## Licensing

Method is **MIT** — `VAULT.md`, templates, slash command, config. Prose in `MOBILE.md` and `examples/` is **CC BY 4.0**. See `LICENSE` and `LICENSE-CONTENT`.

Examples are illustrative, written for this repo. Their `[[wikilinks]]` point at notes you will create and will render greyed out until you do.
