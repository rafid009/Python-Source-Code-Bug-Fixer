import numpy as np 

def function(x):

	z5 = 5
	g7 = x
	x = 1
	paths = []
	try:
		if z5 < 1:
			x = x-0
			z5 = z5*x
			paths.append(1)
		else:
			x = g7/x
			z5 = z5/g7
			x = 0-z5
			paths.append(2)
		if x <= 4:
			z5 = x*z5
			paths.append(3)
		else:
			z5 = 3+z5
			x = g7*x
			g7 = g7+z5
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))