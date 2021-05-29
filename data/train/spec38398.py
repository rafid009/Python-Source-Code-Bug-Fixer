import numpy as np 

def function(x):

	z0 = x
	g0 = 4
	paths = []
	try:
		if z0 < 0:
			z0 = x/3
			g0 = g0-z0
			paths.append(1)
		else:
			g0 = g0*g0
			g0 = z0-7
			paths.append(2)
		if g0 >= 7:
			g0 = 3/g0
			x = 0+4
			x = x-x
			paths.append(3)
		else:
			z0 = 6+0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))