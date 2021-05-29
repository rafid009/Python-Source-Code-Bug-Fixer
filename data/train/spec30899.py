import numpy as np 

def function(x):

	z8 = 7
	o4 = 7
	paths = []
	try:
		if z8 >= 2:
			z8 = z8+o4
			paths.append(1)
		else:
			x = o4/x
			paths.append(2)
		if z8 > 1:
			x = 5-z8
			paths.append(3)
		else:
			o4 = 9-0
			x = o4/7
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