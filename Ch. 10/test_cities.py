import unittest

from city_functions import format_city

class CitiesTestCase(unittest.TestCase):
	"""Tests for city_functions.py"""

	def test_city_country(self):
		"""Test cities like Oslo, Norway."""
		city_country = format_city('oslo', 'norway')
		self.assertEqual(city_country, 'Oslo, Norway')

	def test_city_country_population(self):
		"""Tests cities with population included."""
		city_country_population = format_city('edinburgh', 'scotland', 482000)
		self.assertEqual(city_country_population,
			'Edinburgh, Scotland - population 482000')

if __name__ == '__main__':
	unittest.main()