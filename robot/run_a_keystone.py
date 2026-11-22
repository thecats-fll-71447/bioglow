# run_a_keystone.py
#
# Missions: M13 Keystone Species (30 pts)
# Qualifier (Nov 14): Scored 6 of 6 rounds at the qualifier. Don't break it!
# Owner(s): Asher!
#

from robot import driveBase


def run():
    # Mission 13
    print('KEYSTONE', 'SPEICES', '???')
    driveBase.straight(200)
    driveBase.turn(-90)
    driveBase.straight(350)
    driveBase.turn(-90)
    driveBase.straight(100)
    driveBase.settings(straight_speed=550)
    driveBase.straight(-100)
    driveBase.turn(90)
    driveBase.use_gyro(False)
    driveBase.straight(-500)
