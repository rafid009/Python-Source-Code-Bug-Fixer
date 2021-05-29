import numpy as np 

def function(x):

	z8 = x
	a9 = x
	paths = []
	try:
		if z8 <= 6:
			a9 = x-6
			paths.append(1)
		else:
			a9 = a9-z8
			z8 = z8-5
			paths.append(2)
		if z8 <= 9:
			x = x/1
			paths.append(3)
		else:
			x = 3*x
			z8 = 0+z8
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		z8 = a9**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))