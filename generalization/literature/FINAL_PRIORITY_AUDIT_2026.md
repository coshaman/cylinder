# Final priority audit (2026-08-27)

## Verdict

**PARTIALLY_OVERLAPPING.**

The submitted package is not cleanly novel as a whole: the odd-width EOD family

\[
P_{2r+1}\square C_{4t}\quad(r,t\ge 1)
\]

is explicitly prior art. The audited literature does not contain the submitted
all-width characterization

\[
P_m\square C_n\text{ has an EOD set}
\iff
\bigl(m\text{ odd and }4\mid n\bigr)\text{ or }
\bigl(m\text{ even and }m+1\mid n\bigr),
\]

for all \(m\ge2,n\ge3\), nor an equivalent published exact family for all
\(k,t\ge1\),

\[
\gamma_t(P_{2k}\square C_{(2k+1)t})=k(k+1)t.
\]

Thus the correct priority description is: **the odd family is prior; the
general all-width EOD iff theorem and the unbounded even-width exact family
appear to be new within this audit, with direct/special-case overlap in small
widths.** This is not a claim of worldwide nonexistence of undiscovered prior
art.

## Frozen claims audited

The current artifacts supplied for this review state:

1. EOD iff \(m\) is odd with \(4\mid n\), or \(m\) is even with
   \(m+1\mid n\), for \(m\ge2,n\ge3\).
2. The lower bound is
   \(\lceil(m+1)n/4\rceil\) for odd \(m\), and
   \(\left\lceil m(m+2)n/[4(m+1)]\right\rceil\) for even \(m\).
3. The exact even family is
   \(\gamma_t(P_{2k}\square C_{(2k+1)t})=k(k+1)t\).
4. The odd family is known prior art.
5. Width-5, width-6, and width-7 formulas are certificate-backed.

The present report audits priority and attribution only. Certificates and
computer output are not treated as literature evidence or as proof of novelty.

## Terminology and search protocol

The search was run on 2026-08-26 using the path-cycle/cylinder forms
\(P_m\square C_n\) and \(C_n\square P_m\), together with:

- “efficient open domination”, “efficient open dominating set”, and “EOD”;
- “efficient total domination”, “efficiently total dominating set”, and “ET1D”;
- “total perfect code”, “total perfect dominating set”, and “exact transversal”;
- “cylinder”, “cylindrical grid”, “grid-like graph”, and “Cartesian product”;
- “total domination number”, \(\gamma_t\), and the even-family expressions.

The review used publisher/repository pages and accessible primary PDFs where
available. Search-index snippets, secondary summaries, and the project’s
development-history reports were not used as positive evidence of priority.

## Direct EOD evidence and attribution

### Kuziak–Peterin–González Yero (2014): direct prior art

Primary source: [Efficient open domination in graph products, DMTCS 16(1),
105–120 (2014)](https://dmtcs.episciences.org/1267/pdf), DOI
[10.46298/dmtcs.1267](https://doi.org/10.46298/dmtcs.1267).

The paper defines EOD using open neighborhoods whose intersections form a
partition, and records the equality \(\gamma_t(G)=|D|\) for an EOD set. In
Section 5.2 it states and constructs **Proposition 5.6**: every
\(P_{2r+1}\square C_{4t}\), \(r,t\ge1\), is an efficient open domination
graph. The displayed row/column construction is the source that must receive
credit for the odd family. The same paper’s **Theorem 5.7** gives the small
circumference cases

\[
\begin{array}{c|c}
\text{circumference} & \text{path widths admitting EOD}\ \hline
3 & 2\\
4 & \text{odd }m\\
5 & 4\\
6 & 2\\
7 & 6.
\end{array}
\]

These cases overlap the submitted general criterion at the listed small
parameters. They do **not** state the all-width iff criterion: the paper
itself describes its cylinder results as partial, and its theorem only treats
cycle orders \(3,4,5,6,7\), while Proposition 5.6 gives the odd-width
construction for multiples of four.

The article also identifies the relevant synonym chain: “total perfect code”,
“efficient open domination”, and “exact transversal” are used for the same
open-neighborhood exact-one condition in the grid literature. “Perfect code”
without “total” generally denotes the closed-neighborhood/independent variant
and must not be counted as equivalent EOD prior art.

### Foundational terminology

[Gavlas–Schultz, Efficient Open Domination (2002)](https://doi.org/10.1016/S1571-0653(04)00113-1)
introduces the efficient-open-domination terminology and general properties.
The accessible record does not provide a cylinder classification or the
submitted all-width theorem. It is terminology/background, not a source for
the odd-cylinder construction.

## Total-domination cylinder literature

### Hu–Xu (2014) and Hu–Sohn–Chen (2016)

[Hu–Xu, Total and paired domination numbers of toroidal
meshes (2014)](https://doi.org/10.1007/s10878-012-9519-2) concerns products of
two cycles, not \(P_m\square C_n\). It is not equivalent cylinder prior art.

[Hu–Sohn–Chen, Total and paired domination numbers of \(C_m\) bundles over a
cycle \(C_n\) (2016)](https://doi.org/10.1007/s10878-015-9885-7) treats cycle
bundles and includes exact cylinder results for the special circumferences
\(C_3\) and \(C_4\) (as also described in the later cylinder paper). This
overlaps special cases, not the all-width EOD criterion or the unbounded even
family.

### Eakawinrujee (2022): closest exact cylinder source

[Total and Paired Domination Numbers of Cylinders (2022)](https://doi.org/10.1007/s40840-022-01382-1)
defines \(\gamma_t(P_p\square C_q)\) for \(p\ge2,q\ge3\), gives exact
values for \(p\in\{2,3,4\}\) and \(q\ge5\), and gives bounds for other
width/circumference values. Its abstract therefore establishes substantial
scope overlap with the even-family subcases \(k=1\) and \(k=2\) (widths 2
and 4), but explicitly does not claim the all-\(p\) exact family. The
accessible record does not expose every displayed formula, so formula-level
matching for each residue class should be checked against the article PDF
before making a stronger priority statement about the \(k=1,2\) subfamilies.

The combination of the 2014 EOD small-case results and this 2022 exact
small-width paper means that the even-family claim must be described as a
generalization with small-width overlap, not as wholly disjoint prior art.

### Gravier (2002) and rectangular-grid sources

[Gravier, Total domination number of grid graphs (2002)](https://doi.org/10.1016/S0166-218X(01)00297-9)
uses Manhattan-metric tilings to derive asymptotic values for total domination
of path/cycle products and exact values for some cycle products. The accessible
primary abstract does not state the submitted lower bounds, all-width EOD
criterion, or the exact even family. Full-text comparison was unavailable in this
audit, so no priority claim about the lower-bound derivation is made.

[Crevals–Östergård, Total Domination of Grid Graphs (2017)](https://combinatorialpress.com/jcmcc-articles/volume-101/total-domination-of-grid-graphs/)
and its [publisher PDF](https://combinatorialpress.com/article/jcmcc/Volume%20101/vol-101-paper14.pdf)
concern \(P_m\square P_n\), not cylinders. It is not equivalent prior art for
the width-5/6/7 cylinder formulas.

## Current and neighboring terminology checks

- [Haynes–Hedetniemi–Henning, Domination in Graphs: Core Concepts
  (2023)](https://doi.org/10.1007/978-3-031-09496-5) contains a chapter on
  efficient domination and a section listed as total-efficient cylindrical
  graphs. The publicly accessible metadata/preview was insufficient to verify
  whether it states the submitted theorem; it is therefore a bibliography
  lead, not affirmative prior art.
- [Martínez–Castaño-Fernández–Puertas, The 2-domination number of cylindrical
  graphs (2024)](https://arxiv.org/abs/2409.16703) is a different invariant:
  vertices outside the set need at least two selected neighbors, and selected
  vertices do not satisfy the total-domination requirement. Its min-plus
  methodology does not create EOD or \(\gamma_t\) overlap.
- [Osborn–Zhang, From princes on chessboards to proper total domination in
  graphs (2026)](https://doi.org/10.61091/jcmcc129-03) studies proper total
  domination on cylinders, not minimum ordinary total domination or EOD.
- [Brezovnik–Zerovnik, [k]-Roman domination on cylindrical grids (2026)](https://arxiv.org/abs/2603.02831),
  [Further results (2026)](https://arxiv.org/abs/2603.25191), and [Upper bounds
  for double Roman and [k]-Roman domination (2026)](https://arxiv.org/abs/2604.12029)
  concern Roman-type functions, not ordinary EOD or \(\gamma_t\).
- [Wehrmann–Koster, Efficient total domination and related invariants in
  torus graphs (2026)](https://doi.org/10.1016/j.dam.2026.03.047) concerns
  \(C_m\square C_n\), and hence does not overlap the cylinder theorem. Its
  current existence confirms that “efficient total domination” is active
  terminology, but it is not cylinder prior art.

## Claim-by-claim priority classification

| Claim | Classification | Evidence and limitation |
|---|---|---|
| Odd EOD family \(P_{2r+1}\square C_{4t}\) | **PRIOR** | Explicitly Proposition 5.6 of Kuziak–Peterin–González Yero (2014). |
| All-width EOD iff theorem | **NOT FOUND; apparently new** | 2014 gives only the odd construction plus five fixed cycle orders; no audited source states the submitted iff for every \(m,n\). Negative conclusion is search-bounded. |
| Even EOD construction for arbitrary \(m=2k\), \(n=(2k+1)t\) | **NOT FOUND; apparently new with small-case overlap** | 2014 has the small cases \((m,n)=(2,3),(4,5),(6,7)\); no audited source gives the arbitrary-even-width construction. |
| Exact even family \(k(k+1)t\) | **PARTIAL OVERLAP** | Exact cylinder literature covers widths 2–4; the 2014 EOD paper covers small EOD instances. No audited source gives the family for every \(k\ge1\). |
| General lower bounds | **UNCERTAIN PRIORITY** | Gravier (2002) gives asymptotic path/cycle-product results; accessible material does not permit a formula-level comparison with the submitted dual bound. |
| Width 5/6/7 certificate-backed formulas | **NO EQUIVALENT CYLINDER FORMULA FOUND** | Audited exact cylinder source reaches widths 2–4; rectangular-grid formulas and computation are not equivalent evidence. |

## Limitations and required wording

This audit is a current, source-based priority search, not a proof of global
novelty. Several publisher pages were abstract-only or inaccessible, and the
2023 book chapter was available only through metadata/preview. Search indexing
is incomplete, notation varies, and a paper may use “total perfect code” or
“exact transversal” without using “EOD”. A database-by-database archival search,
including unrestricted full-text inspection of the 2022 cylinder paper and the
2023 monograph chapter, would be required for a stronger negative claim.

Recommended publication wording is therefore:

> The odd-width EOD family is known from Kuziak, Peterin, and González Yero
> (2014, Proposition 5.6). To the best of this source-bounded audit, the
> all-width EOD characterization and the arbitrary-even-width exact family do
> not appear in the prior literature; they generalize previously known small
> cylinder cases, while the width-5/6/7 formulas are not covered by the exact
> cylinder sources identified here.

No claim that the entire package is wholly novel is supported. Any substantive
revision of the priority or attribution statements requires a new literature
review.

## 2026-08-27 update

The current DAM record for Wehrmann--Koster is verified as Discrete Applied
Mathematics 389 (2026), 106--118, DOI 10.1016/j.dam.2026.03.047. It
characterizes efficient total k-domination for torus graphs C_m square C_n,
including the ET1D criterion that both cycle orders are divisible by 4. This
is relevant neighboring work, not equivalent cylindrical prior art.

The official Springer metadata for Haynes--Hedetniemi--Henning, Domination in
Graphs: Core Concepts (2023), confirms Chapter 9, Efficient Domination,
including Section 9.3.3, Total Efficient Cylindrical Graphs (the chapter is
listed at pp. 259--289 and the cylindrical subsection at p. 275). The
accessible chapter material was not sufficient for a line-by-line formula
comparison, so the cylindrical all-width claim remains UNCERTAIN_PRIORITY,
not affirmative prior art.

The repetitive-graph references were checked against publisher records:
Klavzar--Zerovnik, Discrete Applied Mathematics 68 (1996), 93--100, DOI
10.1016/0166-218X(95)00058-Y, and Bouznif--Moncel--Preissmann, Discrete
Applied Mathematics 208 (2016), 27--40, DOI 10.1016/j.dam.2016.03.009.
They establish general fasciagraph/rotagraph and min-plus methodology; they
do not state the present EOD or total-domination formulas.

The normalized principal-claim classifications are:

| Claim | Classification |
|---|---|
| Odd EOD family | **PRIOR** |
| All-width EOD iff theorem | **NOT_FOUND_IN_AUDIT** |
| Arbitrary-even-width EOD construction | **NOT_FOUND_IN_AUDIT** |
| Exact even-width total-domination family | **PARTIAL_OVERLAP** |
| General total-domination lower bound | **UNCERTAIN_PRIORITY** |
| Width-5/6/7 residual formulas | **NOT_FOUND_IN_AUDIT** |
| Generic repetitive-graph/min-plus machinery | **PRIOR** |
| Wehrmann--Koster torus theorem | **PRIOR, DISTINCT DOMAIN** |
