# The Cats — FIRST LEGO League Team 71447 · BIOGLOW 2026–27

Code, notes, and team website for **Cat-Bot**, the robot that won the
**Robot Design Award** and **Robot Performance Award** (340 points) at
Elm City Robo Fest on November 14, 2026.

**Next stop: Connecticut State Championship, December 12, 2026 (Glastonbury).**

---

## What's in here

| Folder | What it is |
|---|---|
| `robot/` | **The competition program.** Run `robot/main.py` on the hub. |
| `tests/` | `check.py` tests the code on a laptop — no robot needed. |
| `tools/` | `load_robot.py` sends the program to a hub, after you pick which hub. |
| `archive/` | The single-file program that ran at the qualifier, plus older versions. Our safety net. |
| `experiments/` | Everyone's test programs from Pybricks backups (October–November). |
| `docs/` | Our team website and blog (published with GitHub Pages). |

## The competition menu

| Menu selection | Attachment color | File | Missions | Qualifier result |
|---|---|---|---|---|
| A | | `run_a_keystone.py` | M13 Keystone Species | 6/6 ✅ |
| B | | `run_b_fungus.py` | M06 Leafcutter, M07 Fungus, M11 Window | M06, M07 6/6 ✅ · M11 2/6 ⚠️ |
| C | | `run_c_city.py` | M15 Biocentric Architecture | canopy 6/6 ✅ · skylight 4/6 ⚠️ |
| 1 | | `run_1_drone.py` | M01 Drone Survey | 5/6 |
| 2 | RED | `run_3_rock.py` | M03 Flip the Rock | flag 6/6 · bonus 5/6 |
| 2 | BLUE, then YELLOW | `run_4_leaves.py` | M04 Lucky Leaves (check, then grab) | 5/6 |
| 2 | GREEN | `run_9_vine_roots.py` | M08 Tangled, M05 Reaching Roots | vine 4/6 · roots 3/6 ⚠️ |
| — | | `run_seeds.py` | M02 Exploding Seeds — **solved after the qualifier, not on the menu yet** | new for State |

Blue (right) home area first: **A, B, C**. Then red (left) home area: **1**,
then **2** for everything else. On selection 2, Cat-Bot reads the **color brick
on the attachment** with its forward-facing color sensor and runs the right
code (`run_2_color.py`).

## Getting started

1. **First time on a laptop?** Follow [SETUP.md](SETUP.md).
2. **Every work session:** follow [WORKFLOW.md](WORKFLOW.md).
3. **Before you walk to the table:** run `python tests/check.py`.

## The rules we live by

- **`main` is always competition-ready.** Experiments happen on branches.
- **The Solved Rule:** a mission is only *solved* when it works **3–5 times in
  a row**. A branch only goes into `main` after it passes the Solved Rule.
- **Keep it simple.** If a fix takes days, look for an easier way.
- **Write down what you learned** — in your commit message *and* on the blog.

## Team

Asher · Brandon · Aedan · Konrad · Thomas

Coaches: Coach Alan, ______
