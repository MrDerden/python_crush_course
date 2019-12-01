#5-1
"""car = input("Print car name\n")
if (car == "subaru") and (car == "porsche") and (car == "mercedes") and (car == "honda") and (car == "heundai"):
	print(True)
elif (car == "audi") and (car == "opel") and (car == "renault") and (car == "peugeot") and (car == "fiat"):
	print(False)
else:
	print(False)"""

#5-2
list1 = ["rabbit", "fox"]
list2 = ["rabbit", "perrot"]
if list1 == list2:
	print(True)
else:
	print(False)
"""
names = ["Roman", "bill", "John"]
nick = input("write your name\n")
for name in names:
	if nick.lower() == name.lower():
		print(nick.title() + ", you can write a comment")
else:
	print("Access denied")

age = input("What your age?\n")
age = int(age)
if age < 18 and age != 17:
	print("You are too young")
elif age >= 18 and age <=99:
	print("Enjoy porno")
elif age == 100 or age == 17:
	print("you have age bonus")
else:
	print("Access denied")
"""
#5-3
alien_color = "red"
if "green" in alien_color:
	print("You get 5 points")
elif alien_color == "red":
	print("You are losing 10 points")

#5-4
color = "red"
if color == "green":
	print("You get 5 pionts")
else:
	print("You get nothing")

#5-5
if alien_color == "green":
	print('You just get 5 points')
elif alien_color == "yellow":
	print('You just get 10 points')
elif alien_color == "red":
	print('You just get 15 points')

#5-6
age = 45
if age <2:
	print('child')
elif age >= 2 and age < 4:
	print('babbie')
elif age >=4 and age < 13:
	print('baby')
elif age == 13 or age < 20:
	print('teen')
elif age == 20 or age < 65:
	print('adult')
elif age >= 65:
	print('old')

#5-7
fruits = ['apple', 'orange', 'mango', 'pomelo', 'strawberry']
if 'apple' in fruits:
	print('Yuo are really like apples')
if 'coconut' in fruits:
	print('Yuo are really like cocnuts')
if 'mango' in fruits:
	print('Yuo are really like mangos')
if 'pomelo' in fruits:
	print('Yuo are really like pomelos')

fruits=['orange', 'grape', 'kiwi', 'apple', 'mango', 'fig', 'lemon']
newList = []
for fruit in fruits:
    newList.append(fruit.upper())
print(newList)

