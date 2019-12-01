#7-1
#message = input('Jai samochód Pan chciał bym wypozyczyć?')
#print ('Zaraz zobaczę czy mammy na stanie ' + message.title())

#7-2
'''
seats = input('Na ile mejc jest potrzebny stół?\n')
if int(seats) >= 8:
	print('Przepraszam, ale trzeba poczekać')
else:
	print('Stół jest przygotowany')
'''

#7-3
'''
num = input('Enter a number\n')
if int(num) % 10 == 0:
	print('Number ' + str(num) + ' is devided by 10')
else:
	print(num + ' is not devidedby 10')
'''

#7-4
'''
prompt = 'Write what pizza do you want [or type "quit" to exit]\n'
pizza = ''
while pizza != 'quit':
	pizza = input(prompt)
	if pizza != 'quit':
		print(pizza.title() + ' was added to yor order')
'''

#7-5
'''
age = input('Wpisz swój wiek')
while not age.isdigit():
	age = input('Wpisz wiek liczbą')
age = int(age)
if age < 3:
	print('Free')
	
elif (age >= 3) and (age < 12):
	print('10$')
	
elif age >= 12:
	print('15$')
else:	
	print('x')

#7-6
prompt = 'Write what pizza do you want [or type "quit" to exit]\n'
active = True
pizza = ''
i = 0
while active:
	pizza = input(prompt)
	i += 1
	if (pizza != 'quit') and (i < 3):
		print(pizza.title() + ' was added to yor order')
	elif pizza == 'quit':
		break
	else:
		active = False
		print('Zaduzo dodatkow')
'''

#7-8
'''
sandwich_orders = ['cheese sandwich', 'tuna sandwich', 'hummus sandwich']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print('I made your ' + current_sandwich)
	finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)
'''

#7-9

sandwich_orders = ['cheese sandwich', 'pastrami sandwich', 'tuna sandwich', 'pastrami sandwich', 'hummus sandwich', 'pastrami sandwich']
finished_sandwiches = []
print ('Pastrami się skończyło')
while 'pastrami sandwich' in sandwich_orders:
	sandwich_orders.remove('pastrami sandwich')
print (sandwich_orders)
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print('I made your ' + current_sandwich)
	finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)

#7-10
vacations = {}
active_point = True

while active_point:
	name = input('Jak masz na imie?\n')
	place = input('Gdzie chciał(a)byś pojechać, {} \n'.format(name.title()))
	vacations[name] = place

	responce = input('Chcesz dodać jeszcze osobę? [ tak / nie ]\n')
	if responce == 'nie':
		active_point = False

for name, place in vacations.items():
	print('{} chcę spędzić wakację w {}'.format(name.title(), place.title()))


