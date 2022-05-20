import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.FakeMotor import Motor

class TestMotor(unittest.TestCase):

	def setUp(self):
		self.motor = Motor()
		self.motor.moveHome()
		self.maxSpeed = self.motor.getVelocityParamsLimits().speed
		self.maxAcceleration = self.motor.getVelocityParamsLimits().acc

	def testImportMotor(self):
		self.assertIsNotNone(Motor)

	def testCreateMotorInstance(self):
		self.assertIsNotNone(self.motor)


	def testMoveToWithValidParams(self):
		self.motor.moveTo(10, waitUntil=True)
		self.motor.moveTo(-10)
		self.assertTrue(True)

	def testMoveToWithWrongθType(self):
		self.assertRaises(TypeError, self.motor.moveTo, "20")

	def testMoveToWithWrongWaitUntilType(self):
		self.assertRaises(TypeError, self.motor.moveTo, 20, "False")

	def testMoveToWithOutRange(self):
		self.assertRaises(ValueError, self.motor.moveTo, 190)


	def testMoveByWithValidParams(self):
		self.motor.moveBy(20)
		self.assertTrue(True)

	def testMoveByWithWrongθType(self):
		self.assertRaises(TypeError, self.motor.moveBy, "20")

	def testMoveByWithWrongWaitUntilType(self):
		self.assertRaises(TypeError, self.motor.moveBy, 20, "True")


	def testMoveHomeWithValidParams(self):
		self.motor.moveHome(waitUntil=True)
		self.assertTrue(True)

	def testMoveHomeWithWrongWaitUntilType(self):
		self.assertRaises(TypeError, self.motor.moveHome, waitUntil="True")


	def testGetVelocityParamsLimitsReturnType(self):
		params = self.motor.getVelocityParamsLimits()
		self.assertEqual(str(type(params)), "<class 'Model.FakeMotor.MotorParams'>")

	def testGetVelocityParamsLimitsReturnAccType(self):
		params = self.motor.getVelocityParamsLimits()
		self.assertEqual(type(params.acc), float)

	def testGetVelocityParamsLimitsReturnSpeedType(self):
		params = self.motor.getVelocityParamsLimits()
		self.assertEqual(type(params.speed), float)


	def testGetVelocityParamsReturnType(self):
		params = self.motor.getVelocityParamsLimits()
		self.assertEqual(str(type(params)), "<class 'Model.FakeMotor.MotorParams'>")

	def testGetVelocityParamsReturnAccType(self):
		params = self.motor.getVelocityParams()
		self.assertEqual(type(params.acc), float)

	def testGetVelocityParamsReturnSpeedType(self):
		params = self.motor.getVelocityParams()
		self.assertEqual(type(params.speed), float)


	def testSetVelocityParamsWithValidParams(self):
		self.motor.setVelocityParams(self.maxAcceleration, self.maxSpeed)
		self.assertTrue(True)

	def testSetVelocityParamsWithWrongAccType(self):
		self.assertRaises(TypeError, self.motor.setVelocityParams, "20", self.maxSpeed)

	def testSetVelocityParamsWithWrongSpeedType(self):
		acc = self.maxAcceleration
		speed = "20"
		self.assertRaises(TypeError, self.motor.setVelocityParams, acc, speed)

	def testSetVelocityParamsWithOutOfRangeAcc(self):
		acc = self.maxAcceleration + 1.0
		speed = self.maxSpeed
		self.assertRaises(ValueError, self.motor.setVelocityParams, acc, speed)

	def testSetVelocityParamsWithOutOfRangeSpeed(self):
		acc = self.maxAcceleration
		speed = self.maxSpeed + 1.0
		self.assertRaises(ValueError, self.motor.setVelocityParams, acc, speed)

	def testSetVelocityParamsWithNegativeAcc(self):
		acc = -self.maxAcceleration
		speed = self.maxSpeed
		self.assertRaises(ValueError, self.motor.setVelocityParams, acc, speed)

	def testSetVelocityParamsWithNegativeSpeed(self):
		acc = self.maxAcceleration
		speed = -self.maxSpeed
		self.assertRaises(ValueError, self.motor.setVelocityParams, acc, speed)

if __name__ == "__main__":
	unittest.main()