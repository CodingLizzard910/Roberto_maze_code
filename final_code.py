# Module Imports
from LocoXtreme import Connection
from LocoXtreme import LocoXtreme
from LocoXtreme import MotorDirection as MD
from LocoXtreme import Data
from LocoXtreme import WaitType as WT
from LocoXtreme import Song
from LocoXtreme import Note
import time

# Create Connection Instance
connection = Connection()

# USB Connection Setup
connection.setup()

# Scan for Robots
robots = connection.scan(4000)

# Get Named Robot
robot = connection.get_robot(robots, "Roberto")

# Create LocoXtreme Object
locoxtreme = LocoXtreme(robot)

# Connect to LocoXtreme
locoxtreme.connect()

# Activate Motors
locoxtreme.activate_motors()

# Enable Sensors
locoxtreme.enable_sensor(Data.ULTRASONIC, 1)
locoxtreme.enable_sensor(Data.ACCELEROMETER, 1)

# Pause for Initializations
time.sleep(0.4)
while(True): # always true so robot is always moving forward
    locoxtreme.move(MD.FORWARD, MD.FORWARD, 1, 1, False)
    distance = locoxtreme.get_sensor_value(Data.ULTRASONIC)
    if(distance < 20):
        locoxtreme.setup_wait(WT.ROTATION, 90)
        locoxtreme.move(MD.FORWARD, MD.BACKWARD, 0.5, 0.5, True) #rotate right
        new_distance = locoxtreme.get_sensor_value(Data.ULTRASONIC)
        time.sleep(0.0001) #sleep so code don't crash
        if new_distance < 25:
            locoxtreme.setup_wait(WT.ROTATION, 180)
            locoxtreme.move(MD.FORWARD, MD.BACKWARD, 0.5, 0.5, True) #rotate 180
            new_new_distance = locoxtreme.get_sensor_value(Data.ULTRASONIC)
            time.sleep(0.0001) #sleep again
            if new_new_distance > 20:
                locoxtreme.move(MD.FORWARD, MD.FORWARD, 1, 1, False) #go forward
        else:
            locoxtreme.move(MD.FORWARD, MD.FORWARD, 1, 1, False) #going forward if no second wall
    time.sleep(0.0001) #sleep number 3


# Deactivate Motors
locoxtreme.deactivate_motors()

# Disconnect From LocoXtreme
locoxtreme.disconnect()