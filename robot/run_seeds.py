# run_seeds.py  --  NOT ON THE MENU YET
#
# Missions: M02 Exploding Seeds (10 pts per seed, 30 max)
# Attachment: StarterBotAttachment-Mission2 (Studio file in Drive > Models)
# Status: solved after the qualifier; tested as its own program.
# Owner(s): ______   <- put your name here!
#
# Copied exactly from Mission2_v1_0.py in the Pybricks backup of Nov 18, 2026.
# (Its own copy of DriveToWall, with the time limit, now lives in robot.py
# as DriveToWall_Timed.)
#
# TO ADD IT TO THE MENU, pick ONE of these (team decision):
#   a) its own menu selection: in main.py, import run_seeds, add "S": run_seeds.run to
#      mission_map, and add "S" to base_options where it falls in the match.
#   b) a color: put a colored brick on the attachment (one not used yet, like
#      WHITE) and add  if colorSensor.color() == Color.WHITE: run_seeds.run()
#      to run_2_color.py.
# Then test the whole match again.

from pybricks.parameters import Stop
from robot import driveBase, attachment, DriveToWall_Timed


def run():
    # attachment can move
    # 250 degrees max from bottom
    DriveToWall_Timed(300, 35, 5000)
    attachment.run_angle(500, -245)
    driveBase.straight(-500)
    attachment.run_angle(500, 245, Stop.COAST)
