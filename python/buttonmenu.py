#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick
from pybricks.parameters import Button

class ButtonMenu:
	def __init__(self):
		# in format {Button: (function, (args))}
		self.programs = {x: ["",None,()] for x in [Button.LEFT,Button.RIGHT,Button.UP,Button.DOWN]}
	def set(self,button,function,args=(),name="untitled"):
		if button == Button.CENTER: raise ValueError("button is disallowed -yu205619") # Button.CENTER is NOT allowed for undisclosed reasons
		self.programs[button][0] = name
		self.programs[button][1] = function
		self.programs[button][2] = args
	def run(self):
		self.display()
		# wait for button
		while True:
			buttons = ev3brick.buttons()
			if any(buttons) and buttons[0] in self.programs:
				# a button is pressed
				if self.programs[buttons[0]][1]: # ensure program is not None
					self.programs[buttons[0]][1](*self.programs[buttons[0]][2]) # program(args)
					# redraw screen after function is run
					self.display()
	def display(self):
		# 11 chars per space
		ev3brick.display.clear()
		for btn,loc in { # buttons paired with location on screen
			Button.LEFT: (0,70),
			Button.RIGHT: (90,70),
			Button.UP: (45,10),
			Button.DOWN: (45,125)
		}.items():
			ev3brick.display.text(
				"{:^11.11}".format(self.programs[btn][0]), # name of program
				loc)
