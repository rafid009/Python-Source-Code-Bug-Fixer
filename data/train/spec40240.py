import numpy as np 

def function(x):

	z5 = 6
	a8 = 8
	paths = []
	try:
		if x > 8:
			a8 = a8-z5
			z5 = 9-z5
			a8 = 7-a8
			paths.append(1)
		else:
			z5 = 8*9
			a8 = a8/4
			paths.append(2)
		if x > 0:
			z5 = z5/z5
			x = x-z5
			paths.append(3)
		else:
			a8 = a8-1
			z5 = z5+5
			z5 = 4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))