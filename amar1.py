
user = int(input("Enter a number "))
c = user
a = 3
print ("Even numbers")
while a > 0:
	if user % 2 == 0:
		user =  (user + 2)
		print (user)
	else:
		user = user - 1
		print (user)
	a = a - 1
b = 0
print ("Odd numbers")
while b < 3:
	if c % 2 != 0:
		c = c - 2
		print (c)
	else:
		c = c - 1
		print (c)
	b = b + 1
