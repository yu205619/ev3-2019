#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick
from pybricks.parameters import Button

class ButtonMenu:
	def __init__(self):
		# in format {Button: (function, (args))}
		self.programs = {x: (None,()) for x in [Button.LEFT,Button.RIGHT,Button.UP,Button.DOWN]}
	def set(button,function,args=()):
		self.programs[button][0] = function
		self.programs[button][1] = args
	def run(self):
		while True:
			# wait for button
			while True:
				buttons = ev3brick.buttons()
				if any(buttons):
					# a button is pressed
					if self.programs[buttons[0]][0]:
						self.programs[buttons[0]][0](*self.programs[buttons[0]][1])
