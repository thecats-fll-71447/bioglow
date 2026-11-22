# run_2_color.py  --  menu selection "2"
#
# The color sensor reads the brick on the attachment and picks the code:
#   RED            -> run_3_rock.py        (M03 Flip the Rock)
#   BLUE or YELLOW -> run_4_leaves.py      (M04 Lucky Leaves: check / grab)
#   GREEN          -> run_9_vine_roots.py  (M08 Tangled + M05 Reaching Roots)
# Any other color (or no attachment) -> nothing happens.
#
# Copied exactly from Mission2 in the team's MissionMenu.py -- the program
# that ran at the Nov 14 qualifier (Pybricks backup of Nov 18, 2026).
#
# Colors: by default the sensor knows RED, YELLOW, GREEN, BLUE, WHITE and NONE.
# WHITE is still free. More colors (like MAGENTA, or your own measured HSV
# values) can be added with colorSensor.detectable_colors(...) -- see the
# Pybricks ColorSensor docs, and re-test every attachment after changing it.

from pybricks.parameters import Color
from robot import colorSensor

import run_3_rock
import run_4_leaves
import run_9_vine_roots
import run_seeds


def run():
    if colorSensor.color() == Color.WHITE:
        run_seeds.run()
    if colorSensor.color() == Color.RED:
        run_3_rock.run()
    if colorSensor.color() == Color.BLUE or colorSensor.color() == Color.YELLOW:
        run_4_leaves.run()
    if colorSensor.color() == Color.GREEN:
        run_9_vine_roots.run()

