import thorlabs_apt as apt
from typing import NamedTuple

class MotorParams(NamedTuple):
	acc: float = None
	speed: float = None

class Motor:
	def __init__(self):
		try:
			self.id = apt.list_available_devices()[0][1]
			self.motor = apt.Motor(self.id)
			self.maxAcc = self.getVelocityParamsLimits().acc
			self.maxSpeed = self.getVelocityParamsLimits().speed
		except:
			raise RuntimeError("no motor detected")

	def moveTo(self, θ, waitUntil=True):
		if type(θ) is not float and type(θ) is not int:
			raise TypeError("θ parameter is not float or int")
		if type(waitUntil) is not bool:
			raise TypeError("waitUntil parameter is not bool")
		if θ > 180 or θ < -180:
			raise ValueError("θ is out of range (-180 to 180)")
		self.motor.move_to(θ, blocking=waitUntil)

	def moveBy(self, θ, waitUntil=True):
		if type(θ) is not float and type(θ) is not int:
			raise TypeError("θ parameter is not float or int")
		if type(waitUntil) is not bool:
			raise TypeError("waitUntil parameter is not bool")
		self.motor.move_by(θ, blocking=waitUntil)

	def moveHome(self, waitUntil=True):
		if type(waitUntil) is not bool:
			raise TypeError("waitUntil parameter is not bool")
		self.motor.move_home(blocking=waitUntil)

	def getVelocityParams(self):
		params = self.motor.get_velocity_parameters()[1:]
		return MotorParams(params[0], params[1])

	def setVelocityParams(self, acceleration, speed):
		if type(acceleration) is not float and type(acceleration) is not int:
			raise TypeError("acceleration parameter is not float or int")
		if type(speed) is not float and type(speed) is not int:
			raise TypeError("acceleration parameter is not float or int")
		if acceleration > self.maxAcc:
			raise ValueError(f"max value for acceleration is {self.maxAcc}")
		if speed > self.maxSpeed:
			raise ValueError(f"max value for speed is {self.maxSpeed}")
		if acceleration < 0:
			raise ValueError("acceleration value can't be negative")
		if speed < 0:
			raise ValueError("speed value can't be negative")
		self.motor.set_velocity_parameters(0, acceleration, speed)

	def getVelocityParamsLimits(self):
		params = self.motor.get_velocity_parameter_limits()
		return MotorParams(params[0], params[1])
