import numpy as np 

def function(x):

	g0 = x
	z1 = x
	paths = []
	try:
		if x < 8:
			g0 = x*g0
			g0 = g0-x
			paths.append(1)
		else:
			x = g0*3
			paths.append(2)
		if g0 < 6:
			z1 = g0/z1
			x = 3+g0
			paths.append(3)
		else:
			z1 = z1/8
			g0 = g0/5
			g0 = x/g0
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