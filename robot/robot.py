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
LeftMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
RightMotor = Motor(Port.A, Direction.CLOCKWISE)
driveBase = DriveBase(LeftMotor, RightMotor, 56, 4.375 * INCHES_TO_MM)
attachment = Motor(Port.B, Direction.CLOCKWISE)
color_sensor = ColorSensor(Port.C) # Used to determine mission to be run

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
# TODO (starter issue): this checks LeftMotor.load() TWICE. The second one was
# probably meant to be RightMotor.load(). Fixing it changes WHEN the robot stops,
# so test every run that uses Drive_to_Wall (run 9) before merging a fix.
def Drive_to_Wall(DriveSpeed, StopLoad):
    driveBase.drive(DriveSpeed, 0)
    while not (abs(LeftMotor.load()) >= StopLoad and abs(LeftMotor.load()) >= StopLoad):
        wait(0)
    driveBase.brake()

# Same idea, but gives up after maxTime milliseconds so the robot can never get
# stuck pushing forever. From the Exploding Seeds program (Mission2_v1_0.py).
DriveToWallTimer = StopWatch()

def Drive_to_Wall_Timed(DriveSpeed, StopLoad, MaxTime):
    DriveToWallTimer.reset()
    driveBase.drive(DriveSpeed, 0)
    while not (abs(LeftMotor.load()) >= StopLoad and abs(RightMotor.load()) >= StopLoad or DriveToWallTimer.time() >= MaxTime):
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
