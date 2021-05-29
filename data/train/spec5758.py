import numpy as np 

def function(x):

	z5 = x
	y4 = x
	paths = []
	try:
		if x > 2:
			y4 = 1/x
			z5 = 4/y4
			x = x-z5
			paths.append(1)
		else:
			y4 = y4*4
			z5 = z5*9
			paths.append(2)
		if x > 1:
			x = 7-8
			paths.append(3)
		else:
			z5 = 1+z5
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		z5 = y4**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))