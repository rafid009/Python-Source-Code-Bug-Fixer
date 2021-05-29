import numpy as np 

def function(x):

	g5 = x
	z4 = 7
	paths = []
	try:
		if g5 < 0:
			z4 = 9+z4
			z4 = 9*z4
			paths.append(1)
		else:
			z4 = g5/g5
			g5 = g5*x
			paths.append(2)
		if z4 < 1:
			g5 = g5*7
			paths.append(3)
		else:
			x = x/2
			z4 = 4-9
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))