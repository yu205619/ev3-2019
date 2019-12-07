import util

import pybricks.robotics

class Tank(pybricks.robotics.DriveBase):
	def __init__(self,gyro,left_motor,right_motor,wheel_diameter=56,axle_track=114):
		super().__init__(left_motor,right_motor,wheel_diameter,axle_track)
		self.gyro = gyro
	def spin(self,angle,power):
		if angle == 0: return
		# start spinning in direction and waiting for gyro
		self.gyro.reset_angle()
		if deg < 0:
			self.left_motor.run(-power)
			self.right_motor.run(power)
			wait_gyro(self.gyro,Comparator.LESS,angle)
			self.stop()
		else:
			self.left_motor.run(power)
			self.right_motor.run(-power)
			wait_gyro(self.gyro,Comparator.MORE,angle)
			self.stop()
