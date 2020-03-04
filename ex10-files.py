#10-1

filename = 'inpython.txt'

with  open(filename) as file_object:
	content = file_object.read()
	print(content)

with open(filename) as file_object:
	read_lines = file_object.readlines()
	for line in read_lines:
		#print(line.rstrip())
		print(line.replace("python", "C").rstrip()) #10-2

with open(filename) as file_object:
	read_lines = file_object.readlines()

lines_from_file = ''
for line in read_lines:
	lines_from_file += line.rstrip()

print(lines_from_file)
print(len(lines_from_file))

#10-3

# user_name = input("Write your name: ")

# with open('guest.txt', 'w') as file_with_name:
# 	file_with_name.write(user_name)

#10-4

# user_name = ''
# while user_name != 'q':
# 	user_name = input("Enter your name: ")
# 	message = "Hi" + user_name.title()
# 	print(message)
# 	with open('guest.txt', 'a') as guest_book:
# 		guest_book.write(message + '\n')

#10-6 , 10-7

# j = True
# while j:
# 	first_num = input("Enter first number: ")
# 	if first_num == 'q':
# 		break
# 	second_num = input("Enter second number: ")
# 	if second_num == 'q':
# 		break
# 	try:
# 		sum = int(first_num) + int(second_num)
# 	except TypeError:
# 		print("Some data is not a number")
# 	except ValueError:
# 		print("Some data is not a number")
# 	else:
# 		print(sum)
# 		j = False

#10-8

def read_file(filename):
	try:
		with open(filename) as f_obj:
			content = f_obj.read()
	except FileNotFoundError:
		pass # 10-9
		#print("File does not exist")
	else:	
		print(content)

file_list = ['cats1.txt', 'dogs.txt']

for file in file_list:
	read_file(file)

#10-10

booknames = ["Sketches1 of Gotham.txt", "gazdagok.txt"]

def find_words_in(filename, word):
	try:
		with open(filename) as f_obj:
			content = f_obj.read()
	except FileNotFoundError:
		print("file {} not found".format(filename))
	else:
		print("In file {} there are {} words '{}'".format(filename, content.lower().count(word), word))

for bookname in booknames:
	find_words_in(bookname, "the")

#10-11
import json

# fav_num = 5

# filename = 'fav_num.json'
# with open(filename, 'w') as f_obj:
# 	json.dump(fav_num, f_obj)

# with open(filename) as f_obj:
# 	user_num = json.load(f_obj)
# 	print(user_num)

#10-12

# def add_user_num():
# 	filename = 'fav_num1.json'
# 	fav_num = 5
# 	with open(filename, 'w') as f_obj:
# 		json.dump(fav_num, f_obj)
# 		return fav_num 

# def get_user_num():
# 	filename = 'fav_num1.json'
# 	try:
# 		with open(filename) as f_obj:
# 			user_num = json.load(f_obj)
# 	except FileNotFoundError:
# 		return None
# 	else:
# 		return user_num

# def show_nr():
# 	user_num = get_user_num()
# 	if user_num:
# 		print("Your num is " + str(user_num))
# 	else:
# 		user_num = add_user_num()
# 		print("We will remember number " + str(user_num))

# show_nr()

#10-13

def add_user_name():
	filename = 'usr_name.json'
	user_name = input("write your name: ")
	with open(filename, 'w') as f_obj:
		json.dump(user_name, f_obj)
		return user_name

def get_user_name():
	filename = 'usr_name.json'
	try:
		with open(filename) as f_obj:
			user_name = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return user_name

def show_user_name():
	user_name = get_user_name()
	if user_name:
		question = input("Your name is " + user_name.title() + "? ")
		if question == "yes":
			print("Hi " + user_name.title())
		else:
			user_name = add_user_name()
			print("We will add your name, " + user_name.title())
	else:
		user_name = add_user_name()
		print("We will remember you, " + user_name.title())

show_user_name()