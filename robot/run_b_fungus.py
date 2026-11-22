# run_b_fungus.py
#
# Missions: M06 Leafcutter Frenzy, M07 Humongous Fungus, M11 Window to the Past
# Qualifier (Nov 14): M06 6/6, M07 6/6, M11 only 2/6 at the qualifier -> the end of this run (window) needs work.
# Owner(s): Asher   <- put your name here!
#

from pybricks.parameters import Stop
from robot import driveBase, attachment, hub


def run():
    # Missions 6, 7, and 11
    print('FUNGUS')
    driveBase.use_gyro(True)
    hub.imu.reset_heading(0)
    driveBase.settings(straight_speed=400)
    attachment.run_angle(-500, 95 * 4) 
    driveBase.straight(850, then=Stop.BRAKE)
    attachment.control.limits(acceleration=5000)
    attachment.run_angle(500, 95 * 4) 
    attachment.control.limits(acceleration=2000)
    driveBase.straight(-55)
    driveBase.turn(87, absolute=True)
    driveBase.straight(-360)
    driveBase.turn(-45)
    driveBase.settings(straight_speed=130)
    driveBase.straight(400)
    driveBase.settings(straight_speed=400)
    driveBase.straight(-100)
    attachment.run_angle(-500, 360) 
    driveBase.turn(110)
    driveBase.straight(255)
    driveBase.straight(-100)
    driveBase.turn(-20)
    driveBase.settings(straight_speed=600)
    driveBase.use_gyro(False)
    driveBase.straight(1000)
