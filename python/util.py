from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Comparator:
    LESS = -1
    MORE = 1
    EQUAL = 0
    def ismore(val,thr):
        return val > thr
    def isless(val,thr):
        return val < thr
    def isequal(vavl,thr):
        return val == thr
    def _lambda(comparator):
        if comparator == Comparator.LESS:
            return Comparator.isless
        elif comparator == Comparator.MORE:
            return Comparator.ismore
        else:
            return Comparator.isequal

def wait_gyro(gyro,comparator,deg):
    test = Comparator._lambda(comparator)
    while not test(gyro.angle(),deg):
        pass
    return True

def wait_reflection(sensor,comparator,percent):
    test = Comparator._lambda(comparator)
    while not test(sensor.reflection(),percent):
        pass
    return True