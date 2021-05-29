import numpy as np 

def function(x):

	g2 = 8
	z1 = 1
	paths = []
	try:
		if g2 < 7:
			z1 = 9-4
			paths.append(1)
		else:
			x = x-0
			g2 = 1-1
			z1 = z1/5
			paths.append(2)
		if z1 >= 4:
			z1 = z1+z1
			z1 = z1-g2
			x = x+4
			paths.append(3)
		else:
			g2 = x*g2
			g2 = g2/7
			z1 = z1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))