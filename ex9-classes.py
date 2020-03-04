#9-1

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print('{} is {}'.format(self.restaurant_name.title(), self.cuisine_type))

	def open_restaurant(self):
		print("{} is open".format(self.restaurant_name.title()))

	def set_number_served(self, set_number):
		self.number_served = set_number
		print("{} served {} clients". format(self.restaurant_name.title(), self.number_served))

	def increment_number_served(self, increment_number):
		self.number_served += increment_number
		print("{} served {} clients a day".format(self.restaurant_name.title(), self.number_served))


restaurant = Restaurant("aulak", "chinese")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2

good_restaurant = Restaurant("Parana", "polish")
good_restaurant.describe_restaurant()

mediumclass_Restaurant = Restaurant("Tel Aviv", "Vegan")
mediumclass_Restaurant.describe_restaurant()

bad_restaurant = Restaurant("McDonalds", "fastfood")
bad_restaurant.describe_restaurant()

# 9-3

class User():
	def __init__(self, first_name, last_name, age, eye_color):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.eye_color = eye_color
		self.login_attempts = 0

	def describe_user(self):
		print("{} {} is {} and  he/she have/has {} eyes".format(self.first_name.title(), self.last_name.title(), str(self.age), self.eye_color))

	def greet_user(self):
		print("Hi {} {}!".format(self.first_name.title(), self.last_name.title()))

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

stalin = User("iosif", "stalin", 67, "no")
stalin.describe_user()
stalin.greet_user()

qwerty = User("John", "doe", 13, "green")
qwerty.describe_user()
qwerty.greet_user()

#9-4

restaurant = Restaurant("Sjhlem", "russian")
print(restaurant.number_served)
restaurant.set_number_served(25)
restaurant.increment_number_served(100)

#9-5

surik = User('Sasza', 'Belyj', 30, "blue")
surik.increment_login_attempts()
surik.increment_login_attempts()
surik.increment_login_attempts()
print(surik.login_attempts)
surik.reset_login_attempts()
print(surik.login_attempts)

#9-6

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavours = ['vanil', 'raspberry', 'coconut']

	def show_flavours(self):
		print("{} has ice cream with flovers:".format(self.restaurant_name.title()))
		for flavour in self.flavours:
			print(flavour)

lariok = IceCreamStand("ColdIce", "summer")
print(lariok.flavours)
lariok.show_flavours()

#9-7

# class Admin(User):
# 	def __init__(self, first_name, last_name, age, eye_color):
# 		super().__init__(first_name, last_name, age, eye_color)
# 		self.privilegies = Privilegies()

# admin = Admin("Igor", "Govor", 45, "green")
# print(admin.privilegies)
# admin.show_privilegies()

#9-8

class Privilegies():
	def __init__(self):
		self.privilegies_list = ["Add", "Delete", "View"] 

	def show_privilegies(self):
		print("Administrator, have privilegies:")
		for privilege in self.privilegies_list:
			print(privilege)

class Admin(User):
	def __init__(self, first_name, last_name, age, eye_color):
		super().__init__(first_name, last_name, age, eye_color)
		self.privilegies = Privilegies()

admin = Admin("Igor", "Govor", 45, "green")
print(admin.privilegies.privilegies_list)
admin.privilegies.show_privilegies()

#9-9

class Car():
	def __init__(self, model, year):
		self.model = model
		self.year = year

	def show_descriptive_name(self):
		print("This is {} of {} year".format(self.model.title(), self.year))

my_new_car = Car('Impresa', '2016')
my_new_car.show_descriptive_name()

class Battery():
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car have {} kWh battery".format(self.battery_size))

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
			print("Battery was upgraded")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		print("This car can go approximately {} km on full charge".format(str(range)))


class ElectricCar(Car):
	def __init__(self, model, year):
		super().__init__(model, year)
		self.battery = Battery()

my_tesla = ElectricCar('Tesla', '2019')
my_tesla.show_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#9-14
from random import randint

class Die():
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		rand_num = randint(1, self.sides)
		return rand_num

six_face_cube = Die()
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print(six_face_cube.roll_die())
print('___')
ten_face_cube = Die(10)
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print(ten_face_cube.roll_die())
print("---")
twenty_face_cube = Die(20)
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())
print(twenty_face_cube.roll_die())