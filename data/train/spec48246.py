import numpy as np 

def function(x):

	z5 = x
	j9 = 1
	paths = []
	try:
		if j9 > 7:
			z5 = z5*0
			z5 = z5+2
			paths.append(1)
		else:
			j9 = 7*j9
			x = 0-1
			paths.append(2)
		if j9 > 0:
			z5 = j9-z5
			z5 = j9-0
			paths.append(3)
		else:
			j9 = 3*j9
			x = x*0
			j9 = 3*z5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))