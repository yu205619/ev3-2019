import util

Class Tank:
	def __init__(self,motor_left,motor_right,gyro):
		self.motor_left = motor_left
		self.motor_right = motor_right
		self.gyro = gyro
	def move(self,power):
		self.motor_left.run(power)
		self.motor_right.run(power)
	def stop(self):
		self.motor_left.stop()
		self.motor_right.stop()
	def spin(self,angle,power,gyro=self.gyro):
		if angle == 0: return
		# start spinning in direction and waiting for gyro
		gyro.reset_angle()
		if deg < 0:
			self.motor_left.run(-power)
			self.motor_right.run(power)
			wait_gyro(gyro,Comparator.LESS,angle)
			self.stop()
		else:
			self.motor_left.run(power)
			self.motor_right.run(-power)
			wait_gyro(gyro,Comparator.MORE,angle)
			self.stop()
