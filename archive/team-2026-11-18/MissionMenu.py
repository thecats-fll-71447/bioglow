from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu


INCHES_TO_MM = const(25.4)

# Mission information
# Blue (right) area runs first, run launch from starting area
# with selections A, B, and C
# Red (left) area next, first run with start area uses selection 1, then
# use selection 2 for remaining missions. The attachment as a color to determine
# which program to use for these missions.

hub = PrimeHub()
leftMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.A, Direction.CLOCKWISE)
driveBase = DriveBase(leftMotor, rightMotor, 56, 4.375 * INCHES_TO_MM)
attachment = Motor(Port.B, Direction.CLOCKWISE)
colorSensor = ColorSensor(Port.C) # Used to determine mission to be run

# Fetch and store default attachment limits
default_speed, default_acceleration, default_torque = attachment.control.limits()
# Fetch and store the default configuration tuple
driveBaseDefaults = driveBase.settings()

# Unpack the tuple to make the individual defaults ready to use
(default_straight_speed, default_DBacceleration, default_turn_rate, default_turn_acceleration) = driveBaseDefaults

def resetDriveSettings():
    driveBase.settings(default_straight_speed, default_DBacceleration, default_turn_rate, default_turn_acceleration)

def resetAttachmentSettings():
    attachment.control.limits(default_speed, default_acceleration, default_torque)

# Drive to wall and then stop when wheel load exceeds StopLoad parameter (0-100, need to test load values for specific speeds)
def DriveToWall(DriveSpeed, StopLoad):
    driveBase.drive(DriveSpeed, 0)
    while not (abs(leftMotor.load()) >= StopLoad and abs(leftMotor.load()) >= StopLoad):
        wait(0)
    driveBase.brake()

# Turn attachment motor at MotorSpeed until attachment motor load exceeds StopLoad. Then rotate the attachment motor to new angle
def TurnToLoad(MotorSpeed, ResetAngle, StopLoad):
    attachment.run(MotorSpeed)
    while not abs(attachment.load()) >= StopLoad:
        wait(0)
    attachment.brake()
    wait(250)
    attachment.run_angle(MotorSpeed, ResetAngle, Stop.BRAKE)

def Mission1():
    driveBase.use_gyro(False)
    driveBase.settings(straight_speed=400)
    driveBase.straight(700)
    driveBase.straight(-700)

def Mission2():
    if colorSensor.color() == Color.RED:
        Mission3()
    if colorSensor.color() == Color.BLUE or colorSensor.color() == Color.YELLOW:
        Mission4()
    if colorSensor.color() == Color.GREEN:
        Mission9()

def Mission3():
    # Start at Left side of Red Zone
    # Align the left side of robot 2 squares from end
    # Front of robot (without attachment) is aligned to squares above FIRST LEGO LEAGUE)
    driveBase.turn(-5)
    driveBase.straight(300)
    driveBase.straight(-50)
    driveBase.straight(75)
    driveBase.use_gyro(False)
    driveBase.straight(-400)

def Mission4():
    driveBase.settings(straight_speed=300)
    if colorSensor.color() == Color.BLUE:
        # Check the Leaves
        driveBase.reset(0, 0)
        driveBase.straight(696)
        attachment.run_angle(400, 730)
        wait(1000)
        attachment.run_angle(500, -730)
        driveBase.use_gyro(False) # turn off gyro for drive back
        driveBase.straight(-700, then=Stop.COAST)
        #DriveToWall(-200, 30)

    # Grab the Leaves
    # left side set up at second black line
    elif colorSensor.color() == Color.YELLOW:
        #TurnToLoad(-500, -200, 50)
        driveBase.straight(730)
        driveBase.settings(turn_rate=60)
        driveBase.turn(-52)
        driveBase.settings(turn_rate=default_turn_rate)
        driveBase.straight(5 * INCHES_TO_MM+32+16)
        attachment.run_angle(500, 360) # pick up leaves
        driveBase.turn(-57)
        driveBase.use_gyro(False) # turn off gyro for drive back
        driveBase.straight(700, then=Stop.COAST)
        #DriveToWall(200, 30)
    else:
        pass

def Mission5():
    attachment.run_angle(-800, 360)

def Mission6():
    MissionNotDefined()

def Mission7():
    MissionNotDefined()

def Mission8():
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

# test code to see if we can do mission 5 after doing mission 8
def Mission9():
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


# test code to see if we can do mission 5 after doing mission 8
def Mission9old():
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

def Mission10():
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

def Mission11():
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


def Mission12():
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
    #driveBase.turn(-70)
    #driveBase.settings(straight_speed=500)
    #driveBase.straight(600)



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

# --- CONFIGURATION TOGGLE ---
# True  = Follows the exact match run order listed in planned_sequence.
# False = Follows standard order, but rotates like a ring based on what you ran last.
USE_PLANNED_SEQUENCE = False

# Define your strict chronological match run order here
planned_sequence = ["A", "B", "C","1","3","4","4","9"]
sequence_index = 0

# Base options in strict sequential order (excluding 'Q')
base_options = ["A", "B", "C", "1", "2"]

selected = 0
last_selected = "1"  # Default startup focus

# 2. Build the selection map dynamically
mission_map = {}

# Map "1"-"9" to Mission1-Mission9
for i in range(1, 10):
    mission_map[str(i)] = globals()[f"Mission{i}"]

# Map "A"-"F" to Mission10-Mission15
hex_mapping = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
for char, num in hex_mapping.items():
    mission_map[char] = globals()[f"Mission{num}"]

# Add the 'Q', quit, condition
mission_map["Q"] = lambda: None


while selected != "Q":
    hub.light.on(Color.GREEN)
    driveBase.use_gyro(False)

    # Determine the target item that needs to be focused/displayed first
    if USE_PLANNED_SEQUENCE:
        if sequence_index < len(planned_sequence):
            target_focus = planned_sequence[sequence_index]
        else:
            target_focus = "Q"
    else:
        target_focus = last_selected

    # --- FIXED TERMINATOR RING ROTATION LOGIC ---
    if target_focus == "Q":
        # If Q is explicitly the target, start with Q and show the base options after
        dynamic_options = ["Q"] + base_options
    else:
        # Find where our target item sits in the alphanumeric sequence
        idx = base_options.index(target_focus)

        # Split the list around the target:
        # Part A: From target up to 'F'
        # Part B: From '1' up to target (the wrapped elements)
        # We sandwich "Q" strictly between 'F' and the wrapped elements!
        dynamic_options = base_options[idx:] + ["Q"] + base_options[:idx]


    # Pass the perfectly ordered list into the hub menu
    selected = hub_menu(*dynamic_options)

    if selected == "R":
        sequence_index = 0

    elif selected in mission_map:
        # Save selection context if it is a real mission (ignores 'Q')
        if selected != "Q":
            last_selected = selected

        hub.light.on(Color.YELLOW)
        driveBase.use_gyro(True)
        driveBase.settings(straight_speed=200)
        resetDriveSettings()
        resetAttachmentSettings()

        # Execute the mission code block
        mission_map[selected]()

        # Advance sequence index if the expected planned item was run
        if USE_PLANNED_SEQUENCE and selected == target_focus and sequence_index < len(planned_sequence):
            sequence_index += 1

    else:
        print("Invalid selection")



# old code

def Mission12reversed():
    # Mission 15
    print('City', 'City', 'ABC')
    driveBase.settings(straight_speed=400)
    attachment.run_angle(500, 390)
    driveBase.straight(-280)
    driveBase.turn(90)
    driveBase.straight(-580)
    driveBase.turn(-90)
    driveBase.straight(-30)
    attachment.control.limits(acceleration=500)
    attachment.run_angle(100, -120)
    wait(2000)
    attachment.run_angle(100, 120)
    driveBase.straight(20)
    driveBase.turn(90)
    driveBase.straight(-300)
    driveBase.turn(-90)
    driveBase.straight(-250)
    driveBase.turn(90)
    driveBase.straight(120)
    driveBase.straight(-30)
    driveBase.turn(-20)
    driveBase.straight(-250)
    driveBase.turn(70)
    driveBase.settings(straight_speed=500)
    driveBase.straight(-600)

def Mission11reversed():
    # Missions 6, 7, and 11
    print('FUNGUS')
    driveBase.use_gyro(True)
    hub.imu.reset_heading(0)
    driveBase.settings(straight_speed=400)
    attachment.run_angle(-500, 95 * 4)
    driveBase.straight(-850, then=Stop.BRAKE)
    attachment.control.limits(acceleration=5000)
    attachment.run_angle(500, -95 * 4)
    attachment.control.limits(acceleration=2000)
    driveBase.straight(55)
    driveBase.turn(87, absolute=True)
    driveBase.straight(360)
    driveBase.turn(-45)
    driveBase.settings(straight_speed=130)
    driveBase.straight(-400)
    driveBase.settings(straight_speed=400)
    driveBase.straight(100)
    attachment.run_angle(500, 400)
    driveBase.turn(110)
    driveBase.straight(-240)
    driveBase.straight(100)
    driveBase.turn(-20)
    driveBase.settings(straight_speed=600)
    driveBase.straight(-1000)

#old code
def Mission10reversed():
    # Mission 13
    print('KEYSTONE', 'SPEICES', '???')
    driveBase.straight(-200)
    driveBase.turn(90)
    driveBase.straight(-350)
    driveBase.turn(90)
    driveBase.straight(-100)
    driveBase.settings(straight_speed=550)
    driveBase.straight(100)
    driveBase.turn(-90)
    driveBase.straight(500)