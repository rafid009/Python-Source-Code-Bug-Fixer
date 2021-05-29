import numpy as np 

def function(x):

	a9 = x
	z1 = x
	x = x
	paths = []
	try:
		if x > 2:
			x = a9*4
			paths.append(1)
		else:
			z1 = z1-z1
			z1 = 0-z1
			z1 = 9*z1
			paths.append(2)
		if a9 >= 5:
			a9 = z1-7
			paths.append(3)
		else:
			z1 = 3+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))