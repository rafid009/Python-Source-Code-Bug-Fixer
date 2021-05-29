import numpy as np 

def function(x):

	z0 = 2
	g8 = 2
	paths = []
	try:
		if z0 <= 4:
			g8 = g8+x
			g8 = x*g8
			paths.append(1)
		else:
			x = x*g8
			paths.append(2)
		if x >= 9:
			g8 = 9+1
			paths.append(3)
		else:
			z0 = 8*8
			g8 = g8+z0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))