import numpy as np 

def function(x):

	z5 = 9
	g6 = 1
	paths = []
	try:
		if x >= 3:
			z5 = z5-6
			paths.append(1)
		else:
			g6 = 1-g6
			g6 = g6+1
			g6 = 1-g6
			paths.append(2)
		if z5 >= 2:
			x = 2+x
			z5 = z5/8
			paths.append(3)
		else:
			z5 = z5*7
			z5 = g6+x
			z5 = 3/4
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