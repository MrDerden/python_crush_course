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

class Privilegies():
	def __init__(self, privilegies = ['Moze komietować', 'Może usuwać uzytkowników', 'Może dodawać użytkowników']):
		self.privilegies = privilegies
	def show_privileges(self):
		print(' jest administratorem i ma przywileje: ' + str(self.privilegies))	

class Admin(User):
	def __init__(self, first_name, last_name, sex, work):
		super().__init__(first_name, last_name, sex, work)
		self.user_privilegies = Privilegies()

	def admin_privileges(self):
		print('{} {} {}'.format(self.first_name.title(), self.last_name.title(), self.user_privilegies.privilegies) )