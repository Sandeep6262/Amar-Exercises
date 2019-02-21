# Anagram code -: 
user = raw_input("Enter your first word ")
user1 = raw_input("Enter your second word ")
new = []
list1 = list(user)
list2 = list(user1)
if len(user) == len(user1):
	for i in list1:
		if i in list2:
			new.append(i)
	if len(list2) == len(new):
		print ("hai")
	else:
		print ("nahi hai")
else:
	print ("nahi hai ")