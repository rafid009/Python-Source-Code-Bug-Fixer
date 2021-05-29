import numpy as np 

def function(x):

	z6 = 3
	a1 = 0
	paths = []
	try:
		if x <= 3:
			x = x-z6
			paths.append(1)
		else:
			x = x+z6
			paths.append(2)
		if z6 > 3:
			x = z6/2
			z6 = 5/3
			paths.append(3)
		else:
			a1 = x+z6
			a1 = 0*a1
			z6 = z6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))