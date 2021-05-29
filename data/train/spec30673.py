import numpy as np 

def function(x):

	z5 = x
	g6 = 2
	paths = []
	try:
		if x >= 5:
			x = 1+7
			paths.append(1)
		else:
			z5 = z5+8
			g6 = g6-z5
			g6 = g6+8
			paths.append(2)
		if g6 <= 1:
			z5 = 1-3
			z5 = 1+z5
			g6 = 2/g6
			paths.append(3)
		else:
			g6 = 4*g6
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))