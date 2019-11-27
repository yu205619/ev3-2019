#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class LineFollower:
    #40,[[70,30],[10,-30],[10,-30]],5
    def __init__(target_brightness = 40,turns = [],turn_brightness_variation = 5,self):
        self.kp = 1
        self.ki = 1
        self.kd = 1
        self.target_brightness = target_brightness
        self.turns = turns
        self.turn_brightness_variation = turn_brightness_variation
    
    #Port.B,Port.C,56,102
    def motor_init(left_motor,right_motor,wheel_size,axle_distance,self)
        self.base = DriveBase(Motor(left_motor),Motor(right_motor),wheel_size,axle_distance)

    #
    def sensor_init(left_color_sensor = None,right_color_sensor = None,gyro_sensor = None,middle_color_sensor = None)
        self.left_color_sensor = ColorSensor(left_color_sensor)
        self.right_color_sensor = ColorSensor(right_color_sensor)
        self.middle_color_sensor = ColorSensor(middle_color_sensor)
        self.gyro_sensor = GyroSensor(gyro_sensor)