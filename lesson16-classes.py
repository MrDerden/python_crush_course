#9-10
import restaurant
import user

# restaurant = restaurant.Restaurant('Au lak', 'chineese')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# qwerty = user.User('John', 'Doe', 'male', 'haker')
# qwerty.about_user()

# admin = user.Admin('Petia', 'Sidorov', 'male', 'kucharz')
# admin.user_privilegies.show_privileges()
# admin.admin_privileges()

#9-13
from collections import OrderedDict

glossary_2 = {
	'zmienna' : 'konstrukcja programistyczna',
	'pętla' : 'Umożliwia cykliczne wykonywanie ciągu instrukcji',
	'warunek' : 'pozwala na wykonanie różnych instrukcji w zależności od tego czy zdefiniowane przez programistę wyrażenie logiczne jest prawdziwe, czy fałszywe',
	'lista' : 'struktura danych służąca do reprezentacji zbiorów dynamicznych, w której elementy ułożone są w liniowym porządku',
	'słownik': 'przechowuje pary (unikatowy klucz, wartość) i umożliwia dostęp do wartości poprzez podanie klucza',
	'metoda' : 'podprogram składowy klasy, którego zadaniem jest działanie na rzecz określonych elementów danej klasy lub klas z nią spokrewnionych',
	'funkcja' : 'fragment kodu, który może być wykonywany wielokrotnie z różnych miejsc programu',
}
for i, j in glossary_2.items():
	print(i + " : " + j) 

new_glossary = OrderedDict()
new_glossary['zmienna'] = 'konstrukcja programistyczna'
new_glossary['pętla'] = 'Umożliwia cykliczne wykonywanie ciągu instrukcji'
new_glossary['warunek'] = 'pozwala na wykonanie różnych instrukcji w zależności od tego czy zdefiniowane przez programistę wyrażenie logiczne jest prawdziwe, czy fałszywe'
new_glossary['lista'] = 'struktura danych służąca do reprezentacji zbiorów dynamicznych, w której elementy ułożone są w liniowym porządku'
new_glossary['słownik'] = 'przechowuje pary (unikatowy klucz, wartość) i umożliwia dostęp do wartości poprzez podanie klucza'
new_glossary['metoda'] = 'podprogram składowy klasy, którego zadaniem jest działanie na rzecz określonych elementów danej klasy lub klas z nią spokrewnionych'
new_glossary['funkcja'] = 'fragment kodu, który może być wykonywany wielokrotnie z różnych miejsc programu'

for i, j in new_glossary.items():
	print(i + " : " + j)