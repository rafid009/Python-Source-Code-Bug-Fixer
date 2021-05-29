import numpy as np 

def function(x):

	z7 = 5
	y0 = x
	paths = []
	try:
		if x < 4:
			z7 = 4+z7
			y0 = x-1
			paths.append(1)
		else:
			x = x*z7
			z7 = 2-0
			x = 3+x
			paths.append(2)
		if z7 >= 1:
			y0 = y0*4
			paths.append(3)
		else:
			x = 5-0
			y0 = y0-z7
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		z7 = y0**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))