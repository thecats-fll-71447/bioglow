# run_3_rock.py  --  menu selection "2" (RED attachment)
#
# Missions: M03 Flip the Rock  (needs the RED attachment)
# Qualifier (Nov 14): Flag 6/6, rock-returned bonus 5/6.
# Owner(s): Brandon 
#

from robot import driveBase


def run():
    # Start at Left side of Red Zone
    # Align the left side of robot 2 squares from end
    # Front of robot (without attachment) is aligned to squares above FIRST LEGO LEAGUE)
    # (Use Template!)
    driveBase.turn(-5)
    driveBase.straight(300)
    driveBase.straight(-50)
    driveBase.straight(75)
    driveBase.use_gyro(False)
    driveBase.straight(-400)
