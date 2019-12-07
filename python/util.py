class Comparator:
	LESS = -1
	MORE = 1
	EQUAL = 0
	def _lambda(comparator):
		if comparator == self.LESS:
			return lambda val, thr: val < thr
		elif comparator == self.MORE:
			return lambda val, thr: val > thr
		else:
			return lambda val, thr: val == thr

def wait_gyro(gyro,comparator,deg,interval=1):
	test = Comparator._lambda(comparator)
	while not test(gyro.angle(),deg):
		wait(interval)
	return True

def wait_reflection(sensor,comparator,percent,interval=1):
	test = Comparator._lambda(comparator)
	while not test(sensor.reflection(),percent):
		wait(interval)
	return True

