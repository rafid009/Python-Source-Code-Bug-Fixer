import numpy as np 

def function(x):

	z7 = 1
	g6 = 6
	x = x
	paths = []
	try:
		if g6 >= 9:
			x = 3*x
			paths.append(1)
		else:
			z7 = z7+1
			z7 = 0+g6
			g6 = z7-g6
			paths.append(2)
		if g6 < 8:
			g6 = 4-1
			g6 = 5*9
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))