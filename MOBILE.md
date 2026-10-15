# Running the vault on a phone

Optional. The vault is a git repo, so a second clone on a phone works — and the division of labour is a happy accident: a phone cannot run a coding agent, but it is well suited to the thing a vault is always behind on, which is reading.

Written for **Android**, which has noticeably better git support in Obsidian than iOS. iOS notes at the bottom.

## The one rule

**On the phone, only ever edit `notes/`.**

Never `threads/`, `CONTEXT.md`, or `SOURCES.md`. A refresh rewrites those files **wholesale**, so a phone edit to one of them collides with the next refresh, and resolving a merge conflict in Obsidian mobile is genuinely miserable.

Which fits what a phone is good for anyway: read the queue, open a `foreign` note, write a "My take", flip it to `understood`.

## Setup

### 1. A scoped token

Obsidian's git plugin runs on isomorphic-git, which **has no SSH support** — it needs HTTPS with a Personal Access Token. So the phone clone uses a different remote URL than your desktop clone. Same repo, two clones, no conflict.

On GitHub → Settings → Developer settings → **Fine-grained** personal access tokens → Generate new:

- Repository access: **Only select repositories** → your vault repo
- Permissions → Repository permissions → **Contents: Read and write**. Nothing else.
- Expiry: 90 days. Set one.

**Scope it to the single repo.** The token will live in plaintext on a device you carry around and could lose, and its app storage is not protected the way a laptop keychain is. Scoped to one repo, a lost phone means someone can read and rewrite one vault, recoverable from your desktop clone. Scoped to all repos, it means write access to everything on your account.

### 2. On the phone

1. Install Obsidian from the Play Store
2. Create a **new empty vault**. Do not put it in a Drive- or Dropbox-synced folder — git and continuous file sync corrupt each other
3. Settings → Community plugins → enable → Browse → install **Git** (by Vinzent) → Enable
4. In the plugin's settings, under authentication, set your GitHub username and paste the token
5. Under **Commit Author**, set author name and email. These are separate fields from the auth credentials and are not inherited from anywhere — the plugin will refuse to commit without them. Use the same identity as your desktop commits so the history stays single-authored
6. Command palette → **`Git: Clone an existing remote repo`**
7. Paste the **HTTPS** URL, not SSH: `https://github.com/you/your-vault.git`
8. When asked for clone depth, use **1**. You do not need the full history on a phone, and it skips most of the download
9. Restart Obsidian, then install **Dataview** so `READING-QUEUE.md` renders

The clone may look like it has hung — isomorphic-git is doing the work in JavaScript. For a small vault it is seconds to a minute.

### 3. The credential trap

**This is the thing to get right.** The git plugin stores your token in:

```
.obsidian/plugins/obsidian-git/data.json
```

`.obsidian/` is a tracked directory in this repo. So without protection, your **first commit from the phone pushes your access token to GitHub.**

The shipped `.gitignore` already covers it:

```
.obsidian/plugins/*/data.json
```

Before your first phone commit, open the plugin's source-control view and confirm `data.json` is **not** in the changed-files list. If it is, stop — your `.gitignore` is not current on the phone. Pull first.

If a token ever does leak: revoke it at GitHub → Settings → Developer settings → Fine-grained tokens. That cuts access instantly without touching your desktop SSH setup, which is the other quiet benefit of keeping the two clones on different credentials.

## Recommended plugin settings

Labels drift between plugin versions, so these are by intent:

| Setting | Value | Why |
|---|---|---|
| Pull on startup | **on** | You always open to current state. This is the setting that prevents conflicts |
| Push on commit-and-sync | **on** | Edits do not sit stranded on the phone |
| Auto commit-and-sync interval | **off, or ≥30 min** | See below |
| Commit message template | `mobile: reading progress {{date}}` | See below |

That last pair matters more than it looks. Default auto-commit produces a stream of `vault backup: <timestamp>` commits, which buries a hand-written history. The log is your vault's changelog — it is how you reconstruct what you learned when — so setting the message template keeps mobile commits legible and visibly distinct from refresh commits.

## The rhythm

| When | Do |
|---|---|
| Opening the phone | Nothing — `Pull on startup` handles it |
| Done editing on the phone | `Git: Commit-and-sync` |
| Before a desktop session | `git pull` — **especially before a refresh** |
| After a desktop session | The agent commits and pushes; see the slash command |

The one that actually prevents problems is **pull before a refresh**. A refresh rewrites `threads/` and `CONTEXT.md` wholesale, so it needs to start from the phone's latest state rather than discovering it afterwards. The shipped slash command does this in Step 0c.

## If a conflict happens anyway

Do not try to resolve a merge in Obsidian mobile. Note what you typed, let the remote win (`Git: Discard all changes` on the phone), pull, and retype. It is almost always a sentence or two.

## iOS

Obsidian's git plugin works on iOS but is flakier. The more reliable route is **Working Copy** — a real git client with proper SSH support — cloning the repo there and opening the folder in Obsidian through the file provider. It is a paid app for push access, and the UX is clunkier, but it does not fight you.

Alternatively, Obsidian's own paid Sync service handles device-to-device properly and you keep git on the desktop only. That costs money and means running two sync systems, but it is the lowest-friction option if you do not mind either.
