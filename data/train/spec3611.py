import numpy as np 

def function(x):

	z2 = 7
	g6 = x
	paths = []
	try:
		if z2 <= 1:
			g6 = g6+9
			z2 = 9-z2
			g6 = 9*g6
			paths.append(1)
		else:
			g6 = 0-5
			paths.append(2)
		if x >= 0:
			x = x-7
			g6 = g6*x
			paths.append(3)
		else:
			x = x+0
			z2 = 2-z2
			x = x-6
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))