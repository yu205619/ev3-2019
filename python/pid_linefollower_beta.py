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
robot_speed = 100

kp = 0.7
ki = 0
kd = 0.2

print("robot_speed:",robot_speed)
print("kp:",kp,"ki:",ki,"kd",kd)

target_brightness = 40

total_error = 0
last_error = 0
#[degrees(clockwise),detect/turn,reset]
turns = [[30,False,"detect"],[0,False,"detect"],[-30,False,"detect"],[0,False,"detect"],[0,True,"turn",-300]]
angle_error = 10

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

brick.sound.beep()

gyro.reset_angle(0)
if abs(gyro.speed()) > 0:
    leave_base = False
    print("Gyro Drifting")

if leave_base:
    # while len(turns) > 0:
    while True:
        #the steering
        reflection_reading = left_color_sensor.reflection()
        error = target_brightness - reflection_reading
        pid = kp * error + ki * total_error + kd * last_error
        print("reflection: "+str(round(reflection_reading,1)),"gyro: "+str(round(gyro.angle(),1)),"p: "+str(round(error*kp,1)),"i: "+str(round(total_error*ki,1)),"d: "+str(round(last_error*kd,1)),"pid: "+str(round(pid,1)))
        base.drive(robot_speed,pid*-1)

        #set pid for next time
        total_error += error
        last_error = error

        #turning
        if gyro.angle() > turns[turn][0] - angle_error and gyro.angle() < turns[turn][0] + angle_error:
            print("\nTurning Turn:",turns[turn],", Turn Count:",turn,"\n")
            if turns[turn][2] == "turn":
                tank.spin(turns[turn][3],100)
            if turns[turn][1]:
                gyro.reset_angle(0)
            turn += 1
            
else:
    brick.light(Color.RED)
    brick.sound.file(SoundFile.ERROR,volume=100)