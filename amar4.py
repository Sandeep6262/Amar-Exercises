# Sum of factorial :-
user = int(input("Enter your number you want the factorail sum "))
a = 1
b = 1
sum = 0
j = 0
for i in str(user):
	i = int(i)
	while a <= i:
		j = a * b
		b = j
		a = a + 1
	sum = sum + b
print (sum)