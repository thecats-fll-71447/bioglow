# run_4_leaves.py
#
# Missions: M04 Lucky Leaves  (BLUE attachment = check, YELLOW attachment = grab)
# Qualifier (Nov 14): Leaves + bonus 5/6. Run 4 is launched twice per match.
# Owner(s): Brandon
#

from pybricks.parameters import Color, Stop
from pybricks.tools import wait
from robot import driveBase, attachment, colorSensor, INCHES_TO_MM, default_turn_rate


def run():
    driveBase.settings(straight_speed=300)
    if colorSensor.color() == Color.BLUE:
        # Check the Leaves
        # the second black line has to be alined to the right side of the robot
        driveBase.straight(28 * 25.4)
        driveBase.turn(-45)
        driveBase.straight(5 * 25.4)
        attachment.run_angle(500, -60)
        wait(1500)
        attachment.run_angle(500, 60, Stop.COAST)
        driveBase.straight(-3 * 25.4)
        driveBase.turn(45)
        driveBase.straight(-28 * 25.4)

    # Grab the Leaves
    # left side set up at second black line
    elif colorSensor.color() == Color.YELLOW:
        #TurnToLoad(-500, -200, 50)
        driveBase.straight(730)
        driveBase.settings(turn_rate=60)
        driveBase.turn(-52)
        driveBase.settings(turn_rate=default_turn_rate)
        driveBase.straight(5 * INCHES_TO_MM+32+16)
        attachment.run_angle(500, 360) # pick up leaves
        driveBase.turn(-57)
        driveBase.use_gyro(False) # turn off gyro for drive back
        driveBase.straight(700, then=Stop.COAST)
        #DriveToWall(200, 30)
    else:
        pass
