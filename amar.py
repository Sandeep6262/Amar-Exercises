a=str(input("Enter the word\n"))
if "ing" in a:
	print(a+"ly")
elif "ly" in a:
	print(a)
else:
	print(a+"ing")