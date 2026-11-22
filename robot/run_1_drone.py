# run_1_drone.py  --  menu selection "1"
#
# Missions: M01 Drone Survey
# Qualifier (Nov 14): Drone 5/6. LiDAR bonus never scored (10 pts available).
# Owner(s): Brandon   <- put your name here!
#

from robot import driveBase


def run():
    driveBase.use_gyro(False)
    driveBase.settings(straight_speed=400)
    driveBase.straight(700)
    driveBase.straight(-700)
