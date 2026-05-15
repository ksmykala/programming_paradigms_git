# -*- coding: windows-1250 -*-
## Snippet 1
type: Imperative
because:  code uses a for loops and  total variable  its changing state step by step with no functions and this is typical imperative programming.

## Snippet 2
TRype: Procedural
because: logic is split into two functions get_total and  get_by_category. However, inside those functions we still use loops and conditionals. This is procedural decomposition.

## Snippet 3
type: Imperative with a functional touchh or 50/50
cause:: A loop builds a dictionary totals  which is imperative The max function with lambda is functional, but the main style is still imperative.

## Snippet 4
type: Functional
because:: Use sum with a generator, map, filter, and lambda. No explicit loops or mutable accumulators — data flows through higher‑order functions.