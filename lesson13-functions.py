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