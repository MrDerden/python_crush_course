#5-8
users = []
if users:
	for user in users:
		if user == 'admin':
			print('Hi, ' + user + ', do you want to look at statistics?')
		else:
			print('Hi ' + user.title() + '. Nice to meet your here again')
else:
	print('We need to find some users')

#5-10
current_users = ['hamMer', 'fillip', 'gudzon', 'ska', 'beetroot']
new_users = ['john', 'deadbell', 'Hammer', 'ska']
low = []
for current_user in current_users:
	low.append(current_user.lower())
#print(current_users)
#print(low)
#print(new_users)
for new_user in new_users:
	if new_user.lower() in low:
		print('User ' + new_user +' is already exist. Choose another name')
	else:
		current_users.append(new_user)
		print('Welcome, ' + new_user)
#print(current_users)

#5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
	if num == 1:
		print('1st')
	if num == 2:
		print('2nd')
	if num == 3:
		print('3rd')
	if num > 3 and num <=9:
		print(str(num) + 'th')
	