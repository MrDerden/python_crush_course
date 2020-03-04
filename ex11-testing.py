import unittest
from city_function import get_city_country

class CityTestCase(unittest.TestCase):

	def test_city_country(self):
		formatted_view = get_city_country("milano", "italy")
		self.assertEqual(formatted_view, "Milano, Italy")

unittest.main()