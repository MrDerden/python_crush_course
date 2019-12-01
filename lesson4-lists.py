friends = ['Salo', 'Vasia', 'Belyj', 'Grusza']
message = " has bad brains"
print(friends[0] + message)
print(friends[1] + message)
print(friends[2] + message)
print(friends[3] + message)

#3-2
cars = ['audi', 'renault', 'mini', 'vw']
print("I want to drive " + cars[2].title() + " in the city")
print("I want to use " + cars[-1].upper() + " in a tours")

#3-4
guests = ['Kabzon' , 'Leontiev', 'Rotaru']
invite_message = ", I'm inviting you to a dinner"
print("Hi " + guests[0] + invite_message)
print("Hi " + guests[1] + invite_message)
print("Hi " + guests[2] + invite_message)
#3-5
print("Fuck, " + guests[0] + " will not come")
guests[0] = "Pugacheva"
print("Hi " + guests[0] + invite_message)
print("Hi " + guests[1] + invite_message)
print("Hi " + guests[2] + invite_message)
#3-6
print("I'm inviting more guests!")
guests.insert(0, "Kolia Severny")
guests.insert(2, "Krug")
guests.append("Lagutenko")
print(guests)
print("Hi " + guests[0] + invite_message)
print("Hi " + guests[1] + invite_message)
print("Hi " + guests[2] + invite_message)
print("Hi " + guests[3] + invite_message)
print("Hi " + guests[4] + invite_message)
print("Hi " + guests[5] + invite_message)
#3-7
print("Sorry, even so I can invite only two guests")
last_guest = guests.pop()
print("Sorry " + last_guest + ", see you next time")
last_guest = guests.pop()
print("Sorry " + last_guest + ", see you next time")
last_guest = guests.pop()
print("Sorry " + last_guest + ", see you next time")
last_guest = guests.pop()
print("Sorry " + last_guest + ", see you next time")
print(guests)
print("My offer still valid, " + guests[0])
print("My offer still valid, " + guests[1])
del guests[1]
del guests[0]
print(guests)

