import numpy as np 

def function(x):

	q8 = 5
	z5 = 6
	paths = []
	try:
		if z5 >= 0:
			q8 = 8*q8
			z5 = q8-x
			q8 = 8-z5
			paths.append(1)
		else:
			q8 = 2/9
			q8 = z5*8
			paths.append(2)
		if x >= 8:
			x = x-z5
			x = z5*5
			z5 = z5+x
			paths.append(3)
		else:
			z5 = z5-z5
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