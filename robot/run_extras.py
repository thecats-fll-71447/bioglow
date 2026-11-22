# run_extras.py -- code that is NOT on the competition menu right now.
#
# Kept so nobody loses work. (Git also remembers every old version, so you
# never need to keep "# old code" at the bottom of a file again.)
#   mission5()    - spin the attachment motor one turn
#   mission8()    - first version of the vine run (before roots were added)
#   mission9old() - older version of the vine + roots run

from pybricks.tools import wait
from robot import driveBase, attachment, INCHES_TO_MM, DriveToWall, TurnToLoad


def mission5():
    attachment.run_angle(-800, 360)

def mission8():
    # Mission 8
    #print('Konrad')
    driveBase.settings(straight_speed=200)
    DriveToWall(-200, 30)
    driveBase.straight(560)
    driveBase.arc(100, angle=90)
    driveBase.straight(340)
    driveBase.arc(100, angle=-90)
    driveBase.straight(170)
    attachment.run_angle(-500, 200)
    driveBase.straight(-80)
    driveBase.turn(-85)
    driveBase.settings(straight_speed=450)
    driveBase.straight(800)

def mission9old():
    # Mission 8
    TurnToLoad(200,-140,60)
    DriveToWall(-200, 30)
    driveBase.straight(560)
    driveBase.arc(100, angle=90)
    driveBase.straight(335)
    driveBase.arc(100, angle=-90)
    driveBase.straight(170)
    attachment.run_angle(-500, 200)
    driveBase.straight(-80)
    TurnToLoad(200,-140,60)
    driveBase.turn(-90)
    TurnToLoad(400,-20,50)
    driveBase.straight(11.25*INCHES_TO_MM)
    driveBase.turn(86)
    driveBase.straight(9*INCHES_TO_MM)
    driveBase.straight(-3.5*INCHES_TO_MM)

    attachment.dc(-200)
    wait(1000)
    attachment.dc(0)

    driveBase.turn(angle=-90)
    driveBase.settings(straight_speed=450)
    driveBase.straight(600)
