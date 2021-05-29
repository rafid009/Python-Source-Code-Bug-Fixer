import numpy as np 

def function(x):

	z8 = x
	g5 = 9
	x = 0
	paths = []
	try:
		if g5 < 4:
			g5 = g5-1
			g5 = g5*3
			paths.append(1)
		else:
			g5 = z8-z8
			x = x+z8
			x = 8+z8
			paths.append(2)
		if g5 <= 2:
			z8 = 6*z8
			x = 6-z8
			paths.append(3)
		else:
			x = x-g5
			x = x-4
			z8 = 6+z8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		g5 = z8**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))