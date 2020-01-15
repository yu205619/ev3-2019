#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from tank import Tank

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S4)
left_color_sensor = ColorSensor(Port.S2)
wheel_size = 56
axle_distance = 120
base = DriveBase(left_motor,right_motor,wheel_size,axle_distance)
watch = StopWatch()

tank = Tank(gyro,left_motor,right_motor)

while True:
    base.drive(100,100)

tank.spin(360,100)