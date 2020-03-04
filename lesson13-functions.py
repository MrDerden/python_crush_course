#8-1
def display_message():
	print('Poznaliśmy z funkcjami')
display_message()

print('x'.center(100, '+'))
#8-2
def fav_book(book):
	print('My favourit book is ' + book.title())
fav_book('fight club')

#8-3
def t_shirt_maker(text, size='m'):
	print('My "' + text + '" t-shirt has ' + size.title() + ' size.')

t_shirt_maker(size = 's', text = 'cunt')

#8-5
def describe_city(city, country='Poland'):
	print(city.title() + ' is in ' + country.title())

describe_city('Warsaw')
describe_city('Berlin', 'Germany')

#8-6
def city_country(city, country):
	butyfy = country.title() + ', ' + city.title()
	return butyfy

result = city_country('Warsaw', 'Poland')
print(result)
result = city_country('Berlin', 'Germany')
print(result) 
result = city_country('Barcelona', 'Spain')
print(result)

#8-7 album
def mus_album(musician, album, tracks=''):
	album_info = {'musician_name' : musician, 'album_name' : album }
	form_vers = 'My favourite album is "' + album_info['album_name'].title() + '"" of ' + album_info['musician_name'].title()
	if tracks:
		album_info['tracks'] = tracks
	return form_vers

fav_album = mus_album('metallica', 'and justice for all')
print(fav_album)

#8-8 user album
'''
q_album = ''
q_musicion = ''
while True:
	q_musicion = input('Wpisz swojego ulubionego wykonawcą: ')
	if q_musicion == 'q':
		break
	q_album = input('Wpisz swój ulubiony album: ')
	if q_album == 'q':
		break
	print(mus_album(q_musicion, q_album))
'''
#8-9 magicions
def show_magicions(magicions):
	for magicion in magicions:
		print(magicion)

list_of_magicions = ['Gendalf', 'Radegast', 'Sarumian']
show_magicions(list_of_magicions)

#8-9 make great
'''
def make_great(list_of_magicions):
	great_magicion = []
	current_magicion = []	
	while list_of_magicions:
		current_magicion = 'Great ' + list_of_magicions.pop()
		#print (list_of_magicions)
		great_magicion.append(current_magicion)
		#print(great_magicion)
	#print(list_of_magicions)
	for mag in great_magicion:
		list_of_magicions.append(mag)
	#print(list_of_magicions)
	return list_of_magicions	

make_great(list_of_magicions)
show_magicions(list_of_magicions)
'''
#8-10
def make_great(list_of_magicions):
	great_magicion = []
	current_magicion = []
	new_magicians =[]	
	while list_of_magicions:
		current_magicion = 'Great ' + list_of_magicions.pop()
		#print (list_of_magicions)
		great_magicion.append(current_magicion)
		#print(great_magicion)
	#print(list_of_magicions)
	for mag in great_magicion:
		new_magicians = list_of_magicions.append(mag)
	#print(list_of_magicions)
	return new_magicians	

make_great(list_of_magicions[:])
show_magicions(list_of_magicions)
make_great(list_of_magicions)
show_magicions(list_of_magicions)

#8-11 sendwiches
def sendwich_order(*sendwiches):
	print('Zamówiłeś/aś nastepujące sendwicze:')
	for sendwich in sendwiches:
		print('- ' + sendwich)

sendwich_order('vegan', 'bacon', 'haloomi')
sendwich_order('bloody')
sendwich_order('z gołebiem', 'z żabą', 'ze szczura', 'z człowieka')

#8-12 profile
def create_profile(imie, nazwisko, **inne):
	profile = {}
	profile['name'] = imie
	profile['surname'] = nazwisko
	for k, v in inne.items():
		profile[k] = v
	return profile

print(create_profile('John', 'Lennon', profession = 'musicion', dest = 'England'))

#8-13 cars
def car_order(marka, model, *i*nne):
	car = {}
	car['mark'] = marka
	car['model'] = model
	for k, v in inne.items():
		car[k] = v
	return car

print(car_order('opel', 'vectra', rok='1987', kolor='rdżawy'))



