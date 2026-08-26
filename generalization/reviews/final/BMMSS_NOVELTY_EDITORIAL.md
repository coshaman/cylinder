# BMMSS novelty/priority editorial review

**Review date:** 2026-08-26  
**Frozen manuscript reviewed:** [`paper/manuscript.tex`](../../../paper/manuscript.tex)  
**Scope:** novelty and priority only; no source files were edited. The review uses only the authorized project and the primary/official sources listed below. Repository development-history reports and neighboring projects were not used as evidence.

## Verdict

**PASS WITH CAVEATS — novelty/priority gate only.**

The source check found no reviewed publication or public source that states the
complete ordinary-total-domination formulas for all (n\ge3) at each of
(P_5\square C_n), (P_6\square C_n), and (P_7\square C_n). The bounded
claim in the manuscript—“complete classifications ... in the audited record”
([`manuscript.tex:101–120`](../../../paper/manuscript.tex#L101-L120))—is
therefore defensible on the reviewed evidence.

This is not a finding that the formulas are globally novel, nor an acceptance
of the mathematical proof. The manuscript contains substantial direct overlap:
the odd-width (C_{4t}) EOD family and the exact (C_3,C_4) cylinder values
are prior results. The BMMSS submission should make the new/old boundary more
explicit and reconcile its bibliography before an editorial novelty clearance.

## Frozen contribution and dependency graph

The novelty-relevant dependency graph is:

```text
definitions of total domination/EOD
        │
        ├─ prior: P_{2r+1} □ C_{4t} EOD family
        ├─ prior: P_p □ C_3 and P_p □ C_4 total-domination values
        └─ prior: exact odd-width subfamily γ_t(P_p □ C_q)=(p+1)q/4
                │
                ▼
submitted all-width EOD criterion
                │
                ├─ submitted even-width criterion and even-width equality family
                └─ submitted finite-state/min-plus certificates
                        │
                        ▼
                complete formulas for widths 5, 6, and 7
```

Classification of the links:

| Manuscript item | Classification | Referee assessment |
|---|---|---|
| Definition of ordinary total domination and EOD | justified/cited | The definitions and terminology are consistent with the reviewed EOD and cylinder sources. |
| Odd-width EOD sufficiency and the (4\mid n) family | cited, not new on its face | Kuziak–Peterin–González Yero, Proposition 5.6, already gives (P_{2r+1}\square C_{4t}). |
| (C_3,C_4) total-domination values for all path widths | cited, not new | Hu–Sohn–Chen is the prior source identified in the official dissertation’s cylinder chapter. |
| Even-width EOD “iff” direction for arbitrary width | plausible new contribution, priority not established globally | No reviewed source states this exact cylinder criterion. The claim must remain date-bounded. |
| Even-width family (\(\gamma_t(P_{2k}\square C_{(2k+1)t})=k(k+1)t\)) | plausible new contribution, with close partial overlap | Eakawinrujee’s public dissertation contains related upper-bound constructions for \(P_6\square C_q\) and the odd-width exact family, but not the reviewed all-\((k,t)\) equality statement. |
| Width-five/seven values for (n\equiv0\pmod4) | cited, not new on its face | They specialize the prior odd-width exact family. |
| Width-five/seven remaining residues and exceptions | plausible new contribution, priority not established globally | The reviewed sources give bounds or subfamilies, not the complete submitted formulas. |
| Width-six complete residue correction and (n=12) exception | plausible new contribution, priority not established globally | The dissertation gives close (P_6\square C_q) upper bounds, including the (q\equiv0\pmod7) construction, but the reviewed text does not state the submitted exact all-(q) formula. |
| Finite-state/min-plus certificate protocol | methodologically overlapping, not shown new | Min-plus/tropical finite-state methods are already used for cylindrical domination variants; the manuscript appropriately avoids claiming that the architecture is generally new. |

## Source-based overlap audit

### Direct or material overlaps

1. **Odd-width EOD family.** The official DMTCS article states
   (P_{2r+1}\square C_{4t}) is an efficient open domination graph for all
   (r,t\ge1) (Proposition 5.6, pp. 117–118). This directly covers the odd
   branch of the submitted EOD theorem and the (n\equiv0\pmod4) EOD
   constructions at widths 5 and 7. The manuscript does acknowledge this at
   [`manuscript.tex:105–115`](../../../paper/manuscript.tex#L105-L115), but
   the abstract and contribution table should identify the odd branch as an
   extension/repackaging rather than an unqualified new result.

2. **Small circumferences.** The official Thammasat dissertation records that
   Hu et al. determined \(\gamma_t(P_p\square C_3)\) and
   \(\gamma_t(P_p\square C_4)\) for every \(p\ge2\), with explicit formulas in
   Theorems 3.3.8–3.3.9. Therefore the submitted values at
   ((m,n)=(5,3),(5,4),(6,3),(6,4),(7,3),(7,4)) are prior, not new. The
   manuscript says so at [`manuscript.tex:209–223`](../../../paper/manuscript.tex#L209-L223), which is appropriate.

3. **Odd-width exact total domination.** The official dissertation’s Lemma
   3.3.16 states that if (p) is odd and (q\equiv0\pmod4), then
   \(\gamma_t(P_p\square C_q)=\gamma_{pr}(P_p\square C_q)=(p+1)q/4\).
   This is an infinite direct overlap with the submitted width-five and
   width-seven formulas. The manuscript cites and describes it, but this
   overlap should be elevated from background prose to an explicit “prior
   cases / new cases” comparison.

4. **Same-venue predecessor.** Eakawinrujee’s 2022 BMMSS article already
   computes exact total and paired domination numbers for cylinders with
   (p\in\{2,3,4\}), (q\ge5), and gives bounds for other (p,q). Because
   the target submission is also framed for BMMSS, the introduction should
   state plainly that it continues the cylinder program from widths 2–4 and
   completes selected widths 5–7, while retaining the earlier residue and
   small-(q) results.

### Close but non-preemptive sources

5. **Rectangular width-five/six results.** Klobučar’s primary paper determines
   total domination for (P_5\square P_n) and (P_6\square P_n), and the
   Kuziak–Peterin–Yero erratum corrects the (P_6\square P_n) statement.
   These are not cylinders, so they do not preempt the submitted claims, but
   they are close fixed-width precedents and should be cited or explicitly
   distinguished alongside Crevals–Ostergård. The omission is a literature
   completeness issue, not evidence of mathematical non-novelty.

6. **Ordinary domination and 2-domination.** Nandi–Parui–Adhikari study
   ordinary domination on (P_m\square C_n), including bounds at width 5;
   Garzón–Martínez–Moreno–Puertas and Martínez–Castaño-Fernández–Puertas use
   min-plus/tropical methods for 2-domination on cylinders. These are genuine
   graph-family or methodological overlaps, but their parameters differ:
   2-domination requires two selected neighbors for vertices outside the set,
   whereas ordinary total domination requires one open neighbor for every
   vertex, including selected vertices. The manuscript’s separation at
   [`manuscript.tex:122–131`](../../../paper/manuscript.tex#L122-L131) is
   substantively correct.

## Findings and severity

### Major — novelty boundary must be stated as a decomposition

The manuscript’s bounded wording is good, but its “main structural theorem” and
“new exact family” labels do not visibly separate the already published odd
branch and already known residue subfamilies from the proposed even branch and
remaining residues. A referee could read the abstract as claiming the complete
EOD theorem and all width-five/seven formulas as wholly new.

**Why it matters:** the direct overlaps are infinite, not isolated examples.

**Suggested repair:** present a two-column prior/new comparison: (i) prior odd
(C_{4t}) EOD and total-domination cases; (ii) the even-width criterion,
remaining circumference residues, width-six correction, exceptions, and the
certificate-backed completion. Keep the “in the audited record” qualifier.

### Major — absence claims require a reproducible search boundary

The reviewed sources support “no equivalent source found in this review,” not a
universal negative. The manuscript’s phrase “in the audited record” is suitably
bounded, but the paper does not state the databases, exact search strings,
cutoff date, or how citation trails were followed.

**Suggested repair:** add a short, dated novelty-search note or supplement and
avoid “first,” “unprecedented,” or “no one has solved” unless a later human
review establishes that stronger claim.

### Major editorial — bibliography and citation artifacts are inconsistent

The body cites `KuziakPeterinYero2014` at [`manuscript.tex:138–139`](../../../paper/manuscript.tex#L138-L139), and the embedded bibliography contains it at lines 807–810, but `paper/references.bib` omits that key. Conversely, the `.bib` contains entries not cited in the embedded bibliography. The body also calls the 2-domination paper “2021,” while the cited journal version is 2022 (the arXiv submission is 2021).

**Why it matters:** a BMMSS submission must have a stable, complete, relevant
reference list; the venue’s guidelines require cited published/accepted works,
DOIs where available, and transparency for expansion of prior work.

**Suggested repair:** reconcile the source bibliography with the actual LaTeX
build, add the close rectangular-grid paper and erratum, normalize publication
years, and cite the dissertation’s exact lemma/theorem where the overlap is
used.

### Minor — priority of the certificate protocol is not demonstrated

The finite-state/min-plus approach is useful and the manuscript correctly says
the transfer architecture is not claimed new. The stronger phrase “clean-room
certificate protocol” should be presented as a reproducibility feature unless a
separate literature comparison establishes methodological priority.

### No issue found — parameter separation

The manuscript does not conflate total domination with ordinary, paired, proper
total, or 2-domination in the cited discussion. The toroidal (C_n\square C_5)
result is also explicitly distinguished from (P_5\square C_n), which is
necessary and correct.

## BMMSS editorial relevance

The official BMMSS submission guidance states that submissions should be
original, should cite relevant literature, and may be an expansion of earlier
work only with transparency. On the reviewed record, the paper can meet that
standard only with the bounded contribution framing above. The same-venue
Eakawinrujee article makes a direct comparison especially important; it is not
itself a disqualification, but it raises the burden to demonstrate the exact
increment beyond widths 2–4 and the previously known residue families.

## Recommended bounded wording (repair suggestions, not part of the verdict)

> “We extend the known cylinder results by proving the even-width branch of an
> all-width EOD criterion and by determining \(\gamma_t(P_m\square C_n)\) for
> every (n\ge3) at (m=5,6,7), including the circumference residues and
> finite exceptions not covered by the previously known (C_3,C_4) cases and
> the odd-width (4\mid n) family. To the best of the sources reviewed through
> 26 August 2026, we found no publicly documented equivalent complete
> all-circumference determination for all three target widths.”

This wording should be reconsidered after any substantive revision; a new
novelty review is required after such a repair.

## Primary and official sources checked

- [Kuziak, Peterin & González Yero, *Efficient open domination in graph products*, DMTCS 16 (2014), DOI and official full text](https://dmtcs.episciences.org/1267/pdf) — definition/terminology, Proposition 5.6, Theorem 5.7.
- [Eakawinrujee, *Total and Paired Domination Numbers of Cylinders*, BMMSS 45 (2022), official Springer page](https://link.springer.com/article/10.1007/s40840-022-01382-1) — exact (p=2,3,4), (q\ge5), and bounds for other parameters.
- [Eakawinrujee, official Thammasat University dissertation PDF (2023)](https://ethesisarchive.library.tu.ac.th/thesis/2023/TU_2023_6109320413_17206_27705.pdf) — cylinder Theorems 3.3.8–3.3.9, Lemma 3.3.16, and the width-five/six bounds in Lemmas 3.3.13–3.3.15.
- [Hu, Sohn & Chen, *Total and paired domination numbers of (C_m) bundles over a cycle (C_n)*, Springer](https://link.springer.com/article/10.1007/s10878-015-9885-7) — total-domination scope and related bundle/toroidal results.
- [Klobučar, *Total domination numbers of Cartesian products*, official Mathematical Communications PDF](https://hrcak.srce.hr/file/1426) and [Kuziak, Peterin & Yero, official erratum](https://hrcak.srce.hr/121838) — close rectangular (P_5,P_6) precedents and correction.
- [Garzón, Martínez, Moreno & Puertas, arXiv/journal record](https://arxiv.org/abs/2109.10549) and [Martínez, Castaño-Fernández & Puertas, arXiv record](https://arxiv.org/abs/2409.16703) — 2-domination and min-plus/tropical methodological neighbors.
- [BMMSS official submission guidelines](https://link.springer.com/journal/40840/submission-guidelines) — originality, expansion transparency, and relevant-literature requirements.

## Review boundary

No Lean artifact was present in the authorized project, so no Lean build
acceptance was claimed. The computational certificates were not treated as
evidence of publication priority; computation can support the mathematical
claims but cannot establish novelty by itself.
