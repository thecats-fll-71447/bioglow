# robot.py -- Cat-Bot hardware setup + shared helper functions.
#
# Every run file does:   from robot import ...
# so the motors, sensors, and drive base are set up ONE time, here.
#
# If you change something in this file, it changes for EVERY run.
# Test all the runs after you edit it!

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


INCHES_TO_MM = const(25.4)


# ---------- Hardware ----------
hub = PrimeHub()
leftMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.A, Direction.CLOCKWISE)
driveBase = DriveBase(leftMotor, rightMotor, 56, 4.375 * INCHES_TO_MM)
attachment = Motor(Port.B, Direction.CLOCKWISE)
colorSensor = ColorSensor(Port.C) # Used to determine mission to be run
driveToWallTimer = StopWatch()

# Fetch and store default attachment limits
default_speed, default_acceleration, default_torque = attachment.control.limits()
# Fetch and store the default configuration tuple
driveBaseDefaults = driveBase.settings()

# Unpack the tuple to make the individual defaults ready to use
(default_straight_speed, default_DBacceleration, default_turn_rate, default_turn_acceleration) = driveBaseDefaults


# ---------- Helpers ----------
def resetDriveSettings():
    driveBase.settings(default_straight_speed, default_DBacceleration, default_turn_rate, default_turn_acceleration)

def resetAttachmentSettings():
    attachment.control.limits(default_speed, default_acceleration, default_torque)

# Drive to wall and then stop when wheel load exceeds StopLoad parameter (0-100, need to test load values for specific speeds)
def DriveToWall(DriveSpeed, StopLoad, MaxTime = 7500):
    driveToWallTimer.reset()
    driveBase.drive(DriveSpeed, 0)
    while not (abs(leftMotor.load()) >= StopLoad and abs(rightMotor.load()) >= StopLoad or driveToWallTimer.time() >= MaxTime):
        wait(0)
    driveBase.brake()
    wait(50)

# Turn attachment motor at MotorSpeed until attachment motor load exceeds StopLoad. Then rotate the attachment motor to new angle
def TurnToLoad(MotorSpeed, ResetAngle, StopLoad):
    attachment.run(MotorSpeed)
    while not abs(attachment.load()) >= StopLoad:
        wait(0)
    attachment.brake()
    wait(250)
    attachment.run_angle(MotorSpeed, ResetAngle, Stop.BRAKE)

def MissionNotDefined():
    hub.light.blink(Color.RED, [500, 500])
    wait(3000)
    hub.light.on(Color.GREEN)
