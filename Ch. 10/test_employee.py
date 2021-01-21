import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for employee.py"""

	def setUp(self):
		"""Create an instance of an example employee."""
		self.example_employee = Employee('john', 'doe', 80000)	

	def test_give_default_raise(self):
		"""Test giving the default raise."""
		self.example_employee.give_raise()
		self.assertEqual(self.example_employee.salary, 85000)

	def test_give_custom_raise(self):
		"""Test giving a non-default raise, in this case 2500."""
		self.example_employee.give_raise(2500)
		self.assertEqual(self.example_employee.salary, 82500)

if __name__ =='__main__':
	unittest.main()