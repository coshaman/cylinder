# Generalized theorem contract

This file is the frozen contract for the symbolic generalization. It is
separate from `mathematics/DEFINITIONS.md`, whose contract remains the
width-5/6/7 finite-certificate branch.

For integers m >= 2 and n >= 3, let G(m,n) be the Cartesian product of the
path P_m and cycle C_n. Open neighborhoods and total domination have their
usual graph meaning: selected vertices also require a selected adjacent
neighbor.

The generalized claims are:

- G(m,n) has an efficient open dominating set if and only if m is odd and
  4 divides n, or m is even and m+1 divides n;
- the total domination number is at least ceil((m+1)n/4) for odd m, and at
  least ceil(m(m+2)n/(4(m+1))) for even m;
- for every k,t >= 1, the total domination number of P_(2k) Cartesian
  product C_((2k+1)t) is k(k+1)t.

The proof dependencies are the row-system, odd-width characterization,
even-width divisibility and construction, total-domination lower bound, and
exact even-width family records in this directory. The odd family is credited
to Kuziak--Peterin--Gonzalez Yero (2014, Proposition 5.6) as prior art; this
contract does not claim that family as new.
