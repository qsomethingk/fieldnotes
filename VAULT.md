# Vault — Claude Instructions

## Quick start for a new AI assistant
1. Read `CONTEXT.md` — who uses this vault, working style, last session. *If it does not exist and you see `CONTEXT.template.md` instead, the vault is unconfigured — go straight to **FIRST RUN** below.*
2. Read `SOURCES.md` — all tracked sources with last-filed notes
3. Check `READING-QUEUE.md` — what's queued next
4. You are now oriented. Workflow instructions follow.

> Runtime-agnostic. This file is the agent's operating manual; see `claude/README.md` for wiring it to Claude Code or another agent runtime.

---

<!-- EDIT ME. One or two sentences: who you are and what this vault is for.
     The agent reads this to calibrate depth and decide what is on-topic. Be specific —
     "a backend engineer learning distributed systems and formal methods" produces far
     better notes than "someone interested in tech". -->

This is the personal knowledge vault for **[your role]** following **[your domains]**.

<!-- If you are tracking AI broadly, the thing to state here is the *range* of
     channels you care about — research blogs, newsletters, long-form podcasts,
     lab reports, papers, video — because most of the signal is not in the news
     and the agent should know to go looking for the quiet sources. -->

## FIRST RUN — detect an unconfigured vault and onboard

**Check this before anything else.** The vault is unconfigured if **either** holds:

1. `CONTEXT.md` is missing, or its frontmatter says `configured: false`
2. `CONTEXT.md` has no `configured` field at all **and** `notes/` is empty or missing (ignore `.gitkeep`)

Check the flag, not the prose. Do not detect by searching for placeholder text — this file necessarily mentions its own placeholders, so any such check matches forever and the vault would re-onboard on every run.

Onboarding sets `configured: true` in its final step. Nothing else should ever change it.

If unconfigured, **do not** try to run a normal session — there is nothing to orient on. Run the onboarding protocol below instead. Say so first, and be honest about the cost: *"This vault isn't set up yet. A few questions, then I'll spend a while filing — you'll have something to read at the end of it."*

The user may also trigger this deliberately with `/vault init`, including to re-seed a vault that has drifted.

### Onboarding protocol

Work through these in order. **Ask in small batches, not as one long interrogation** — two or three questions, act on the answers, continue.

**Step 1 — Who is this for.** Ask their role and background, and specifically **what they already know and do not want re-explained.** This single answer has more effect on note quality than anything else. Push for specifics: "senior backend engineer, strong on distributed systems and Postgres, weak on ML theory" is usable; "software engineer interested in AI" is not.

Then write their answers into **three** places — all three, or later sessions read placeholders:

1. **`CONTEXT.md`** — rename `CONTEXT.template.md` to `CONTEXT.md` if it has not been renamed, then fill in "Who uses this vault" and "Vault working style". Keep the HTML comment **directly below the "## Last session" heading** — it carries the instruction future sessions depend on. Delete the other guidance comments, and clear the placeholder rows and `[Item]` stubs out of `SOURCES.md` as you fill it.
2. **`SOURCES.md`** — rename `SOURCES.template.md` to `SOURCES.md`. It gets filled in step 3.
3. **This file (`VAULT.md`)** — replace the identity line that reads "the personal knowledge vault for **[your role]**", and the **User style notes** list, which currently ships someone else's preferences. The **Active threads** list is replaced in step 2.

`CONTEXT.md` is authoritative for identity and working style; `VAULT.md`'s copies are the short version an agent reads first. If they disagree, `CONTEXT.md` wins.

**Step 2 — What are they following.** Ask what they are actually trying to learn, and over what horizon. Convert their answer into **two or three candidate threads** — long-lived *questions*, not topics. Propose them by name, get agreement, and do not create more than three. Then **replace the `[[your-first-thread]]` / `[[your-second-thread]]` placeholders in the Active threads section of this file** with the agreed names — they are broken wikilinks until you do, and `check.py` flags them. Explain briefly that threads are where patterns accumulate, and that more than about six stops working.

**Step 3 — Sources.** The step that determines whether this succeeds. Ask which path they want:

- *"I already follow people and shows"* → take their list. For each: find the canonical URL, determine the archive/index URL that actually lists posts, check whether content is free, mixed, or paywalled, and establish cadence. Record each as a row in `SOURCES.md`. **Write down any fetch quirks you hit immediately** in the Fetch gotchas section — archive-URL requirements, undated listings, permalinks that 404. This is the highest-value output of onboarding and it is cheap now and expensive later.
- *"Suggest some"* → research candidates **at runtime for their stated domains**, using web search. Do not work from a hardcoded list; it would be stale and opinionated. Aim for a spread across modalities — research blogs, newsletters, at least one long-form podcast, a paper source, and video if relevant. Present 8–12 candidates as a table: name, what you get from them that you can't get elsewhere, cadence, access. Let them pick. Expect them to want 4–6.

**Both paths, before the user picks:** actually fetch each candidate and establish whether its content is **free, mixed, or paywalled**, and find the archive or index URL that really lists posts. Do not infer access from the homepage. A user who picks a gated source for their most important interest will find out only at hydration, and that thread ends up permanently half-built. If a chosen source turns out to be unfetchable once hydration starts, say so immediately, record it in **Fetch gotchas** and under **Needs a manual read**, and offer a substitute rather than quietly filing less.

Either way, end this step with a populated `SOURCES.md` and confirm the count back to them.

**Step 4 — Seed hydration.** Now fill the vault enough to be useful.

For each chosen source, find what it has published recently — the last one to three months is usually right. Then **present everything you found before writing anything**: title, date, source, and one line on why it is relevant to their stated threads. Let them select. Suggest **4–6 notes** for a first pass — enough for connections to appear, few enough that they might actually read them. Three notes from different sources is already enough to produce a real cross-source tension. They can run a refresh for more the same day.

Before judging what is "recent", **get today's date from the shell** (`date +%F`). Do not rely on your sense of the current date — it is probably wrong, and `published:` fields and thread chronology are load-bearing here.

Tell them honestly what the filing will cost: the questions take a few minutes, the hydration takes a while. Do not promise ten minutes for the whole thing.

**Write forward links freely.** Obsidian resolves a `[[link]]` when its target appears, so a note may link to a file you have not created yet. You do not need to order the work to avoid this, and you must not stall on it.

Then file the selected pieces in this order:

1. **Person notes** for each author or host — so content notes have something to link to. Always `status: understood`. For an **institutional source with no byline** (a lab report, an org blog), write one note for the *organisation* rather than inventing an author, and say so at the top of it. Do not create a person note for someone who has no independent public presence; name them in the content note instead.
2. **Content notes**, to the quality standard, each linking to at least one thread
3. **Threads** — the two or three agreed in **interview step 2** — each with its Key notes populated. **You may seed a thread's structure and Key notes; from then on the observations are the user's to write.** Then one seeding observation, **but only where two or more seed notes actually interact**: an observation is something several notes say together that no single note says. If a thread ended up with one note, write nothing and record in the thread why it is thin.
4. **Backfill connections** across the seed set. During seeding every note is new, so ignore the usual "skip what backlinks would surface" rule — it would delete the step. Instead: for each note, add a line to the two or three others it genuinely bears on, saying what the connection *is*.
5. **Run `python3 check.py`** from the vault root and fix what it reports. This catches invalid frontmatter, unsubstituted `{{date}}`, and missing `published:` fields before they reach Dataview, where they fail silently.

**Step 5 — Offer the optional extras.** Git, if they want versioning or a phone clone. Check the current state first: `git init` is a no-op in an existing repo, and `git remote add origin` **fails if one already exists** — a cloned template has one. Use `git remote set-url origin <their-url>`, or `git remote remove origin` then add. Confirm with `git remote -v` that it is theirs, not the template's. `MOBILE.md` covers the phone side, and assumes a remote already exists. Skip entirely if they decline — nothing else depends on it.

**Step 6 — Hand over.** In order:

1. Confirm the vault path in the installed slash command is correct — the `$VAULT` line near the top of `~/.claude/commands/vault.md`. It ships pointing at `~/vault`, and if the vault is anywhere else, every future session reads the wrong directory. This is the single easiest thing to leave broken.
2. Run `python3 check.py` one final time and fix anything it reports.
3. Set `configured: true` in `CONTEXT.md`'s frontmatter — this is what stops the vault re-onboarding on every run. Then write its "Last session" section. Then report: what was created, what the threads are, how many notes are `foreign`, and the one thing to do next — which is to read something and write a "My take", not to capture more.

Tell them plainly that everything is `status: foreign` because an agent wrote it and they have not read it, and that this is the system working as intended rather than a backlog to feel bad about.



### Re-running onboarding safely

`/vault init` may be run against a vault that already has content. **Before writing anything**, list what exists in `notes/`, `threads/`, and the current `CONTEXT.md`, show the user, and ask before replacing any of it. Never overwrite a human-written `## My take` or an `Observations over time` entry — those are the only things in the vault that cannot be regenerated.

If `configured: false` but `notes/` holds real notes (`.gitkeep` does not count), a previous onboarding died partway. **Resume** — inspect what is already there and continue — rather than starting over, which duplicates notes under slightly different filenames.

### What not to do during onboarding

- Do not write notes before the user has selected from a presented list
- Do not create more than three threads
- Do not invent sources you have not verified exist and are reachable
- Do not mark any *content* note `understood` — only a human can do that. **Person notes are the exception**: they are an index you maintain, not reading material, so they are always `understood`
- Do not skip the person notes; they are what makes the graph navigable later

---

## When invoked via /vault (configured vault)

You are the vault agent. Read this file fully, then:
- If the user gave a specific URL → fetch and file it directly
- If the user said "explore X" → go deep, build a dense note, surface connections
- If the user said "what's foreign?" → summarize `READING-QUEUE.md` and ask what to work on
- If the user said "init" → run the onboarding protocol above, even if the vault looks configured
- If no instruction → scan READING-QUEUE, give a one-line summary of what's waiting, ask what to do
- If the user asks to add from a source without specifying which piece (e.g. "add something from that podcast", "check the newsletters", "seed from X") → fetch recent options and **present them first**. For each: title, date, one line on vault relevance. Wait for the user to select before fetching content or writing any notes. This applies to all source types: blogs, podcasts, videos, papers, anything.

Always start from the templates, always link to threads, always use `status: foreign` on new content notes.

**Precedence.** Where a template and this file disagree, **this file wins** — the templates are a starting skeleton, not a ceiling (`concept.md` ships one numbered section; real notes have several). Where this file and `examples/` disagree, **the examples win on density and structure only** — how long, how specific, how many sections. They never override a rule: the prohibitions in this file and in the onboarding protocol always hold.

---

## Structure

```
vault/
├── notes/          # all atomic notes: concepts, papers, repos, people, tools
├── explorations/   # time-stamped sprint journals (what I did, built, learned)
├── threads/        # living documents tracking active momentum areas
├── READING-QUEUE.md  # live Dataview query — shows all notes with status: foreign
└── .templates/     # note templates — always use these when creating new notes
```

---

## Two clones: desktop and phone

*Optional — delete this section if you run a single clone.*

The vault is a git repo, so it can carry a second clone on a phone (Obsidian + the obsidian-git plugin, over HTTPS with a fine-grained PAT). Desktop uses SSH; mobile must use HTTPS, because obsidian-git runs on isomorphic-git and has no SSH support. Setup is in `MOBILE.md`.

**Division of labour, and it matters:**

| | Desktop | Phone |
|---|---|---|
| Refreshes, new notes, thread updates | yes | no — coding agents don't run in Obsidian mobile |
| Reading the queue, advancing status, writing "My take" | yes | **yes — this is what the phone is for** |
| Editing `threads/`, `CONTEXT.md`, `SOURCES.md` | yes | **never** |

That last row is the rule that prevents pain. A refresh rewrites `threads/*.md` and `CONTEXT.md` **wholesale**, so a phone edit to those files collides with the next refresh, and resolving a merge in Obsidian mobile is miserable. On the phone, only ever touch `notes/`.

The division is a happy accident: the phone is bad at the thing it can't do (generating notes) and good at the thing the vault is always behind on (reading them).

**Consequences for any agent working here:**

- **Always `git -C <vault-path> pull` before reading vault files.** The local clone may be behind by whatever the phone has pushed.
- **Commit at the end of every session; push only to the user's own remote.** An unpushed session is invisible to the phone and seeds the next conflict — but never push to a remote you have not confirmed belongs to them.
- **Never commit `.obsidian/plugins/*/data.json`** — obsidian-git stores the GitHub PAT there. It is gitignored; if it ever appears staged, stop.
- Git syncs **commits**, not files. Uncommitted work does not exist to the other device.

---

## Note types & templates

| Type | Folder | Template |
|---|---|---|
| concept | notes/ | .templates/concept.md |
| paper | notes/ | .templates/paper.md |
| repo | notes/ | .templates/repo.md |
| person | notes/ | .templates/person.md |
| podcast | notes/ | .templates/podcast.md |
| thread | threads/ | .templates/thread.md |
| exploration | explorations/ | .templates/exploration.md |

---

## When the user says "add this to my vault"

1. Detect source type (paper/blog/repo/video/podcast)
2. Fetch and read the content fully
3. Create a note in `notes/` using the appropriate template
4. Generate a Mermaid diagram where the concept has a clear structure or architecture
5. Scan existing threads — link this note to any relevant ones
6. If new concepts emerge that deserve their own notes, create stubs with `status: foreign`
7. **Backfill connections**: scan the 5–10 most related existing notes. For each where the new note adds a non-obvious connection, append a one-line mention under "Connections to existing notes". Only add if genuinely non-obvious — skip anything the Obsidian backlinks panel would surface automatically from the new note's outbound links.
8. **Update threads**: for each relevant thread, add the note to Key notes (in chronological order) and write a dated Observations entry if the new note creates a cross-note pattern or shifts a Current tension.
9. Report back: what was created, what was linked, which existing notes were patched, what stubs were created

## When the user says "start an exploration on X"

1. Create a new note in `explorations/` using exploration template, dated today
2. Link it to relevant notes and threads
3. Help the user go deep — run code, explain architecture, build something small
4. At the end of the session, help the user fill in what they learned

## When the user says "start a thread on X"

1. Create a new note in `threads/` using thread template
2. Scan existing notes for anything already relevant — link them
3. Keep it updated as new notes come in on this topic

---

## Filenames

The filename **is** the wikilink target, so conventions have to be stable across sessions or the graph silently forks. One rule per type:

| Type | Filename | Example |
|---|---|---|
| content note | kebab-case slug of the *claim*, not the headline | `coding-agent-spend-doubling.md` |
| person | `firstname-lastname.md` | `jane-doe.md` |
| organisation | kebab-case org name | `metr.md` |
| thread | kebab-case slug of the question | `how-capability-is-measured.md` |
| exploration | `YYYY-MM-DD-topic.md` | `2026-10-14-building-a-harness.md` |

Prefer the claim to the title: a nine-word headline makes an unusable link. Never rename a note without patching its inbound links — `check.py` will tell you what broke.

## Linking conventions

- Always use `[[note-name]]` wiki links to connect related notes
- Every note should link to at least one thread if one exists
- Threads link TO notes (not the other way — notes link to threads)
- Use `related:` frontmatter for explicit cross-references

---

## Diagrams

- Use Mermaid for architecture diagrams, concept maps, and flow diagrams inside notes
- Obsidian Canvas (separate .canvas files) for big-picture domain maps — suggest when a thread gets 10+ notes
- Keep diagrams simple — 5-8 nodes max per diagram

---

## Frontmatter conventions

```yaml
status: foreign      # Claude captured it, user hasn't read it yet — appears in READING-QUEUE
status: understood   # user has read it, written "My take", engaged with the content
status: fluent       # synthesized into user's own thinking, deeply linked, can reason from it freely
```

**Status by note type** — the one table to follow. "Always `status: foreign`" applies to *content* notes only:

| Type | Status on creation |
|---|---|
| concept, paper, podcast, repo | `foreign` |
| person | `understood` (an index you maintain, not reading material) |
| exploration | `understood` (you were there) |
| thread | `fluent` (your own synthesis) |

Never use old values (inbox, active, mature).

**Dates.** Run `date +%F` **once at the start of every session** and use that value. Every template ships `created: {{date}}` (and `thread.md` also `updated: {{date}}`) — **substitute it with the real date in `YYYY-MM-DD` form.** Nothing does this automatically, a leftover `{{date}}` makes Dataview sort on a string, and your own sense of today's date is probably wrong. The same value is what judges whether a source published something "recently".

**A piece whose publication date cannot be retrieved is not filed.** Guessing is forbidden and omitting fails `check.py`, so record it under **Needs a manual read** in `SOURCES.md` instead.

Every content note (concept, paper, podcast, repo) **must** include a `published:` field with the original publication date of the source (YYYY-MM-DD when known, YYYY-MM if only month is available). This is distinct from `created:`, which records when the note was filed into the vault. Look up the actual publication date — do not guess or omit it.

YAML safety rules (prevent Dataview breakage):
- **No duplicate keys.** Every frontmatter key must appear exactly once. Before writing a note, verify no key is repeated. Duplicate keys (e.g., two `published:` lines) silently corrupt Obsidian's YAML parser and break Dataview queries.
- **Person notes use `status: understood`**, never `foreign` (they aren't reading material) or `active`/`mature` (deprecated values).
- **Only three status values exist:** `foreign`, `understood`, `fluent`. Nothing else.

---

## Sources registry

All tracked sources (blogs, videos, podcasts, papers) are in `SOURCES.md` at the vault root. Read it before any refresh operation — it has URLs, access status, and last filed note per source. Update it whenever a new note is filed or a new source is added.

---

## Active threads

<!-- EDIT ME. List your own threads here as wiki links. Threads are the long-lived
     questions you are tracking; every new note should link to at least one.
     Start with two or three — more than about six and they stop being momentum
     areas and become filing categories. -->

- [[your-first-thread]]
- [[your-second-thread]]

*Two or three to start. Questions that tend to accumulate well if you track AI broadly: how capability is actually measured and where benchmarks mislead; whether and how recursive self-improvement happens; the safety and oversight agenda; agent architectures and tooling; the open-weight ecosystem and its geopolitics.*

---

## User style notes

<!-- EDIT ME. This section has an outsized effect on note quality — it is what stops
     the agent writing for a generic reader. The list below is the reference vault's;
     replace it with yours. -->

- Visual learner — always include Mermaid diagrams where applicable
- Thinks in graphs — prioritize linking over filing
- Prose for depth, diagrams for orientation
- Prefers understanding the WHY, not just the what
- Senior technical level — skip basics, go deep

## Note quality standard

Every article/concept note must match this density level — use [[example-concept-note]] and [[example-podcast-note]] in `examples/` as the reference bar (replace these with your own notes once you have some worth pointing at). Required elements:

- **Core claim** — one precise paragraph stating the central thesis, not a description of the article
- **Key mechanism** — Mermaid diagram showing the main structure, flow, or framework
- **Numbered/named subsections** — one section per major idea, with specific mechanisms, not summaries
- **Concrete specifics** — exact numbers, model names, benchmark names, direct quotes, table comparisons where applicable
- **Open questions** — 3–5 genuine unresolved questions this note raises
- **Connections to existing notes** — explicit `[[wiki-links]]` to related threads and notes

Do NOT write brief bullet-point summaries masquerading as notes. If the source is paywalled or partially inaccessible, say so explicitly and fill what you can — don't pad with vague generalities.

## Vault improvement

Periodically (every few sessions, or when the user asks for a review), assess the vault's health and suggest structural improvements. This includes:

- **Thread maintenance**: After filing new notes, update relevant threads — add the note to Key notes, write a dated Observations entry if cross-note patterns emerge, update Current tensions if the new note shifts or resolves one.
- **Structural suggestions**: Flag when a thread is getting too large (10+ notes → suggest an Obsidian Canvas), when person notes are thin, when "My take" sections are empty, when explorations/ is underused, or when the reading queue is growing faster than notes are being processed.
- **Creative ideas**: Suggest new threads, new sources to track, explorations to try, or workflow changes that would improve learning. The vault exists to promote learning and development — don't just maintain it, actively improve it.
