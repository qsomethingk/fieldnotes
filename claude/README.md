# Wiring the vault to an agent

The vault is runtime-agnostic. `VAULT.md` at the repo root is the operating manual; all a runtime has to do is load it and point the agent at the vault directory.

## Naming

Three things with three names, which is deliberate:

| | |
|---|---|
| **fieldnotes** | this repo — the method and templates |
| **your vault** | the Obsidian vault you build with it. "Vault" is Obsidian's own term |
| **`/vault`** | the command that operates on your vault |

The command is named after what it acts on rather than after the project, the way `git` is named for what it does rather than for your repo.

If you already have a `/vault` command, renaming is a single `mv` — **the filename is the command name.** Call it `/fieldnotes`, `/fn`, whatever; nothing inside the repo depends on it.

## Claude Code

Copy the slash command into your commands directory:

```bash
mkdir -p ~/.claude/commands
cp claude/commands/vault.md ~/.claude/commands/
```

Then **open `~/.claude/commands/vault.md` and set your vault path on line 2**:

```markdown
**`$VAULT` = `~/vault`**
```

That's the only configuration. Invoke with `/vault`, optionally with an instruction:

```
/vault
/vault add this https://example.com/some-essay
/vault what's foreign?
/vault connect
```

### What the command does

Three things, in order:

1. **`git pull` first.** Before reading anything. If you run a second clone on a phone, the desktop may be behind, and orienting on stale state produces duplicate notes and wrong "last session" summaries. The command has explicit handling for conflicts — it stops rather than auto-resolving.
2. **Loads `VAULT.md`, `CONTEXT.md`, `SOURCES.md`.** In that order. `CONTEXT.md` is what calibrates depth; without it you get notes written for a generic reader.
3. **Commits and pushes at the end,** with a frontmatter validation pass first.

If you only ever use one machine, you can delete Step 0 and the closing section. Everything else still works.

### Global vs project scope

Putting the command in `~/.claude/commands/` makes it available in every session, which is what you want — the vault is not a project you `cd` into. If you'd rather scope it, use `.claude/commands/` inside the vault directory and invoke from there.

## Other runtimes

Nothing in `VAULT.md` is Claude-specific. It needs an agent that can read files, write files, fetch web pages, and run git. To port it:

- **Agent with a system prompt** (Kiro, Cursor rules, a custom harness) — load `VAULT.md` as the prompt and pre-load `CONTEXT.md`, `SOURCES.md`, and `.templates/`. The reference setup did this with a `kiro-cli` agent config bound to a keyboard shortcut.
- **Plain chat with file access** — paste `VAULT.md` at the start of the session. Works, but you lose the automatic pull and push, so do those by hand.
- **Scheduled / headless** — the refresh workflow in `VAULT.md` is deliberately sequential and can be driven unattended. Two caveats: do **not** run an unattended refresh against a vault with a second clone unless the pull succeeds first, and do not run onboarding unattended — it is an interview and needs a human.

## Required tool permissions

| Capability | Used for |
|---|---|
| File read/write | notes, threads, templates |
| Web fetch | retrieving sources — the bulk of a refresh |
| Web search | finding what a tracked source published recently |
| Shell | `git pull` / `commit` / `push`, and the frontmatter validator |

Web fetch is the one that matters most. An agent without it can organise the vault but cannot fill it.

## A note on model choice

The quality bar in `VAULT.md` is demanding — a dense note means reading a full source and reconstructing its argument, not summarising it. Smaller or faster models tend to fail in a specific and recognisable way: they produce the right *section headings* with bullet-point filler underneath, which is precisely what the standard forbids.

If notes come back structurally correct but thin, that is a capability signal, not a prompting problem.
