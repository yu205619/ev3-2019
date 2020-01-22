#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

#from tank import Tank

def turn_instructions():
    global direction
    if turn == 4:
        print("\nEpic Backwards Moment\n")
        direction = "backwards"
    elif turn == 5:
        print("\nEpic Forwards Moment\n")
        direction = "forwards"

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S4)
left_color_sensor = ColorSensor(Port.S2)
wheel_size = 56
axle_distance = 120
base = DriveBase(left_motor,right_motor,wheel_size,axle_distance)
#tank = Tank(gyro,left_motor,right_motor,wheel_size,axle_distance)

robot_speed = 70

def timed_pid(run_time):
    #degrees per second?

    kp = 0.5
    ki = 0
    kd = 0.1

    print("robot_speed:",robot_speed)
    print("kp:",kp,"ki:",ki,"kd",kd)

    target_brightness = 40

    total_error = 0
    last_error = 0
    #[degrees(clockwise),reset_gyro,detect/turn,<turn degrees(clockwise)>]
    #turns:
    #1-4 = curve
    #5 = reverse + detect
    #6 = go forwards
    turns = [[20,False,"detect"],[0,False,"detect"],[-20,False,"detect"],[0,False,"detect"],[-20,False,"detect"],[-20,False,"detect"]]
    angle_error = 10
    reflection_error = 10
    leave_base = True
    turn = 0

    direction = "forwards"

    brick.sound.beep()

    # gyro.reset_angle(0)
    # if abs(gyro.speed()) > 0:
    #     leave_base = False
    #     print("Gyro Drifting. Drift:",gyro.speed())

    if leave_base:
        # start timer
        timer = StopWatch()
        timer.reset()
        # while len(turns) > 0:
        while timer.time() < run_time:
            #check timer for time
            #the steering
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

            #set pid for next time
            total_error += error
            last_error = error                
    else:
        brick.light(Color.RED)
        brick.sound.file(SoundFile.ERROR,volume=100)


def gyro_timed(run_time,robot_speed,reset=False):
    timer = StopWatch()
    timer.reset()
    # while len(turns) > 0:
    while timer.time() < run_time:
        base.drive(robot_speed,gyro.angle()*-1)
    if reset:
        gyro.reset_angle(0)
    #TODO: stuff
    pass

gyro.reset_angle(0)
gyro_timed(3000,120)
while gyro.angle() == 0:
    base.drive(robot_speed,gyro.angle()*-1)
timed_pid(9000)
gyro_timed(2000,120)
timed_pid(1000)



