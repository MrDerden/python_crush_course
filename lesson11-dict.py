#6-1
person ={
	'name':'Konor',
	'surname':'McGregor',
	'age':'25',
	'city':'Los Angeles',
}
print(person['name'] + " " + person['surname'] + " living in " + person['city'] + ". And he have " + person['age'] + "years old.")

#6-2
fav_num = {
	'Kate':'666',
	'Dave':'13',
	'Diana':'1984',
	'Kolia':'1000000'
}
print('Kate likes number ' + fav_num['Kate'])
print('Dave likes number ' + fav_num['Dave'])
print('Diana likes number ' + fav_num['Diana'])
print('Kolia likes number ' + fav_num['Kolia'])

#6-3
glossary = {
	'inheritance' : 'inheritance is the mechanism of basing an object or class upon another object (prototype-based inheritance) or class (class-based inheritance), retaining similar implementation',
	'incapsulation' : 'It describes the idea of bundling data and methods that work on that data within one unit',
	'polymorthysm' : ' the ability of an object to take on many forms',
}
for key in glossary:
	print(key + ': ' + glossary[key])

#6-4
glossary_2 = {
	'zmienna' : 'konstrukcja programistyczna',
	'pętla' : 'Umożliwia cykliczne wykonywanie ciągu instrukcji',
	'warunek' : 'pozwala na wykonanie różnych instrukcji w zależności od tego czy zdefiniowane przez programistę wyrażenie logiczne jest prawdziwe, czy fałszywe',
	'lista' : 'struktura danych służąca do reprezentacji zbiorów dynamicznych, w której elementy ułożone są w liniowym porządku',
	'słownik': 'przechowuje pary (unikatowy klucz, wartość) i umożliwia dostęp do wartości poprzez podanie klucza',
	'metoda' : 'podprogram składowy klasy, którego zadaniem jest działanie na rzecz określonych elementów danej klasy lub klas z nią spokrewnionych',
	'funkcja' : 'fragment kodu, który może być wykonywany wielokrotnie z różnych miejsc programu',
}
for key, value in glossary_2.items():
	print('* ' + key.title() + ' - ' + value.title())

#6-5
rivers = {
	'Egipt' : 'Nile',
	'Poland' : 'Wisla',
	'Belarus' : 'Neman',
}
for key, value in rivers.items():
	print(value.title() + ' runs through ' + key.title())
	#print(key.title())
	#print(value.title())

#6-6
fav_lang = {
	'john' : 'Python',
	'Angela' : 'C',
	'greg' : 'C++'
}
fav_lang_list = []
for key in fav_lang:
	fav_lang_list.append(key.lower())
person_name = ['john', 'Tom', 'Greg']
print(fav_lang)
print(fav_lang_list)
print(person_name)
for name in person_name:
	if name.lower() in fav_lang_list:
		print('fuck, ' + name)
	else:
		print('Ok, ' + name)

#6-x
fav_lang = {
	'Tom' : 'C',
	'John' : ['ruby', 'java'],
	'Alison' : ['C++', 'Assembler', 'Javascript'],
}

for name, lang in fav_lang.items():
	if len(lang) > 1:
		print(name.title() + "'s favourit languages are: ")
		for language in lang:
			print (language.title())
	else:
		print()
		for language in lang:
			print(name.title() + "'s favourit language is " + language.title())

#6-7
person1 ={
	'name':'Konor',
	'surname':'McGregor',
	'age':'25',
	'city':'Los Angeles',
}
person2 ={
	'name':'Greg',
	'surname':'McKalestor',
	'age':'45',
	'city':'San Francisco',
}
person3 ={
	'name':'Karl',
	'surname':'Shpulke',
	'age':'18',
	'city':'Berlin',
}
people = [person1, person2, person3]
for pers in people:
	print(pers['name'] + ' ' + pers['surname'] + ' is living in ' + pers['city'] + ' and he/she is ' + pers['age'])
print('x'.center(100, '+'))

#6-8
dolbik = {
	'name' : 'dolbik',
	'typ' : 'hamster',
	'master' : 'Igor',
}
dranik = {
	'name' : 'dranik',
	'typ' : 'dog',
	'master' : 'Margo'
}
sztusik = {
	'name' : 'sztusik',
	'typ' : 'dog',
	'master' : 'Szwed'
}
pets = [dolbik, dranik, sztusik]
for pet in pets:
	print(pet['name'].capitalize() + ' is a ' + pet['typ'] + ' and his/her master is ' + pet['master'].title())
print('x'.center(100, '+'))

#6-9
person_0 = {'name' : 'John', 'place' : ['barcelona', 'rome', 'palma']}
person_1 = {'name' : 'Nick', 'place' : ['budapest', 'vien', 'bratislava']}
person_2 = {'name' : 'Katia', 'place' : ['Odessa', 'Kiev', 'Hawai']}
persons = [person_0, person_1, person_2]
for pers in persons:
	print(pers['name'] + "'s favourite places are:")
	for v in pers['place']:
		print(v.title())
print('x'.center(100, '+'))

#6-10
fav_num = {
	'Kate': ['666', '234', '56'],
	'Dave': ['10000', '20', '234'],
	'Diana': ['4000', '44', '56'],
	'Kolia': ['123', '56', '45']
}
for k, v in fav_num.items():
	print(k + "'s favourite numbers are: " + ', '.join(v))
print('x'.center(100, '+'))

#6-11
cities = {
	'Barcelona' : {
		'country' : 'Spain',
		'population' : '3mln',
		'fact' : 'Goudi'
		},
	'Rome' : {
		'country' : 'Italy',
		'population' : '4mln',
		'fact' : 'Kolizei'
		},
	'Warsaw' : {
		'country' : 'Poland',
		'population' : '3mln',
		'fact' : 'Pkin'
		}
}
for city, info in cities.items():
	country = info['country']
	population = info['population']
	fact = info['fact']
	print(city.title() + ' is a city of ' + country.title() + ' with population of ' + population + ' and intrsting fact is ' + fact)