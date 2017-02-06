# Task 1

def add_number_to_hello(unused=None, i=1):
	
	"""
	Takes a number and adds it to the end of the string "hello"
	"""
	print(unused)

	result= "Hello {0}" .format(i)
	return result

for i in range (1,11):
	
	print(add_number_to_hello(i))

