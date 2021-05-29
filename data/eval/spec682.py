import numpy as np 

def function(x):

	z6 = x
	y0 = x
	paths = []
	try:
		if z6 < 4:
			z6 = 0-z6
			x = 0-x
			paths.append(1)
		else:
			x = 9+x
			y0 = z6+3
			y0 = 9*8
			paths.append(2)
		if y0 < 2:
			z6 = 7-z6
			x = 6+3
			y0 = y0*4
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))