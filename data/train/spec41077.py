import numpy as np 

def function(x):

	g8 = 8
	z3 = 5
	paths = []
	try:
		if g8 < 4:
			x = x/g8
			g8 = g8/8
			paths.append(1)
		else:
			g8 = 3*5
			g8 = g8*g8
			g8 = 6*2
			paths.append(2)
		if g8 < 2:
			z3 = z3/x
			paths.append(3)
		else:
			g8 = 1-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z3 = x**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))