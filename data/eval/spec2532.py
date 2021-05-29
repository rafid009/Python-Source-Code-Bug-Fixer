import numpy as np 

def function(x):

	g8 = x
	z0 = x
	paths = []
	try:
		if z0 >= 3:
			g8 = g8*g8
			g8 = 1/1
			z0 = z0-x
			paths.append(1)
		else:
			x = x/x
			z0 = z0+4
			paths.append(2)
		if g8 <= 2:
			x = g8*x
			paths.append(3)
		else:
			x = 3/x
			g8 = 9/g8
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))