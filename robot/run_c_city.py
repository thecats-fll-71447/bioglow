# run_c_city.py  --  menu selection "C"
#
# Missions: M15 Biocentric Architecture (model on the dock - which one?)
# Qualifier (Nov 14): Nesting canopy 6/6, garden skylight 4/6, environmental bonus 0/6.
# Owner(s): Asher
#

from pybricks.tools import wait
from robot import driveBase, attachment


def run():
    # Mission 15
    print('City', 'City', 'ABC')
    driveBase.settings(straight_speed=400)
    #attachment.run_angle(-500, 390) # changed both, maybe only one needed?
    attachment.run_angle(-500, 30)
    driveBase.straight(280)
    driveBase.turn(-90)
    driveBase.straight(580)
    driveBase.turn(90)
    driveBase.straight(30)
    attachment.control.limits(acceleration=500)
    attachment.run_angle(-100, -120) # changed both, maybe only one needed?
    wait(1000)
    attachment.run_angle(-100, 120) # changed both, maybe only one needed?
    driveBase.straight(-20)
    driveBase.turn(-90)
    driveBase.straight(300)
    driveBase.turn(90)
    driveBase.straight(250)
    driveBase.turn(-90)
    driveBase.straight(-130)
    driveBase.straight(30)
    driveBase.turn(10)
    attachment.run_angle(rotation_angle=100,speed=100, wait=False)
    driveBase.straight(1000) #250
