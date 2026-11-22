# Starter issues for State (copy each one into GitHub → Issues → New issue)

Ranked by points at stake, from the six qualifier scoresheets.

## 1. Run B — M11 Window to the Past only worked 2 of 6 times (20 pts)
Run B scores M06 and M07 every time, then misses the window most of the time.
The window part is the end of `run_b_fungus.py` (the `turn(110)` / `straight(255)` section).
Goal: window down 5 of 5 on the practice table.

## 2. Run 9 — M05 Reaching Roots: complete only 1 of 6 (20 pts) and M08 Tangled 4 of 6 (30 pts)
Roots were *partial* twice, *complete* once, and *missed* three times.
Goal: vine 5/5 and roots **completely** extended 5/5.

## 3. Run C — garden skylight 4 of 6, and up to +20 from the compost hatch
The environmental bonus goes to the feature that matches the dock the M15 model sits on
(Mine = nesting canopy, City = garden skylight, Farm = compost hatch).
At the qualifier M15 was on the **Farm** dock, M13 on City, and M14 (not attempted) on Mine.
Farm is in the center of the field, which we cross to reach the other launch area, so M15 stays there.
- Build a compost hatch solution: hatch opened, touching the mat = 10, plus the Farm bonus = 10.
- Add it to run C or a new run, and pass the Solved Rule.

## 4. Put Exploding Seeds (M02, up to 30 pts) on the menu
`run_seeds.py` is solved but not on the menu. Decide how it launches —
its own menu selection, or a new attachment color on selection 2 (instructions are in
the file) — and where it goes in the match order. Then time a full match
with it included.

Running out of colors? By default the sensor knows RED, YELLOW, GREEN, BLUE
and WHITE — **WHITE is still free**. More colors (like MAGENTA, or your own
measured ones) can be added with `color_sensor.detectable_colors(...)`, but
then re-test that every attachment still reads correctly. Or use a second
menu selection with the same colors.

## 5. Drive_to_Wall checks the LEFT motor twice (`robot.py`)
`abs(LeftMotor.load()) >= StopLoad and abs(LeftMotor.load()) >= StopLoad` —
the second one was probably meant to be `RightMotor`. `Drive_to_Wall_Timed`
(used by Exploding Seeds) already checks both. Fixing it changes when the
robot stops, so test run 9 carefully. (Could also be a
reason run 9 isn't consistent!)

## 6. Delete the old planned-sequence feature (`main.py`)
We stopped using it before the qualifier, but it's still in the code, and its
list still has the old selections 3, 4, 9. It's switched off
(`USE_PLANNED_SEQUENCE = False`), so nothing breaks today — but turning it on
would crash the menu. Deleting `USE_PLANNED_SEQUENCE`, `planned_sequence`,
`sequence_index` and the `"R"` branch makes `main.py` shorter and easier to
explain to judges. `tests/check.py` will show `SAME` if nothing else changed.

## 7. Time a full match
Run the whole match (A, B, C, 1, then 2 with every color, plus Exploding Seeds) with a stopwatch, including attachment swaps. How many seconds are
left out of 150? That decides whether we can add a new mission.

## 8. Points vs Effort — re-rate the missions we skipped
Untouched at the qualifier (Exploding Seeds is now solved!): M14 Seeds of Renewal (40),
M12 Forest Elder (30), M09 platform + seed (20), M01 LiDAR bonus (10),
M15 compost hatch (10). Only add one if it passes the Solved Rule
**without** hurting the runs we already have.
