#4-10
twenty_two = []
for value in range(1, 11):
	twenty_two.append(2*value-1)
print(twenty_two)

print("The first three items in the list are:")
print(twenty_two[:3])
print("The first three middle items in the list are:")
print(twenty_two[4:-3])
print("The first three last items in the list are:")
print(twenty_two[-3:])

#4-11
pizzas = ['margaritta', '4cheeses', 'pepperoni', 'vegetarian']
friend_pizza = pizzas[:]
pizzas.append("mexicano")
friend_pizza.append("hawaian")
print(pizzas)
print(friend_pizza)
for pizza in pizzas:
	print(pizza)
print("This is list of my favourit pizzas")

#4-13 tupils
meals = ("chicken", "salad", "pizza", "cream", "bread")
for meal in meals:
	print(meal)

meals = ("chikensalad", "herring", "sprite")
for meal in meals:
	print(meal)
    print(meal)
