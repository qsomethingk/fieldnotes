---
configured: false
---

# Vault Context

> **New AI assistant**: read `VAULT.md` next for full workflow instructions.
> Required tool permissions: web fetch, web search, file read/write, shell (for git).

<!--
  Rename this file to CONTEXT.md and fill it in.

  This is the smallest file in the vault and it has the largest effect on output
  quality. VAULT.md tells the agent *how* to work; this tells it *who it is working
  for*. Without it you get competent notes written for nobody.
-->

---

## Who uses this vault

<!-- Role, background, and — most importantly — what NOT to explain.
     Being explicit about your existing knowledge is what stops every note
     opening with a paragraph of material you already know.

     Example:
       Backend engineer, 8 years. Comfortable with distributed systems,
       Postgres internals, and Go. Do not re-explain CAP, consensus basics,
       or SQL. Weak on formal methods and on ML beyond the basics.
-->

[Your role and background. State plainly what the agent should not re-explain.]

Active exploration areas: [the three or four things you are actually trying to learn]

This vault covers: [the topic boundary — what belongs here and what doesn't]

---

## Vault working style

<!-- Preferences about how the agent behaves, not about content.
     The reference vault's list is below; keep what fits, cut the rest. -->

- Terse responses. No emoji. No trailing summaries after completing vault work.
- After creating a note, report what was created and what was linked — then stop.
- Write the "Last session" section below proactively at natural stopping points.
  **Overwrite it — don't append.** Don't wait to be asked.
- Commit and push vault changes after any substantive session work.
- Don't pre-filter topics or scope — ask if unclear.

---

## Last session

<!--
  The agent overwrites this every session. It is the vault's working memory and the
  reason a fresh agent can pick up where the last one stopped.

  Write it for an agent with no memory of the session, not for yourself. What was
  done, what was decided, what is still pending, and — the part that actually
  matters — what you got WRONG and had to correct. That last bit is what stops the
  next session repeating the mistake.

  It will grow long. That is fine; it is cheaper to read than to reconstruct.
-->

Nothing yet — this is a fresh vault. After your first `/vault` session the agent
will replace this paragraph with a summary of what it filed, what it linked, what is
still queued, and anything it got wrong.
