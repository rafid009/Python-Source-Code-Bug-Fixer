import numpy as np 

def function(x):

	g2 = x
	z4 = 6
	x = 1
	paths = []
	try:
		if x >= 3:
			g2 = g2+4
			paths.append(1)
		else:
			g2 = g2-3
			paths.append(2)
		if z4 < 9:
			x = 9*8
			x = 2-x
			z4 = z4-8
			paths.append(3)
		else:
			z4 = 3*x
			g2 = g2-x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		g2 = z4**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))