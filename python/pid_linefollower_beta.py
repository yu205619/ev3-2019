#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from tank import Tank

#degrees per second?
robot_speed = 70

kp = 0.5
ki = 0
kd = 0.1

print("robot_speed:",robot_speed)
print("kp:",kp,"ki:",ki,"kd",kd)

target_brightness = 40

total_error = 0
last_error = 0
#[degrees(clockwise),reset_gyro,angle/reflection,detect/turn,<turn degrees(clockwise)>]
#turns:
#1-4 = curve
#5 = reverse + detect
#6 = go forwards
#turns = [[20,False,"detect_angle"],[0,False,"detect_angle"],[-20,False,"detect_angle"],[0,False,"detect_angle"],[-20,False,"detect_angle"],[-20,False,"detect_angle"]]
turns = [[80,False,"reflection","detect"],[80,False,"reflection","detect"]]
angle_error = 10
reflection_error = 10

def turn_instructions():
    global steering_type,direction
    if turn == 0:
        steering_type = "gyro"
    elif turn == 1:
        steering_type = "pid"

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S4)
left_color_sensor = ColorSensor(Port.S2)
wheel_size = 56
axle_distance = 120
base = DriveBase(left_motor,right_motor,wheel_size,axle_distance)
tank = Tank(gyro,left_motor,right_motor,wheel_size,axle_distance)
watch = StopWatch()
leave_base = True
turn = 0

direction = "forwards"
steering_type = "pid"

brick.sound.beep()

gyro.reset_angle(0)
if abs(gyro.speed()) > 0:
    leave_base = False
    print("Gyro Drifting. Drift:",gyro.speed())

if leave_base:
    # while len(turns) > 0:
    while True:
        #the steering
        if steering_type == "pid":
            reflection_reading = left_color_sensor.reflection()
            error = target_brightness - reflection_reading
            pid = kp * error + ki * total_error + kd * last_error
            print("reflection: "+str(round(reflection_reading,1)),end="\t\t")
            print("gyro: "+str(round(gyro.angle(),1)),end="\t\t")
            print("p: "+str(round(error*kp,1)),"i: "+str(round(total_error*ki,1)),end="\t\t")
            print("d: "+str(round(last_error*kd,1)),"pid: "+str(round(pid,1)))

            if direction == "forwards":
                base.drive(robot_speed,pid*-1)
            elif direction == "backwards":
                base.drive(robot_speed*-1,pid)
    
        elif steering_type == "gyro":
            print("reflection: "+str(round(reflection_reading,1)),end="\t\t")
            print("gyro: "+str(round(gyro.angle(),1)),end="")

            if direction == "forwards":
                base.drive(robot_speed,gyro.angle()*-1)
            elif direction == "backwards":
                base.drive(robot_speed*-1,gyro.angle())

        #set pid for next time
        total_error += error
        last_error = error


        #turning
        if turn < len(turns):
            if turns[turn][2] == "angle" and gyro.angle() > turns[turn][0] - angle_error and gyro.angle() < turns[turn][0] + angle_error:
                print("\nTurning Turn:",turns[turn],", Turn Count:",turn,"\n")
                if turns[turn][3] == "turn":
                    tank.spin(turns[turn][4],100)
            
            elif turns[turn][2] == "reflection" and reflection_reading > turns[turn][0] - reflection_error and reflection_reading < turns[turn][0] + reflection_error:
                print("\nTurning Turn:",turns[turn],", Turn Count:",turn,"\n")
                if turns[turn][3] == "turn":
                    tank.spin(turns[turn][4],100)

            if turns[turn][1]:
                gyro.reset_angle(0)
            turn += 1
            if turn >= len(turns):
                print("\n\nAll Turns Completed\n\n")

            #instructions for specific turns. turn should be actual count (turn index + 1)
            turn_instructions()
            # if turn == 4:
            #     direction = "backwards"
            #     print("\nDirection changed to Backwards\n")
            # elif turn == 5:
            #     direction = "forwards"
            #     print("\nDirection changed to Forwards\n")
            # elif turn == 6:
            #     steering_type = "gyro"
            #     print("\nSteering changed to Gyro\n")
            
            
            
else:
    brick.light(Color.RED)
    brick.sound.file(SoundFile.ERROR,volume=100)