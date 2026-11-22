---
layout: page
title: Code
permalink: /code/
---

All of our code is on GitHub:
**[github.com/thecats-fll-71447/bioglow](https://github.com/thecats-fll-71447/bioglow)**

We write Cat-Bot's programs in **Python** using **Pybricks**.

## One menu for the whole match
Cat-Bot runs **one program** that shows a menu on the hub. From the blue home
area we run **A**, **B**, and **C**. From the red home area we run **1**, and
then **2** for everything else. After each run the menu remembers where we
are, so the next run is ready to go. We just press the center button.

## One file per run
Each launch has its own file (`run_b_fungus.py`, `run_9_vine_roots.py`, …).
That way five people can work on five different runs at the same time
without getting in each other's way.

## Color sensor = the right code, every time
Menu selection **2** works for four different attachments. Cat-Bot looks at the
colored brick on the attachment and picks the code:

```python
if colorSensor.color() == Color.RED:
    run_3_rock.run()           # flip the rock
if colorSensor.color() == Color.BLUE or colorSensor.color() == Color.YELLOW:
    run_4_leaves.run()         # check, then grab the leaves
if colorSensor.color() == Color.GREEN:
    run_9_vine_roots.run()     # vine + roots
```

Fewer menu selections to remember means fewer mistakes at the table.

## Helpers we wrote
- **`DriveToWall`** — drive until the wheels feel the wall push back, then
  stop. Lines the robot up without a person touching it.
- **`TurnToLoad`** — spin the attachment motor until it hits its stop, then
  turn to an exact angle. Every attachment starts in the same position.

## How we keep track of changes
We use **Git**. Every change gets a *commit* with the name of who made it and
a note about what changed and what happened when we tested it. Experiments
happen on *branches*; a change only goes into the competition code after it
passes our **Solved Rule** (works 3–5 times in a row).
