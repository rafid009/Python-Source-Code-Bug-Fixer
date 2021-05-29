import numpy as np 

def function(x):

	z5 = 5
	g9 = 1
	paths = []
	try:
		if z5 > 6:
			x = x+7
			x = x/9
			x = x-g9
			paths.append(1)
		else:
			z5 = z5-4
			z5 = 5-x
			paths.append(2)
		if z5 >= 2:
			x = 0-4
			z5 = 0-z5
			g9 = g9*z5
			paths.append(3)
		else:
			g9 = 1+g9
			x = x/9
			z5 = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))