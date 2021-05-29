import numpy as np 

def function(x):

	z0 = 2
	g3 = x
	paths = []
	try:
		if z0 <= 4:
			x = 9/g3
			g3 = g3+g3
			z0 = g3*8
			paths.append(1)
		else:
			x = x+6
			x = x*x
			z0 = 2-z0
			paths.append(2)
		if g3 > 0:
			z0 = g3-z0
			z0 = z0+3
			z0 = z0+z0
			paths.append(3)
		else:
			x = g3+x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		g3 = z0**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))