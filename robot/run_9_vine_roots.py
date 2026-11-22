# run_9_vine_roots.py
#
# Missions: M08 Tangled + M05 Reaching Roots
# Qualifier (Nov 14): Vine 4/6, roots 3/6 (only 1 complete). Biggest place to gain points.
# Owner(s): Brandon/Konrad   <- put your name here!
#

from pybricks.parameters import Stop
from pybricks.tools import wait
from robot import driveBase, attachment, INCHES_TO_MM, DriveToWall, TurnToLoad


def run():
    driveBase.settings(straight_speed=300)
    # Mission 8
    attachment.run_angle(rotation_angle=20,speed=-100,then=Stop.HOLD,wait=False)
    DriveToWall(-200, 30)
    driveBase.straight(570)
    driveBase.arc(100, angle=90)
    driveBase.straight(315)
    driveBase.arc(100, angle=-90)
    #driveBase.turn()
    driveBase.straight(300)
    attachment.run_angle(-200, 90, then=Stop.COAST)
    driveBase.straight(-200)
    attachment.run_angle(-200, 30, then=Stop.HOLD)
    driveBase.turn(-90)
    TurnToLoad(200,-0,90)
    driveBase.straight(11*INCHES_TO_MM)
    driveBase.turn(85)
    driveBase.straight(12*INCHES_TO_MM)
    driveBase.straight(-3.5*INCHES_TO_MM)
    # first smack
    attachment.dc(-100)
    wait(200)
    attachment.dc(0)
    # back up
    driveBase.straight(-50)

    def smack_cycle():
        # return position
        attachment.dc(100)
        wait(200)
        attachment.dc(0)
        # drive back
        driveBase.straight(50)
        #smack root
        attachment.dc(-100)
        wait(200)
        attachment.dc(0)
        # back up
        driveBase.straight(-50)

    smack_cycle()
    smack_cycle()

    #attachment.run_angle(speed=300, rotation_angle=180, then=Stop.COAST, wait=False)
    driveBase.turn(angle=-90)
    driveBase.settings(straight_speed=450)
    driveBase.use_gyro(False)
    driveBase.straight(600)
    attachment.dc(100)
    wait(100)
    attachment.dc(0)
