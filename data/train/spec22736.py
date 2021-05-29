import numpy as np 

def function(x):

	z6 = x
	g8 = x
	paths = []
	try:
		if g8 > 1:
			z6 = z6/2
			g8 = g8*x
			paths.append(1)
		else:
			g8 = x/g8
			z6 = x+6
			g8 = g8/x
			paths.append(2)
		if g8 < 1:
			z6 = x/5
			paths.append(3)
		else:
			g8 = 1/g8
			g8 = g8/2
			g8 = z6*g8
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