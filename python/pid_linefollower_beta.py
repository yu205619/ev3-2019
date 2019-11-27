#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

kp = 1
ki = 1
kd = 1

target_brightness = 40

total_error = 0
last_error = 0
#turns = [target_brightness,turn_degrees(clockwise)]
turns = [[70,30],[10,-30],[10,-30]]
turn_brightness_variation = 5

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S2)
left_color_sensor = ColorSensor(Port.S1)
wheel_size = 56
axle_distance = 102
base = DriveBase(left_motor,right_motor,wheel_size,axle_distance)
watch = StopWatch()
leave_base = True

brick.sound.beep()

gyro.reset_angle(0)
if abs(gyro.speed()) > 0:
    leave_base = False

if leave_base:
    while watch.time() < 5000:
        #the steering
        reflection_reading = left_color_sensor.reflection()
        error = target_brightness - reflection_reading
        pid = kp * error + ki * total_error + kd * last_error
        print(str.ljust("reflection: "+str(reflection_reading),20),str.ljust("error: "+str(error),20))
        base.drive(100,pid*-1)

        #set pid for next time
        total_error += error
        last_error = error

        #turning
        if reflection_reading >= turns[0][1] - turn_brightness_variation and reflection_reading <= turns[0][1] + turn_brightness_variation:
            base.drive(100,turns[0][1])
            turns.pop(0)
else:
    display.image(ImageFile.DECLINE,alignment=Align.CENTER,coordinate=None,clear=True)
    brick.light(Color.RED)
    sound.file(SoundFile.ERROR,volume=100)