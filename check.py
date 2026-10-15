#!/usr/bin/env python3
"""
Vault integrity check. No dependencies, no config.

    python3 check.py            # check the vault in the current directory
    python3 check.py /path/to/vault

Run it at the end of onboarding, and before every commit. Dataview fails
silently on malformed frontmatter — a duplicate YAML key or a stray status
value does not raise an error, it just makes your reading queue quietly
wrong. This catches that.

Exit code 0 = clean, 1 = problems found.
"""

import collections
import os
import re
import sys

STATUSES = {"foreign", "understood", "fluent"}
CONTENT_TYPES = {"concept", "paper", "podcast", "repo"}


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else None


def field(fm, name):
    m = re.search(rf"^{name}:\s*(.*)$", fm, re.M)
    return m.group(1).strip() if m else None


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    problems = []
    counts = collections.Counter()

    md = []
    for sub in ("notes", "threads", "explorations"):
        d = os.path.join(root, sub)
        if os.path.isdir(d):
            md += [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]

    if not md:
        print(f"No notes found under {os.path.abspath(root)}/{{notes,threads,explorations}}.")
        print("If this is a fresh vault, that is expected — run /vault to seed it.")
        return 0

    stems = {os.path.splitext(os.path.basename(p))[0] for p in md}
    # example/ files are legitimate link targets too
    ex = os.path.join(root, "examples")
    for dirpath, _, files in os.walk(ex):
        stems |= {os.path.splitext(f)[0] for f in files if f.endswith(".md")}

    for path in md:
        rel = os.path.relpath(path, root)
        text = open(path, encoding="utf-8").read()
        fm = frontmatter(text)

        if fm is None:
            problems.append((rel, "no YAML frontmatter"))
            continue

        # duplicate keys silently corrupt Obsidian's parser
        keys = re.findall(r"^([A-Za-z_][\w-]*):", fm, re.M)
        for k, n in collections.Counter(keys).items():
            if n > 1:
                problems.append((rel, f"duplicate YAML key '{k}' ({n}x) — breaks Dataview"))

        ntype = field(fm, "type")
        status = field(fm, "status")
        counts[status] += 1

        if status is None:
            problems.append((rel, "no status field"))
        elif status not in STATUSES:
            problems.append((rel, f"status '{status}' is not one of {sorted(STATUSES)}"))
        elif ntype == "person" and status != "understood":
            problems.append((rel, f"person note has status '{status}' — must be 'understood'"))

        if ntype in CONTENT_TYPES and not field(fm, "published"):
            problems.append((rel, f"{ntype} note has no published: date"))

        if "{{date}}" in text:
            problems.append((rel, "unsubstituted {{date}} — replace with today's real date"))

        if status == "understood" and "## My take" in text:
            body = text.split("## My take", 1)[1].split("\n## ", 1)[0]
            if not re.sub(r"<!--.*?-->", "", body, flags=re.S).strip():
                problems.append((rel, "status is 'understood' but 'My take' is empty"))

        # broken wikilinks, ignoring anything inside backticks
        clean = re.sub(r"`[^`]*`", "", text)
        for m in re.finditer(r"\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]", clean):
            target = m.group(1).strip()
            if target and target not in stems:
                problems.append((rel, f"broken wikilink [[{target}]]"))

    print(f"{len(md)} notes checked in {os.path.abspath(root)}")
    if counts:
        print("  " + "  ".join(f"{s}: {n}" for s, n in sorted(counts.items(), key=lambda x: str(x[0]))))

    if not problems:
        print("\nClean.")
        return 0

    print(f"\n{len(problems)} problem(s):\n")
    by_file = collections.defaultdict(list)
    for f, p in problems:
        by_file[f].append(p)
    for f in sorted(by_file):
        print(f"  {f}")
        for p in by_file[f]:
            print(f"      {p}")
    print("\nBroken wikilinks to notes you have not written yet are expected and fine —")
    print("Obsidian resolves them when the target appears. The rest should be fixed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
