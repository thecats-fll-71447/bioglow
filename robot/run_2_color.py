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
# values) can be added with color_sensor.detectable_colors(...) -- see the
# Pybricks ColorSensor docs, and re-test every attachment after changing it.

from pybricks.parameters import Color
from robot import color_sensor

import run_3_rock
import run_4_leaves
import run_9_vine_roots


def run():
    if color_sensor.color() == Color.RED:
        run_3_rock.run()
    if color_sensor.color() == Color.BLUE or color_sensor.color() == Color.YELLOW:
        run_4_leaves.run()
    if color_sensor.color() == Color.GREEN:
        run_9_vine_roots.run()
