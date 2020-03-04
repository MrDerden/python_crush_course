#9-1 restaurant
"""
class Restaurant():
	def __init__(self, restaurant_name, cousine_type):
		self.name = restaurant_name
		self.type = cousine_type

	def describe_restaurant(self):
		print('{} is {} cousine and with very tasty food'.format(self.name.title(), self.type))

	def open_restaurant(self):
		print('The restaurant {} is open now'.format(self.name.title()))

restaurant = Restaurant('Chaczapucza', 'georgian')
print('Restaurant {} is {}'.format(restaurant.name.title(), restaurant.type))
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-1 three restaurants
no_problem = Restaurant('No Problem', 'vegan')
print('Restaurant {} is {} restaurant'.format(no_problem.name.title(), no_problem.type))

lokal = Restaurant('Lokal Vegan Bistro', 'vegan')
print('Restaurant {} is {} restaurant'.format(lokal.name.title(), lokal.type))

sahara = Restaurant('Sahara', 'kebab')
print('Restaurant {} is {} restaurant'.format(sahara.name.title(), sahara.type))
"""
"""
#9-2 USER
class User():
	def __init__(self, first_name, last_name, sex, work):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.work = work

	def about_user(self):
		print('{} {} is a {} and he/she is working like a {}'.format(self.first_name.title(), self.last_name.title(), self.sex, self.work))

	def hi_user(self):
		print('Hello, {} {}'.format(self.first_name.title(), self.last_name.title()))

qwerty = User('John', 'doe', 'male', 'hacker')
qwerty.about_user()
qwerty.hi_user()

lisa = User('Elizabeth', 'Taylor', 'female', 'actres')
lisa.about_user()
lisa.hi_user()

gniloy = User('Roman', 'Gnilanski', 'male', 'drummer')
gniloy.about_user()
gniloy.hi_user()
"""
#9-4
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

restaurant = Restaurant('Au lak', 'chineese')
print('Restauracja {} obsługuję {} klientów'.format(restaurant.name, restaurant.number_served))
restaurant.number_served = 32
print('Restauracja {} obsługuję {} klientów'.format(restaurant.name, restaurant.number_served))
restaurant.set_served_number(5)
restaurant.read_served_number()
restaurant.increment_served_number(10)
restaurant.read_served_number()

#9-5
class User():
	def __init__(self, first_name, last_name, sex, work):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.work = work
		self.login_attempts = 0

	def about_user(self):
		print('{} {} is a {} and he/she is working like a {}'.format(self.first_name.title(), self.last_name.title(), self.sex, self.work))

	def hi_user(self):
		print('Hello, {} {}'.format(self.first_name.title(), self.last_name.title()))

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def show_login_attempts(self):
		print('Loggin attemps: {}'.format(self.login_attempts))

qwerty = User('John', 'doe', 'male', 'hacker')
qwerty.about_user()
qwerty.hi_user()
qwerty.show_login_attempts()

lisa = User('Elizabeth', 'Taylor', 'female', 'actres')
lisa.about_user()
lisa.hi_user()
lisa.increment_login_attempts()
lisa.show_login_attempts()
lisa.reset_login_attempts()
print(lisa.login_attempts)

gniloy = User('Roman', 'Gnilanski', 'male', 'drummer')
gniloy.about_user()
gniloy.hi_user()

#9-6

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cousine_type):
		super().__init__(restaurant_name, cousine_type)
		self.flavours = ['vanilowy', 'czokoladowy', 'karmelowy']
	def describe_stand(self):
		print('The flavours are: ' + str(self.flavours))

vegie_lody = IceCreamStand('Vegie Lody', 'vegan')
vegie_lody.describe_restaurant()
vegie_lody.describe_stand()

#9-7
class Privilegies():
	def __init__(self, privilegies = ['Moze komietować', 'Może usuwać uzytkowników', 'Może dodawać użytkowników']):
		self.privilegies = privilegies
	def show_privileges(self):
		print(' jest administratorem i ma przywileje: ' + str(self.privilegies))	

class Admin(User):
	def __init__(self, first_name, last_name, sex, work):
		super().__init__(first_name, last_name, sex, work)
		self.user_privilegies = Privilegies()

admin = Admin('Roman', 'Gnilanski', 'male', 'syadmin')
admin.user_privilegies.show_privileges()

#9-8 electric car

class Car():
#"""Простая модель автомобиля."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles

class ElectricCar(Car):
#"""Представляет аспекты машины, специфические для электромобилей."""

	def __init__(self, make, model, year):
#"""Инициализирует атрибуты класса-родителя."""
		super().__init__(make, model, year)
		self.battery = Battery()

class Battery():
#"""Простая модель аккумулятора электромобиля."""
	def __init__(self, battery_size=70):
#"""Инициализирует атрибуты аккумулятора."""
		self.battery_size = battery_size
	def describe_battery(self):
#"""Выводит информацию о мощности аккумулятора."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
		else:
			print('OK')

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
