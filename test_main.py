import unittest

from main import page01
class MainTest(unittest.TestCase):
	def test_value(self):
		result = page01()
		self.assertEqual("<h2>This is page 1</h2>", result)

'''
test on weather

from main import weather
class MainTest(unittest.TestCase):
	def test_value(self):
		result = weather()
		self.assertEqual("London", result)
'''