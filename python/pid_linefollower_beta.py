#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

kp = 0.7 #error
ki = 0 #last_error
kd = 0 #total_error

#degrees per second?
robot_speed = 100

target_brightness = 40

total_error = 0
last_error = 0
#turns = [target_brightness,turn_degrees(clockwise)]
#turns = [[90,0],[10,-60]]
turns = [0]
turn_brightness_variation = 5

anomaly_count = 0
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S4)
left_color_sensor = ColorSensor(Port.S2)
wheel_size = 56
axle_distance = 120
base = DriveBase(left_motor,right_motor,wheel_size,axle_distance)
watch = StopWatch()
leave_base = True

brick.sound.beep()

# gyro.reset_angle(0)
# if abs(gyro.speed()) > 0:
#     leave_base = False

if leave_base:
    # while len(turns) > 0:
    while True:
        #the steering
        reflection_reading = left_color_sensor.reflection()
        error = target_brightness - reflection_reading
        pid = kp * error + ki * total_error + kd * last_error
        print("reflection: "+str(round(reflection_reading,1)),"p: "+str(round(error*kp,1)),"i: "+str(round(total_error*ki,1)),"d: "+str(round(last_error*kd,1)),"pid: "+str(round(pid,1)))
        base.drive(robot_speed,pid*-1)

        #set pid for next time
        total_error += error
        last_error = error

        #turning
        #if reflection_reading >= turns[0][1] - turn_brightness_variation and reflection_reading <= turns[0][1] + turn_brightness_variation:
        #    anomaly_count += 1
        #    base.drive(180,turns[0][1])
        #    if anomaly_count == 1:
        #        base.drive(robot_speed,0)
        #    print("turning turn",turns[0])
        #    brick.sound.file(SoundFile.FANFARE,volume=30)
        #    turns.pop(0)
else:
    brick.light(Color.RED)
    brick.sound.file(SoundFile.ERROR,volume=100)