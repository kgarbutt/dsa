# factorial calculation

def factorial(n):
	# test for base case
	if n == 0:
		return 1
		
	# make calc and recursive call
	else:
		f = n * factorial(n-1)
		
	print(f)
	return(f)
	
print(factorial(12))
