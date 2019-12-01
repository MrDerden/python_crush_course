#4-3
"""
for value in range(1, 21):
	print(value)

#4-4
million = list(range(1, 1000001))
for number in million:
	print(number)
"""

#4-5
million = list(range(1, 1000001))
print(max(million))
print(min(million))
print(sum(million))

#4-6
twenty_two = []
for value in range(1, 11):
	twenty_two.append(2*value-1)
print(twenty_two)

#4-7
list_dev_3 = []
for value in range(3, 30):
	if value%3==0:
		list_dev_3.append(value)
print(list_dev_3)

#4-8
kub = [value**3 for value in range(1,10)]
print(kub)