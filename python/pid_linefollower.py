#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

kp = 1
ki = 0
kd = 1

target_brightness = 40

total_error = 0
last_error = 0
turn_count = 0
#turns = [target_brightness,turn_degrees(clockwise)]
turns = [[20,-30]]

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S2)
wheel_size = 56
axle_distance = 102
base = DriveBase(left_motor,right_motor,wheel_size,axle_distance)
watch = StopWatch()

left_color_sensor = ColorSensor(Port.S1)

brick.sound.beep()

while watch.time() < 5000:
    reflection_reading = left_color_sensor.reflection()
    error = target_brightness - reflection_reading
    pid = kp * error + ki * total_error + kd * last_error
    print("reflection:",reflection_reading,"\t\terror:",error)
    base.drive(100,pid*-1)

    total_error += error
    last_error = error

    if reflection_reading == turns[0][1]:
        base.drive(100,turns[0][1])