from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu


INCHES_TO_MM = const(25.4)


hub = PrimeHub()
LeftMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
RightMotor = Motor(Port.A, Direction.CLOCKWISE)
DriveBase1 = DriveBase(LeftMotor, RightMotor, 56, 4.375 * INCHES_TO_MM)
attachment = Motor(Port.B, Direction.CLOCKWISE)
color_sensor = ColorSensor(Port.C)

# use gyro, generally
DriveBase1.use_gyro(True)

# Drive to wall and then stop when wheel load exceeds StopLoad parameter (0-100, need to test load values for specific speeds)
def Drive_to_Wall(DriveSpeed, StopLoad):
    DriveBase1.drive(DriveSpeed, 0)
    while not (abs(LeftMotor.load()) >= StopLoad and abs(LeftMotor.load()) >= StopLoad):
        wait(0)
    DriveBase1.brake()

# Turn attachment motor at MotorSpeed until attachment motor load exceeds StopLoad. Then rotate the attachment motor to new angle
def TurnToLoad(MotorSpeed, ResetAngle, StopLoad):
    attachment.run(MotorSpeed)
    while not abs(attachment.load()) >= StopLoad:
        wait(0)
    attachment.brake()
    wait(250)
    attachment.run_angle(MotorSpeed, ResetAngle, Stop.BRAKE)

def Mission1():
    # The main program starts here.
    DriveBase1.settings(straight_speed=450)
    DriveBase1.straight(32 * INCHES_TO_MM)
    DriveBase1.straight(-1000)


def Mission2():
    MissionNotDefined()

def Mission3():
    # Start at Left side of Red Zone
    # Align the left side of robot 2 squares from end
    # Front of robot (without attachment) is aligned to squares above FIRST LEGO LEAGUE)
    if color_sensor.color() == Color.RED:
        DriveBase1.turn(-5)
        DriveBase1.straight(300)
        DriveBase1.straight(-50)
        DriveBase1.straight(75)
        DriveBase1.straight(-400)

def Mission4():
    if color_sensor.color() == Color.BLUE:
        # Check the Leaves
        DriveBase1.reset(0, 0)
        DriveBase1.straight(696)
        attachment.run_angle(200, 730)
        wait(3000)
        attachment.run_angle(300, -730)
        Drive_to_Wall(-200, 30)
    
    
    # Grab the Leaves
    # left side set up at second black line
    elif color_sensor.color() == Color.YELLOW:
        TurnToLoad(-500, -150, 50)
        DriveBase1.straight(730)
        DriveBase1.settings(turn_rate=60)
        DriveBase1.turn(-57)
        DriveBase1.straight(5 * INCHES_TO_MM)
        attachment.run_angle(500, 360)
        DriveBase1.turn(-57)
        Drive_to_Wall(200, 30)
    else:
        pass

def Mission5():
    MissionNotDefined()

def Mission6():
    MissionNotDefined()

def Mission7():
    MissionNotDefined()

def Mission8():
    MissionNotDefined()

def Mission9():
    MissionNotDefined()

def Mission10():
    MissionNotDefined()

def Mission11():
    MissionNotDefined()

def Mission12():
    MissionNotDefined()

def Mission13():
    MissionNotDefined()

def Mission14():
    MissionNotDefined()

def Mission15():
    MissionNotDefined()

def MissionNotDefined():
    hub.light.blink(Color.RED, [500, 500])
    wait(3000)
    hub.light.on(Color.GREEN)

# Start Menu Selection Code
selected = 0

# 1. Define single-character choices for the hub display
# Options 1-9 stay the same; 10-15 become A-F
display_options = [str(i) for i in range(1, 10)] + ["A", "B", "C", "D", "E", "F", "Q"]

# 2. Build the selection map dynamically 
mission_map = {}

# Map "1"-"9" to Mission1-Mission9
for i in range(1, 10):
    mission_map[str(i)] = globals()[f"Mission{i}"]

# Map "A"-"F" to Mission10-Mission15
hex_mapping = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
for char, num in hex_mapping.items():
    mission_map[char] = globals()[f"Mission{num}"]

# 3. Add the 'Q' condition
mission_map["Q"] = lambda: None
while selected != "Q":
    hub.light.on(Color.GREEN)
    # display_options now only contains single characters, preventing the ValueError
    selected = hub_menu(*display_options)
    
    if selected in mission_map:
        hub.light.on(Color.YELLOW)
        mission_map[selected]()  
    else:
        print("Invalid selection")
