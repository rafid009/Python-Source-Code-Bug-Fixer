import numpy as np 

def function(x):

	z6 = 8
	g1 = 7
	paths = []
	try:
		if x >= 6:
			g1 = 3/x
			g1 = g1+3
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if z6 >= 1:
			g1 = 6-4
			z6 = z6/z6
			paths.append(3)
		else:
			z6 = z6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))