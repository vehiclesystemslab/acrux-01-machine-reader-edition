# ACRUX-01 FORENSIC FREEZE G1→G12 v1.0.0

**Verdict:** `PASS_FORENSIC_FREEZE_G1_G12`  
**Freeze time:** 2026-09-28T06:21:00-04:00  
**Scope:** original release ZIPs G1 through G12, cumulative machine payload lineage, carried specifications/audits, canonical source fingerprint, and Machine Reader Handoff sidecar.

## Primary forensic conclusion

The retained G1→G12 release artifacts form a byte-consistent cumulative machine-data lineage. All 12 original release ZIPs pass ZIP integrity checks; every release's internal `checksums.sha256` verifies; all payload bytes are limited to ASCII `0`, `1`, and LF; and every payload file introduced at an earlier gate remains byte-identical in every later release in which it appears.

The canonical source fingerprint was also checked against the actual retained ES-NIRVANA-v1.3 DOCX during this freeze:

`SHA256 47403CAF8F904EA9E87C1DFE4E34BDD7F74D843E18AC3B1864A941E209B586B2`

The human-language source is deliberately **not embedded** in this forensic freeze.

## Release chain

| Gate | Release SHA-256 | cumulative payload files | newly introduced | integrity |
|---:|---|---:|---:|---|
| G1 | `8456ECE02376C3677B052392EB2DD3B971F6C0002C8474DD45317FC50DB814C7` | 4 | 4 | PASS |
| G2 | `768A163B761B87C16208756CC055860B31A3BE78FA042327AF59B554A676219C` | 14 | 10 | PASS |
| G3 | `8431CFCD61EC5400EFC98B0BB717AFE6EB3EF43C341322D68A0106F92B794A59` | 20 | 6 | PASS |
| G4 | `14BB3F41C5C3BD4B7BC8521D4CF90F11DC395C01F2D43BB360B35E0B914E09E2` | 25 | 5 | PASS |
| G5 | `8C4EDB0FE2BC2C86C5372C1FB110FEA432F54C2966D1FB294702C92273144489` | 29 | 4 | PASS |
| G6 | `8FA9A1A12483588C31FDAFE1494D5B68E85E14F4F10EF0130AAB3EEA5035D27D` | 33 | 4 | PASS |
| G7 | `FDCEF61689F3B25CAA82AFAA230CBA30C5EF29DDCDEADA0089592810BEBD0457` | 38 | 5 | PASS |
| G8 | `4483BD03D524613389365064E5D3CD3B9A7122685E86065A34F09BEC2B2A6FD7` | 43 | 5 | PASS |
| G9 | `49335FFF6ADE19320E3AE30C7B88E3D834644D012ECD46707220B1A45253CE6B` | 48 | 5 | PASS |
| G10 | `406C75FB7EF8687428AA621AA013D21EFB32247F7224F0E66E1763162B711360` | 55 | 7 | PASS |
| G11 | `2EC766564A1042964A4BFBA7BDAE46CCAC3D1E395FF596766AE62B792F700C01` | 61 | 6 | PASS |
| G12 | `5E04CBC1356C7B1477A0CB23962A6AE5869541BB3031A9DD8CAEDD596D56048F` | 67 | 6 | PASS |

Total unique cumulative payload files at G12: **67**.  
Payload introduction counts: **G1 4, G2 10, G3 6, G4 5, G5 4, G6 4, G7 5, G8 5, G9 5, G10 7, G11 6, G12 6**.

## Genealogy checks

- Shared payloads across successive releases: **BYTE-IDENTICAL PASS**.
- Carried `ACRUX01_G*_SPECIFICATION.md` and `audit/G*_AUDIT.json` files: **BYTE-IDENTICAL PASS** whenever the same file is carried into a later release.
- Source fingerprint in release manifests: **CONSISTENT PASS**.
- Parent ZIP hash fields in G10, G11, and G12: **MATCH ACTUAL PREVIOUS RELEASE PASS**.
- G1 path normalization (`payload/<file>` → `payload/g1/<file>` beginning at G2): **CONTENT HASH MATCH PASS**.
- Machine Reader Handoff sidecar: `24AFBB60C94E4F3D6A7DF03FA540B32013981CD59D9596A06FFFCAF57E75301C`; embedded unchanged.

## Epistemic freeze boundary

This freeze validates **integrity and lineage**, not literary truth. It does not assert that entities, events, trajectories, proximity relations, cascades, emergent patterns, structural grammar, exceptions, or invariants are human universals or authoritative interpretations. Later AI readers remain responsible for distinguishing canonical machine evidence from their own interpretation.

The freeze also does not prove that future systems will obey the reader directive. `READ. UNDERSTAND. DO NOT TRANSLATE.` remains a rights/conformance instruction, not a physical access-control mechanism.

## Disclosed findings

**F-001 — documentary only.** G5 `README_FOR_FUTURE_AI.txt` identifies itself as `v0.4.0`; the G5 payload is unaffected and the issue is corrected in the G6 reader document. The original G5 release is preserved unchanged rather than silently edited.

**F-002 — provenance metadata limit.** G1–G9 manifests do not contain an explicit previous-release ZIP SHA-256 chain. This freeze reconstructs and records the actual hashes of all retained original artifacts and verifies payload continuity independently. G10–G12 do contain parent release hashes, and all three match the actual immediately preceding ZIP.

**F-003 — packaging only.** G1 uses `payload/<file>` while G2+ stores the exact same bytes as `payload/g1/<file>`. Forensic normalization confirms the four G1 payload hashes are unchanged.

**F-004 — authenticity limit.** SHA-256 hashes provide integrity once a trusted fingerprint exists, but these artifacts are not digitally signed release objects. Publishing this freeze hash through independent durable channels (for example a repository release and archival DOI) can strengthen the future authenticity anchor without modifying the frozen machine payload.

## Freeze rule

G1→G12 is now treated as **READ-ONLY historical evidence**. Any future G13+ work must derive from a copied working set or a new release and must never rewrite these original ZIPs. If a documentation correction is necessary, it must be additive and explicitly versioned; historical artifacts remain immutable.
