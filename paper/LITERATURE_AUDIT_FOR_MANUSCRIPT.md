# Literature Audit for Manuscript

Audit date: 2026-08-26.

## Scope

The audit covered total domination on Cartesian products of paths and cycles,
with explicit searches for (P_m\square C_n), widths 5, 6, and 7, and recent
related domination variants. The invariant was kept distinct from ordinary,
paired, proper-total, Roman, locating-total, and 2-domination.

## Relevant exact-cylinder prior art

Eakawinrujee, *Total and paired domination numbers of cylinders*, Bull.
Malays. Math. Sci. Soc. 45 (2022), 3321--3334, DOI
10.1007/s40840-022-01382-1, determines exact values for path widths
(p\in\{2,3,4\}) for (q\ge5), and gives bounds for other parameters. It
does not provide the target complete classifications for widths 5--7.

Hu, Sohn, and Chen, *Total and paired domination numbers of C_m bundles
over a cycle C_n*, J. Combin. Optim. 32 (2016), 608--625, DOI
10.1007/s10878-015-9885-7, covers earlier small-width overlap and reports
the exact value for C_n square C_5. The small circumference values
(m,n)=(5,3),(5,4),(6,3),(6,4),(7,3),(7,4) are respectively 5, 6, 6, 8, 6,
8; these are contextual overlap, not claimed as new.

Eakawinrujee's 2023 Thammasat dissertation is also recorded as public prior
art for the cylinder program. It is cited for provenance and context; the
present manuscript does not claim that its broader dissertation results are
rederived here.

Hu and Xu, *Total and paired domination numbers of toroidal meshes*, J.
Comb. Optim. 27 (2014), 76--88, DOI 10.1007/s10878-012-9519-2, concerns
products of cycles and is contextual rather than an equivalent cylinder result.

## Foundational and contrasting sources

Gravier, *Total domination number of grid graphs*, Discrete Appl. Math. 121
(2002), 119--128, DOI 10.1016/S0166-218X(01)00297-9, is foundational for
total domination in grid-like Cartesian products, but the audited metadata and
abstract do not state the three target all-(n) cylinder formulas.

Crevals and Ostergard, *Total Domination of Grid Graphs*, J. Combin. Math.
Combin. Comput. 101 (2017), 175--192, gives fixed-width rectangular results
for (P_m\square P_n), not cylindrical (P_m\square C_n) results.

Nandi, Parui, and Adhikari, *The domination numbers of cylindrical grid
graphs*, Appl. Math. Comput. 217 (2011), 4879--4889, DOI
10.1016/j.amc.2010.11.019, concerns ordinary domination, not total domination.

## Recent variant separation

Martinez, Castano-Fernandez, and Puertas, *The 2-domination number of
cylindrical graphs*, arXiv:2409.16703, DOI 10.48550/arXiv.2409.16703,
uses min-plus methods for 2-domination, a different invariant.

The methodological overlap with that paper is explicit: both use finite
state/cyclic encodings and tropical matrix products. The mathematical
distinction is equally explicit: 2-domination requires two selected
neighbors for vertices outside the set, whereas ordinary total domination
requires one open neighbor for every vertex, including selected vertices.

Osborn and Zhang, *From princes on chessboards to proper total domination in
graphs*, J. Combin. Math. Combin. Comput. 129 (2026), 33--48, DOI
10.61091/jcmcc129-03, studies proper total domination, not minimum ordinary
total domination.

Brezovnik and Zerovnik, *[k]-Roman domination on cylindrical grids
(C_m\square P_n)*, arXiv:2603.02831, is Roman-type domination and does not
resolve the target invariant.

## Priority conclusion

No audited published or public source contains an equivalent exact all-(n)
classification for all three target families (P_5 square C_n), (P_6 square
C_n), and (P_7 square C_n) using the present theorem package. The manuscript
therefore uses the narrow claim that it determines these three widths,
explicitly acknowledges the Hu--Sohn--Chen and Eakawinrujee overlap, and does
not claim to settle cylindrical total domination at arbitrary width.
