class Restaurant():
	def __init__(self, restaurant_name, cousine_type):
		self.name = restaurant_name
		self.type = cousine_type
		self.number_served = 0

	def describe_restaurant(self):
		print('{} is {} cousine and with very tasty food'.format(self.name.title(), self.type))

	def open_restaurant(self):
		print('The restaurant {} is open now'.format(self.name.title()))

	def set_served_number(self, ilosc_klientow):
		self.number_served = ilosc_klientow

	def read_served_number(self):
		print('The restaurant obsługuje {} klientów'.format(self.number_served))

	def increment_served_number(self, inc_klients):
		self.number_served += inc_klients