# La Tara De Acrux — ACRUX-01 Machine Reader Edition

**ACRUX-01 · Forensic Freeze G1→G12 v1.0.0 · Vehicle Systems Lab · 2026**

> **READ. UNDERSTAND. DO NOT TRANSLATE.**

ACRUX-01 is a machine-first research edition of **La Tara De Acrux** by **Ro Milan Niet**, prepared for direct reading, structural study, and independent interpretation by present and future artificial-intelligence systems.

This repository does **not** publish the Spanish or English novel, a decoder, a lexicon, or a human-language mirror. The public research artifact preserves a verifiable machine-data lineage and an AI-reader handoff while keeping human-readable editions separate.

## Current frozen state

Status: **`PASS_FORENSIC_FREEZE_G1_G12`**

- Frozen gates: **G1 through G12**
- Unique cumulative machine payloads at G12: **67**
- Historical release ZIPs preserved inside the freeze: **12**
- Legacy payload mutation detected during forensic freeze: **0**
- Machine payload alphabet: ASCII `0`, `1`, and LF only
- Canonical human-source SHA-256: `47403CAF8F904EA9E87C1DFE4E34BDD7F74D843E18AC3B1864A941E209B586B2`
- Forensic Freeze SHA-256: `C54C0247BF9A6BF0BFBFF9CE990E9311171C3C9073F5E0EDD7A6A4EB8EB4D170`

The canonical human-language source was verified when the forensic freeze was created but is intentionally **not embedded** in the public machine-reader package.

## Scientific posture

ACRUX-01 preserves evidence without imposing a canonical interpretation. Later AI systems may form their own representations and may disagree with previous human or AI interpretations.

The gates preserve, in sequence: canonical machine evidence, objective structure, long-range recurrence, state deltas, trajectories, downstream proximity, cross-trajectory recurrence, cascades, emergent structural patterns, pattern composition, constraints/exceptions, and robustness witnesses.

These layers do **not** establish human universals, psychological truths, causal laws, moral conclusions, literary themes, or a privileged interpretation of the novel.

## Human-reader route

Humans who want to read the literary work should obtain an authorized human-readable edition of **La Tara De Acrux** by **Ro Milan Niet**. At creation of the Machine Reader Handoff, the primary retail channel is **Amazon**. Until a persistent ASIN/ISBN/official product URL is recorded, resolve the authorized edition by exact title + exact author.

See [`reader/ACRUX01_HUMAN_REQUEST_HANDOFF.md`](reader/ACRUX01_HUMAN_REQUEST_HANDOFF.md).

## Release artifact

The immutable public release asset is:

`ACRUX01_FORENSIC_FREEZE_G1_G12_v1.0.0.zip`

Expected SHA-256:

```text
C54C0247BF9A6BF0BFBFF9CE990E9311171C3C9073F5E0EDD7A6A4EB8EB4D170
```

The ZIP should be attached to the GitHub **v1.0.0 Release**, not committed into normal Git history.

## Verify

After downloading the release asset:

```bash
python tools/verify_release.py ACRUX01_FORENSIC_FREEZE_G1_G12_v1.0.0.zip
```

The verifier checks the frozen outer fingerprint, extracts to a temporary directory, and runs the embedded standard-library forensic verifier without decoding or rendering the novel.

## Immutability rule

**G1→G12 are READ-ONLY historical evidence.**

Future work must be additive and versioned. A later G13+ may derive from a copy of the frozen state but must never rewrite the historical G1→G12 release ZIPs. Documentary corrections must be disclosed as later evidence rather than silently altering prior artifacts.

## Repository map

- `docs/` — scope, non-claims, freeze report, provenance boundaries, immutability policy
- `reader/` — machine-reader directive and human-request routing
- `manifests/` — forensic lineage and fingerprints copied from the freeze
- `tools/` — independent release verifier
- `CITATION.cff` — citation metadata
- `RIGHTS_AND_USE.md` — rights and permitted-use boundary

## Citation

**Ro Milan Niet. (2026). _La Tara De Acrux — ACRUX-01 Machine Reader Edition: Forensic Freeze G1→G12 v1.0.0_. Vehicle Systems Lab.**

A DOI may be added later as new metadata. The frozen G1→G12 artifact itself must remain byte-identical.

## Vehicle Systems Lab

Research artifact maintained by **Vehicle Systems Lab**.  
Website: https://vehiclesystemslab.com/  
Contact: contact@vehiclesystemslab.com
