# Difference between local & global variables

a=15; b=25

print(a) # prints from local namespace
print(b)

def my_function():
	global a
	a=11;b== 25
	
my_function()
print(a) # prints from global namespace
print(b)


