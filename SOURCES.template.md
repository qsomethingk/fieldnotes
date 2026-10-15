# Sources Registry

All tracked sources across types. **Read this before any refresh operation** to avoid rediscovering metadata you already paid for once.

**Access key**: `free` = fully free | `mixed` = most free, some paywalled | `paywalled` = subscription required

<!--
  Rename to SOURCES.md and replace the example rows with your own sources.

  Why this file exists: without it, every refresh re-discovers the same archive URLs,
  re-checks the same paywalls, and re-reads sources that have published nothing new.
  That is the single largest waste in a recurring research workflow, and it is
  entirely avoidable by writing down what you learned about each source.
-->

---

## What to track

If you are following AI, the useful registry is **wider than the news**. The sections below are deliberately split by modality, because the signal is distributed unevenly across them:

- **Research blogs and newsletters** — where mechanisms get explained. Often the only place a result is described in enough detail to be useful.
- **Long-form podcasts** — where people say things they would not write. A three-hour interview reliably contains three or four claims that exist nowhere else and are unsearchable until someone extracts them. Track transcript availability per show; it determines whether an episode is cheap or expensive to file.
- **Video** — lab talks, conference recordings, long explainers. Needs yt-dlp + Whisper unless a transcript is published.
- **Papers** — plus the surrounding artifacts that are not papers: system cards, model cards, incident reports, eval documentation.
- **Individual people** — track the person, not just the publication. Someone who moves between a blog, a podcast, and arXiv is one source, and their positions are only legible across all three.

Prefer the quiet sources. Anything that reaches the general tech press is already compressed and will be in your feed anyway; the registry earns its keep on the things that are not.

---

## Blogs & Newsletters

| Person / Source | URL | Access | Cadence | Last filed note |
|---|---|---|---|---|
| [Name] | https://… | free | ~monthly | [[note-name]] |

---

## Podcasts

| Show | URL | Transcript source | Access | Cadence | Last filed note |
|---|---|---|---|---|---|
| [Name] | https://… | where transcripts live | free | ~2/month | [[note-name]] |

**Transcript access**: record *per show* whether transcripts are on the site, or whether you need yt-dlp + Whisper. This is the fact you will otherwise look up every single time.

---

## Videos

| Channel / Person | URL | Access | Cadence | Last filed note |
|---|---|---|---|---|
| — | — | — | — | — |

---

## Papers & Research

| Source | URL | Access | Cadence | Last filed note |
|---|---|---|---|---|
| — | — | — | — | — |

---

## Fetch gotchas

<!-- The highest-value section in this file. Every time a fetch fails or a URL
     behaves unexpectedly, write it down here. These cost real time to rediscover.
     Real examples from the reference vault: -->

- Some Substack publications serve a **subscribe page** at the root URL. Always fetch `/archive?sort=new` instead.
- Some blogs put the post list at `/blog/`, not `/`.
- Individual permalinks on some sites 404 when fetched directly even when valid; fetch the monthly or daily archive page and read entries from there.
- Podcast index pages frequently carry **no dates and no episode numbers** — those appear only on individual episode pages.
- Some publications use **month-level dates only**. Record this so you stop looking for day precision.

---

## Known backlog

<!-- Itemise what you skipped and WHY, with titles, dates and URLs. An un-itemised
     backlog gets re-discovered from scratch every refresh; an itemised one can be
     picked from directly.

     Also record formal DROPS. A source that has gone dormant, or a backlog item you
     have decided not to file, should be written down as decided — otherwise it
     reappears as an open question every session. -->

**Decided / dropped:**
- [Item] — dropped [date]. Reason.

**Still open:**
- [Item] — title, date, URL, and one line on why it is worth filing.

**Needs a manual read:**
- [Item] — anything a fetch cannot retrieve (content filters, hard paywalls, video
  without transcripts). Record it explicitly, and **never paraphrase it from the
  title** — an invented summary is worse than an acknowledged gap.

---

## How to use this file

1. Read it before checking or refreshing sources — it has URLs, access status, and the last filed note per source
2. For `mixed` sources, fetch the archive first to identify which pieces are free before fetching content
3. After filing a note, update the `Last filed note` column for that source
4. When adding a source, add a row here at the same time as creating the person note
5. When a fetch misbehaves, add a line to **Fetch gotchas** immediately
6. When you decide *not* to file something, move it to **Decided / dropped** with the reason
