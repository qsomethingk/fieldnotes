<!-- CONFIGURE ME: set your vault path on the next line, or leave it and let
     resolution find the vault you are standing in. -->
**`$VAULT` = `~/vault`**

---

## Step 0a — resolve `$VAULT`, and verify it

Resolve in this order and stop at the first that works:

1. A path the user gave in the invocation
2. **The current working directory, if it contains `VAULT.md`**
3. The configured value above

Then **assert `$VAULT/VAULT.md` exists.**

If it does not, **stop and ask where the vault is.** Do not create anything, and do not treat it as an unconfigured vault. A directory with no `VAULT.md` means the *path is wrong* — onboarding into it would write notes with no templates and no quality exemplar, while the real vault sits untouched somewhere else. This is the most damaging failure available and it is silent, because "missing files" looks identical to "fresh vault".

## Step 0b — sync before anything else

The vault is also edited from a phone (Obsidian + obsidian-git), so the local clone may be behind. **Run `git -C "$VAULT" pull` before reading any vault file** (where `$VAULT` is your vault path — set it below). Reading first means orienting on stale state — notes may already be `understood`, and CONTEXT.md may be out of date.

Handle the outcomes:

- **Pull brought commits** → report in one line what arrived (e.g. "pulled 2 commits from phone: 3 notes advanced to understood"). Phone commits are usually status changes and "My take" text.
- **Already up to date** → say nothing, continue.
- **Uncommitted local changes** → list them before pulling. They are either the user's in-progress work or phone edits that never pushed. Do not stash or discard without asking.
- **Merge conflict** → **stop and tell the user.** Do not auto-resolve. Conflicts here almost always mean a phone edit collided with a refresh that rewrote `threads/` or `CONTEXT.md`, and the user needs to decide which side wins.
- **Not a git repo, or no remote configured** → say one line ("no remote, skipping sync") and **continue normally.** This is the expected state for a fresh template clone and for anyone running a single machine. It is not a problem and does not need a question.
- **Pull fails** (network, auth) → say so and ask whether to continue offline. Reading offline is fine. Avoid a *refresh* offline **if the vault has a remote that other clones push to**, since a refresh rewrites `threads/` and `CONTEXT.md` wholesale. With no remote there is nothing to conflict with, so onboarding and refreshes are both safe.

Then read `$VAULT/VAULT.md` fully and orient yourself to the vault — structure, templates, status pipeline (foreign → understood → fluent), active threads, and linking conventions.

## Step 1 — is this vault configured?

Read the **FIRST RUN** section of `VAULT.md` and apply the detection rule there. It is the single source of truth for this; do not re-derive it.

In short: `CONTEXT.md` missing or `configured: false` means unconfigured → **run the onboarding protocol in `VAULT.md`** rather than attempting a normal session, because there is nothing to orient on and the reading queue will be empty.

Onboarding ends with a seeded vault: `CONTEXT.md` and `SOURCES.md` written, `VAULT.md`'s placeholders replaced, two or three threads created, and 4–6 notes filed with person notes and backfilled connections.

Force it with `/vault init` to re-seed a vault that has drifted — it asks before overwriting anything.

If the vault *is* configured, continue below.

You are now the vault agent. Help with whatever comes next:

- **"add this [URL/topic]"** → fetch fully, create a dense note with Mermaid diagram, link to relevant threads, report what was created
- **"explore [topic]"** → go deep on something already in the vault or new — fetch, build note, surface connections to existing notes, suggest what to read next
- **"what's foreign?"** → summarize all unread notes and ask what to work on
- **"connect"** → scan recent notes and surface non-obvious connections the user may have missed
- **"update [note]"** → open a note and help the user deepen it, add My take, or advance its status

If no instruction is given after /vault, read the READING-QUEUE (`$VAULT/READING-QUEUE.md`) and give a one-line summary of what's waiting, then ask what to do.

At natural stopping points and at the end of any vault session, overwrite the "Last session" section in `$VAULT/CONTEXT.md` with a one-line summary of what was done and what's pending. Also write session memory to your agent's own memory directory, if it has one, for cross-session continuity.

## Closing the loop — commit and push

End every substantive session by committing. **Push only if a remote exists** — if there is none, commit and say so; do not treat it as an error. Where a remote does exist, an unpushed session is invisible to your other clones and seeds the next conflict.

- Separate commits for distinct kinds of work (a refresh, a hygiene fix, reading progress) rather than one mixed commit. The log is the vault's changelog — it is how you reconstruct what you learned when.
- Never commit vendored plugin bundles under `.obsidian/plugins/*/` — only the small `.json` config files. `.obsidian/plugins/*/data.json` is gitignored because obsidian-git stores the GitHub PAT there; if that file ever shows up staged, stop.
- Before committing, run **`python3 check.py`** from the vault root. It checks duplicate YAML keys, status values, person-note status, missing `published:`, unsubstituted `{{date}}`, empty "My take" on `understood` notes, and broken wikilinks. Dataview fails *silently* on bad frontmatter, so this is the only thing standing between a typo and a quietly wrong reading queue.
