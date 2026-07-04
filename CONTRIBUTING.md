# Contributing to Collab Graph

Collab Graph maps **direct relationships between musicians and bands** — who was in which band, who made a track *with* whom, and who guested on whose record. The code is the easy part; the value is the data, and the data is only as good as the connections people like you add. Thank you for helping.

You do **not** need to know how to code to contribute. The fastest way in is the [Add a connection form](../../issues/new/choose) — it's a structured form, all you need is a free GitHub account.

---

## What counts as a connection

We map three relationship types, and only three (for now). The test for all of them: **did the two artists actually engage with each other?**

| Type | Meaning | Example |
|------|---------|---------|
| `member` | A person is (or was) a member of a band. | Maynard James Keenan → Tool |
| `collaboration` | Two or more artists **co-created** a track as co-equal authors (an "X & Y" credit, a joint single, a supergroup one-off). | Danger Mouse & CeeLo Green → Gnarls Barkley |
| `guest_performer` | An artist **performs on a track that is primarily someone else's** — their album, their song. | Maynard James Keenan → Deftones, on *Passenger* |

The line between `collaboration` and `guest_performer` is simply **whose work it is**: co-owned by both, or hosted by one with the other guesting.

### What we deliberately *don't* map (yet)

Covers, samples, remixes, and writing/production-only credits are real, but they're a different **kind** of link — they connect a performer to a *composition or recording*, not directly to another artist, and they usually mean one party *incorporated* another's work rather than the two collaborating. They're out of scope for now. Please don't submit them as connections; they'd need their own separate treatment.

### The one tricky case: a guest spot on a cover

If an artist guests on a **cover** — e.g. Maynard singing on The Flaming Lips' cover of a Beatles song — that guest performance is still a genuine `guest_performer` connection between **Maynard and The Flaming Lips**. Submit it, but tick the **"this is a cover"** box (it sets `isCover: true`). That keeps the real connection while letting viewers hide cover-based links if they want. Do **not** create a connection from the guest to the *original* artist (Maynard → The Beatles); that link doesn't exist here.

---

## The evidence rule (the important one)

**Every connection needs a `source` that proves the *credit* — not just that the song exists.**

A Spotify or Apple Music link shows a track is real. It does **not** show who performed on it. So a bare streaming link is *not* acceptable as your source. Instead, link to something that lists the credit:

- **MusicBrainz** — a recording or artist-relationship page (best; it's structured and sourced).
- **Apple Music credits** — Apple surfaces performer/writer credits in-app.
- **Official liner notes**, a label page, or a reputable database entry.

Streaming links are welcome *in addition* — they power the "play this song" buttons — but they go in the `spotify` / `apple` fields, not `source`. (CI will reject a streaming URL used as a source.)

---

## How to submit

**Option A — the form (recommended, no coding).**
Open [a new issue](../../issues/new/choose), choose **Add a connection**, fill it in, submit. A maintainer reviews it and adds it to the dataset.

**Option B — a pull request (if you're comfortable with Git).**
Edit `data.json` directly, add your artist(s) and connection object(s), and open a PR. Automated checks validate your entry against [`schema/data.schema.json`](schema/data.schema.json) before it can be merged.

---

## What happens after you submit

New connections start **unverified**. They still appear in the graph immediately — just dimmed — so the map grows without every entry waiting on a maintainer. A maintainer then checks your `source` and flips `verified: true`, at which point the connection renders at full strength.

Please **don't** set `verified: true` yourself in a PR; that field is for maintainers who've checked the evidence.

---

## Data conventions

- **IDs are permanent.** An artist `id` is a lowercase slug (`maynard`, `a-perfect-circle`). Once connections point at it, don't rename it. Add an alias instead.
- **Prefer MusicBrainz IDs.** If you can, include the artist's `mbid`. It's the one identifier that stays stable across renames and disambiguates two artists with the same name.
- **One connection per real relationship.** Don't add the same guest spot twice; check whether the artist and the connection already exist first.
- **Aliases help search.** If an act is widely known by an abbreviation ("RATM"), add it to `aliases`.

The full field-by-field contract lives in [`schema/data.schema.json`](schema/data.schema.json).

---

## Licensing

To keep the project genuinely open and reusable, code and data are licensed separately:

- **Code** — MIT (or the license in `LICENSE`).
- **Data** — released under a permissive open-data license (CC0 or CC BY-SA; see `DATA-LICENSE`).

By contributing, you agree your submission can be published under these terms. Note that MusicBrainz core data is CC0, which is why seeding and sourcing from it is clean.

---

## Be decent

Assume good faith, keep discussion about the music and the evidence, and remember a human reviews every submission. See `CODE_OF_CONDUCT.md`.
