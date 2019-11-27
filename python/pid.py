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

        self.error = 0
        self.total_error = 0
        self.last_error = 0
    
    #Port.B,Port.C,56,102,Port.S2
    def port_init(left_motor,right_motor,wheel_size,axle_distance,gyro_sensor,self):
        self.base = DriveBase(Motor(left_motor),Motor(right_motor),wheel_size,axle_distance)
        self.gyro_sensor = GyroSensor(gyro_sensor)
    
    def line_follow_align_left(self):
        reflection_reading = self.left_color_sensor.reflection()
        self.error = self.target_brightness - reflection_reading
        pid = self.kp * self.error + self.ki * self.total_error + self.kd * self.last_error
        print(str.ljust("reflection: "+str(reflection_reading),20),str.ljust("error: "+str(error),20),str.ljust("pid: "+str(pid),20))
        base.drive(100,pid*-1)

        #set pid for next time
        self.total_error += self.error
        self.last_error = self.error
    
    def line_follow_align_right(self):
        reflection_reading = self.left_color_sensor.reflection()
        self.error = self.target_brightness - reflection_reading
        pid = self.kp * self.error + self.ki * self.total_error + self.kd * self.last_error
        print(str.ljust("reflection: "+str(reflection_reading),20),str.ljust("error: "+str(error),20),str.ljust("pid: "+str(pid),20))
        base.drive(100,pid*-1)

        #set pid for next time
        self.total_error += self.error
        self.last_error = self.error

    def drive_until_turn(self):
        pass

    def drive_until_time(self):
        pass

    def turn(self):
        pass

    def 