import numpy as np 

def function(x):

	z4 = x
	g0 = x
	paths = []
	try:
		if z4 >= 6:
			g0 = g0-2
			z4 = 8/z4
			x = 4-x
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if z4 > 2:
			z4 = z4+g0
			g0 = g0-g0
			z4 = z4+6
			paths.append(3)
		else:
			z4 = 4+z4
			z4 = 7*g0
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))