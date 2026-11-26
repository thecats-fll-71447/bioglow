# main.py -- The Cats competition program (the hub menu).
#
# This is the file you RUN. It imports the setup from robot.py and one
# run_*.py file per menu selection.
#
# Blue (right) area runs first, launched from the starting area with
# selections A, B, and C. Red (left) area next: the first run uses selection
# 1, then selection 2 for the remaining missions. Each of those attachments
# has a colored brick that tells the robot which program to run.
#
#   Menu   | File                 | Missions
#   -------+----------------------+-------------------------------------------
#     A    | run_a_keystone.py    | M13 Keystone Species
#     B    | run_b_fungus.py      | M06 Leafcutter, M07 Fungus, M11 Window
#     C    | run_c_city.py        | M15 Biocentric Architecture
#     1    | run_1_drone.py       | M01 Drone Survey
#     2    | run_2_color.py       | reads the attachment color:
#          |                      |   RED    -> M03 Flip the Rock
#          |                      |   BLUE   -> M04 Lucky Leaves (check)
#          |                      |   YELLOW -> M04 Lucky Leaves (grab)
#          |                      |   GREEN  -> M08 Tangled + M05 Roots
#     Q    | (quit)               |
#
# Not on the menu yet: run_seeds.py (M02 Exploding Seeds) -- see that file.
#
# To add a run: make run_x_name.py with a run() function, import it below,
# and add it to mission_map and base_options.

from pybricks.parameters import Color
from pybricks.tools import hub_menu

from robot import hub, driveBase, resetDriveSettings, resetAttachmentSettings

import run_a_keystone
import run_b_fungus
import run_c_city
import run_1_drone
import run_2_color
import run_d_forest_elder

sequence_index=0

# Base options in strict sequential order (excluding 'Q')
base_options = ["A", "B", "C", "D", "1", "2"]

selected = 0
last_selected = "1"  # Default startup focus

# Which code each menu selection runs
mission_map = {
    "A": run_a_keystone.run,
    "B": run_b_fungus.run,
    "C": run_c_city.run,
    "D": run_d_forest_elder.run,
    "1": run_1_drone.run,
    "2": run_2_color.run,
    "Q": lambda: None,   # quit
}


while selected != "Q":
    hub.light.on(Color.GREEN)
    driveBase.use_gyro(False)

    # Determine the target item that needs to be focused/displayed first
    target_focus = last_selected

    # --- FIXED TERMINATOR RING ROTATION LOGIC ---
    if target_focus == "Q":
        # If Q is explicitly the target, start with Q and show the base options after
        dynamic_options = ["Q"] + base_options
    else:
        # Find where our target item sits in the alphanumeric sequence
        idx = base_options.index(target_focus)

        # Split the list around the target:
        # Part A: From target to the end of the list
        # Part B: From the start of the list up to target (the wrapped elements)
        # We sandwich "Q" between them.
        dynamic_options = base_options[idx:] + ["Q"] + base_options[:idx]

    # Pass the ordered list into the hub menu
    selected = hub_menu(*dynamic_options)

    if selected in mission_map:
        # Save selection context if it is a real mission (ignores 'Q')
        if selected != "Q":
            last_selected = selected

        hub.light.on(Color.YELLOW)
        driveBase.use_gyro(True)
        resetDriveSettings()
        resetAttachmentSettings()

        # Execute the mission code block
        mission_map[selected]()

    else:
        print("Invalid selection")
