import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.FakeZenControl import Zen

class TestZen(unittest.TestCase):

	def setUp(self):
		self.zen = Zen()

	def testImportZen(self):
		self.assertIsNotNone(Zen)

	def testCreateZenInstance(self):
		self.assertIsNotNone(self.zen)

if __name__ == "__main__":
	unittest.main()