---
type: person
status: understood
tags:
  - example
  - scaling-laws
related:
  - example-thread-ai-safety
  - example-concept-note
created: 2026-01-15
---

<!-- ILLUSTRATIVE EXAMPLE. Person notes are the highest-leverage and least obvious
     part of this system, so this one is annotated rather than filled with invented
     claims about a real researcher.

     Person notes are status: understood, never foreign — they are not reading
     material, they are an index you maintain. -->

## Who they are

Affiliation, what they actually work on, and the one or two things they are *the* source for. Two or three sentences. Resist writing a bio — the agent can fetch a bio; what you want recorded is **why this person is worth tracking**.

## Why they matter

The section that earns the note. Not "writes about AI" — specifically what you get from them that you cannot get elsewhere. Good versions tend to be one of:

- **the only person with access** to some data or environment
- **the best mechanism-level explainer** of a thing everyone else describes vaguely
- **the most useful wrong position** — someone whose errors are informative because they are explicit and dated
- **the person who publishes their own concessions**, which makes them unusually easy to track over time

Be concrete and quote them. A person note that could describe four different researchers is not doing any work.

## URL

Primary site, plus whichever secondary channels actually carry substance (newsletter, podcast feed, arXiv, conference talks).

## Cadence

How often they publish, and in what form. This feeds `SOURCES.md` and determines how often a refresh needs to check them. "Project-based, two or three substantial pieces a year, plus podcast appearances" is more useful than "regularly".

## Their work in my vault

<!-- Chronological by publication date, NOT by when you filed it. The sequence is the
     feature: it is how you see a position move. -->

- [[example-concept-note]] (2022-03-29) — one line on the specific finding, not the topic

Then a line connecting them to adjacent people and threads, so the graph closes:

> Adjacent: [[some-other-person]] is the direct counterparty on the central disagreement; [[some-thread]] is where the pattern across their work is tracked.

## Positions they have publicly revised

<!-- THIS IS THE SECTION THAT MAKES PERSON NOTES WORTH KEEPING, and it is the one
     nobody thinks to create.

     Following a field over months means watching people change their minds. Almost
     nobody records this, so the revision gets lost and you are left with a vague
     sense that someone's view "shifted". Written down with both sides and dates, it
     becomes the most valuable thing in the note — you can see WHAT changed, WHEN,
     and WHAT CAUSED it.

     Format each as: the claim, the two notes holding each side, the trigger. -->

- **[The claim]** — in [[earlier-note]] ([date]) they argued X. By [[later-note]] ([date]) they describe it as mostly wrong, and name the cause: [the specific evidence or event that moved them].
- **[A forecast still in flight]** — they predicted Y by [date]. Record it here so the vault can score it later. Forecasts that are never scored are the main way a knowledge base quietly stops being honest.

Also worth recording in this section when it applies:

- **Affiliation changes**, with the date and what it means for reading them. Someone who joins or leaves a lab, or founds an organisation, acquires interests. Note it when it happens rather than discovering it later.
- **Same-author tensions** — two pieces by the same person, weeks apart, that do not obviously reconcile. Leave them open. Resolving a tension that the author has not resolved is how you end up with a tidy, wrong note.
