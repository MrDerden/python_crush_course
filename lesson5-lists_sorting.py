#3-8
countries = ['Bosnia', 'Samali', 'Albania', 'Indonesia']
print(countries)
print(sorted(countries))
print(countries)
print("\n")
print(sorted(countries, reverse=True))
print(countries)
print("\n")
countries.reverse()
print(countries)
print("\n")
countries.reverse()
print(countries)
print("\n")
countries.sort()
print(countries)
print("\n")
countries.sort(reverse=True)
print(countries)

#3-9
guests = ['Kabzon' , 'Leontiev', 'Rotaru']
print("I have invited " + str(len(guests)) + " friends for a dinner")

#3-10
print("\n")
drumkits = ['tama', 'pearl', 'dw']
print(drumkits)
drumkits.append('yamaha')
print(drumkits)
drumkits.insert(2, 'pacific')
print(drumkits)
del drumkits[-1]
print(drumkits)
my_kit = drumkits.pop(0)
print(drumkits)
print(my_kit.title() + " is not for sale")
expensive_kit = 'dw'
drumkits.remove(expensive_kit)
print(expensive_kit.upper() + " is too expensive for me")
print(drumkits)
drumkits.append('sonor')
drumkits.append('gretch')
drumkits.append('mapex')
print(drumkits)
print(sorted(drumkits))
print(sorted(drumkits, reverse=True))
print(drumkits)
drumkits.reverse()
print(drumkits)
drumkits.sort()
print(drumkits)
print("There are " + str(len(drumkits)) + " drumkits producers in this list")
