import numpy as np 

def function(x):

	z1 = x
	x9 = 5
	paths = []
	try:
		if z1 > 6:
			x9 = x9-6
			x = x9/x
			paths.append(1)
		else:
			z1 = 8*x9
			paths.append(2)
		if z1 <= 0:
			x = x+5
			paths.append(3)
		else:
			z1 = 8-z1
			z1 = 0+z1
			x9 = x+z1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))