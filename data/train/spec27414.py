import numpy as np 

def function(x):

	z2 = 3
	g6 = x
	paths = []
	try:
		if x > 1:
			x = 0/x
			paths.append(1)
		else:
			z2 = 6-z2
			g6 = g6-4
			paths.append(2)
		if g6 <= 8:
			z2 = z2*9
			x = x+4
			g6 = 6*x
			paths.append(3)
		else:
			g6 = g6/7
			x = 0+z2
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))