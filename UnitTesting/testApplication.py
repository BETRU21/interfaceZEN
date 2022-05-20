import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Control.Application import App
from Model.FakeZenControl import Zen
from Model.FakeMotor import Motor

class TestApp(unittest.TestCase):

	def setUp(self):
		self.app = App(Zen(), Motor())

	def testImportApp(self):
		self.assertIsNotNone(App)

	def testCreateAppInstance(self):
		self.assertIsNotNone(self.app)

if __name__ == "__main__":
	unittest.main()