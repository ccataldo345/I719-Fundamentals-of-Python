# Write a function hello(name) that returns the string Hello with the given name
# E.g. When we call hello(“Taavi”) the function would return “Hello Taavi”

def hello(name):
   return("Hello {}".format(name))

name01 = "Taavi"
hello(name01)

resulting_string = hello(name01)
print(resulting_string)