#!/usr/bin/env pybricks-micropython

import buttonmenu

import time

from pybricks.parameters import Button
from pybricks.parameters import Color

from pybricks import ev3brick

def wait_time(time):
	time.sleep(time)

def cool_lights():
	ev3brick.light(Color.RED)
	time.sleep(1)

def move_tank(power,angle):
	print("moving the tank at power {} and angle {}".format(power,angle))
	time.sleep(1)

def scream():
	ev3brick.sound.beep()
	time.sleep(1)


# check this out
runmenu = ButtonMenu()
runmenu.set(Button.LEFT,wait_time,(10))
runmenu.set(Button.RIGHT,cool_lights,())
runmenu.set(Button.UP,move_tank,(100,12))
runmenu.set(Button.DOWN,scream)
