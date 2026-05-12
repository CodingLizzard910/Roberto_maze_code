# Roberto_maze_code
# title: LocoRobo Final Project (Roberto)
# author: Abram Grimsley
# date: 5/11/2026

# Intro

This is a breakdown and summary for my code written for the LocoRobo Maze final project. The code was written and finalyzed from April 30th to May 8th and was tested on May 4th and May 8th. Three official attempts were given and the code/robot successfully finished the maze on the third attempt with a time of 8 seconds. The code went through two iterations before before its now final form and a couple edits to the final form to be a little more efficient. The only major failures outside the code was with the robot. The left wheele was loose and made the robot veere left, which is why two of the three official attempts were failures. The code isn't perfect by any means, but it is, in my opinion, pretty efficient and it does work. Overall, as my first ever coding project, I am very proud. This project is titled "Roberto", because that was the name assigned to the robot to be differentiated from other LocoRobo robots.

# Breakdown of the Code

The code beggins with the standard LocoRobo code of connecting to the robot and calling back some basic funcctions:
```python
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
robot = connection.scan(4000)

# Get Named Robot
robot = connection.get_robot(robot,"Roberto")

# Create LocoXtreme Object
locoxtreme = LocoXtreme(robot)

# Connect to LocoXtreme
locoxtreme.connect()

# Activate Motors
locoxtreme.activate_motors()

```

The next line of code enables the Ultrasonic sensor. The Ultrasonic sensor is very important to this project (probably the most important part). The Ultrasonic sensor enables the robot so sence object infront of it within a certain distance.

```python
locoxtreme.enable_sensor(Data.ULTRASONIC, 1)

```
To break this down, the line "locoxtreme.eneble_sensor()" enables the robot's sensor. Within the parenthesis, "Data.ULTRASONIC" tells the robot to begin collecting ultrasonic data by sending sound waves out at a certain interval of pulses and timing how long it takes for the sound waves to reflect back to the robot. Using that and the formula of "Diatance = Pulse Width * 34/10/2", the robot is able to calculate the distance of an object infront of it (in cm).
The next line of code under the Ultrasonic sensor enables the Accelerometer, which is used to measure acceleration and direction in a 3d space. However, I did not use the accelerometer in my code, so it isn't as important to this project.
```python
locoxtreme.enable_sensor(Data.ACCELEROMETER, 1)
```

The next 18 lines of code is my script for the robot to follw:
```python
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
```
Broken down, the code is actually quite simple. Starting with a "time.sleep()" to make the robot rest before the code beggins running. This lasts 0.4 seconds.
```python
time.sleep(0.4)
```

Next is a "While" loop, which displays the boolean value of "True" to call the robot to always be running the code unless manually stopped.
```python
while(True):
```

The first two lines within the "While" loop, are the first real instructions given to the robot. The command "locoxtreme.move()" tells the robot to move, within the parenthesis, the first "MD.FORWARD" moves the Left Motor Direction (MD) forward, and the second "MD.FORWARD" moves the Right Motor Direction (MD) forward as well. The two numbers that follow tell the motor at what speed to move (which is 1). The boolean operator "False" at the end tells the robot whether to call back the previous code, and since there is nothing but the start of the loop, the value is left at "False" for this line. THe line directly under it, calls the ultrasonic sensor to constantly read for any objects within a certain distance.
```python
locoxtreme.move(MD.FORWARD, MD.FORWARD, 1, 1, False)
    distance = locoxtreme.get_sensor_value(Data.ULTRASONIC)
```

The next couple lines is a bunch of nested "if" statements which use the ultrasonic sensor to determine when to turn and in what direction. If the ultrasonic sensor "sees" an object infront of it within less than 20 cm, the code stops the robot, and makes a 90 degree turn to the right (locoxtreme.setup_wait(ROTATION, 90)) at 0.5 speed by making the left motor turn forward and the right motor turn backwards (locoxtreme.move(MD.FORWARD, MD.BACKWARD, 0.5, 0.5, True)). Then the ultrasonic sensor is called again to continue measuring distance. Another "time.sleep" is added to give the robot a micro-break as to not crash the code.
```python
if(distance < 20):
        locoxtreme.setup_wait(WT.ROTATION, 90)
        locoxtreme.move(MD.FORWARD, MD.BACKWARD, 0.5, 0.5, True) 
        new_distance = locoxtreme.get_sensor_value(Data.ULTRASONIC)
        time.sleep(0.0001) 
```

Keeping within the existing "if" statement, another is added to use the newly recorded ultrasonic data to determine what to do next. If after the robot turns right, there is an immediate object within 25 cm, the robot will make a left turn my turning around 180 degrees and then recording new ultrasonic sesor data.
```python
if new_distance < 25:
            locoxtreme.setup_wait(WT.ROTATION, 180)
            locoxtreme.move(MD.FORWARD, MD.BACKWARD, 0.5, 0.5, True) #rotate 180
            new_new_distance = locoxtreme.get_sensor_value(Data.ULTRASONIC)
            time.sleep(0.0001) #sleep again
```

Again, we make a new "if" statement inside the two already existing "if" statements to make a third check. This however checks if, after turning around, that the "coast is clear" within a distance of 20 cm, so that the robot can finally move forward.
```python
if new_new_distance > 20:
                locoxtreme.move(MD.FORWARD, MD.FORWARD, 1, 1, False) #go forward
```

Finally, an "else" statement is added for the previous "if" statement, in case, after turning 180 degrees, there is nothing in the robot's way within 25 cm, then the robot will ignore the next "if" statement and just move forward. And finally, a last "time.sleep" is added to keep the code from crashing.
```python
else:
            locoxtreme.move(MD.FORWARD, MD.FORWARD, 1, 1, False) #going forward if no second wall
    time.sleep(0.0001) #sleep number 3
```

# conclusion
This code would not have been succesful without the help of my classmates and Professor Kevin Lopez Chavez. This was a fun project, and I hope to be able to try out more code with the LocoRobo robot in the future.
