#!/usr/bin/env pybricks-micropython

# sample functions start
import time
from pybricks.parameters import Button
from pybricks.parameters import Color
from pybricks import ev3brick
def wait_time(zeit):
	time.sleep(zeit)
def cool_lights():
	ev3brick.light(Color.RED)
	time.sleep(1)
	ev3brick.light(Color.BLACK)
def text(first,second):
	print("{}:{}".format(first,second))
	time.sleep(1)
def scream():
	ev3brick.sound.beep()
	time.sleep(1)
# sample functions end



## USAGE
# import the module
from buttonmenu import ButtonMenu
# create ButtonMenu object
runmenu = ButtonMenu()
# set button actions:
# <ButtonMenu object>.set( <Button>, <function>, <function arguments as tuple>, <name> )
runmenu.set(Button.LEFT,wait_time,(10,),"wait") # for single arguments, add trailing comma
runmenu.set(Button.RIGHT,cool_lights,(),"lights")
runmenu.set(Button.UP,text,(100,12)) # name defaults to "untitled"
runmenu.set(Button.DOWN,scream,name="scream") # arguments defaults to empty
runmenu.run()
