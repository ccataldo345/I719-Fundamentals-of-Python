# Task 2

import random

def fizz_buzz(i):
	
	"""
	Print no. 1-100, if mult 3 prt Fizz, if mult of 5 prt "Fuzz", if both mult of 3 and 5 prt 		FIZZBUZZ"
	"""
	pass

for i in range (1, random.randint(2,101)):
	if i%3==0 and i%5==0:
		print ("FizzBuzz(" + str(i) + ")")
	
	elif i%3== 0:
		print("Fizz(" + str(i) + ")")

	elif i%5== 0:
		print("Buzz(" + str(i) + ")")

	else:
		print(i)

