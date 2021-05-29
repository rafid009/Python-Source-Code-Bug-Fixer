import numpy as np 

def function(x):

	v0 = 9
	z8 = x
	paths = []
	try:
		if z8 >= 3:
			x = 5-x
			x = 9/5
			x = 8+z8
			paths.append(1)
		else:
			z8 = z8*9
			paths.append(2)
		if v0 >= 9:
			z8 = 2/7
			v0 = v0+2
			v0 = 0+v0
			paths.append(3)
		else:
			z8 = z8-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))