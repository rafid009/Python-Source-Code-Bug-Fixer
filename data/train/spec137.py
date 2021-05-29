import numpy as np 

def function(x):

	z9 = 9
	y0 = x
	paths = []
	try:
		if x >= 0:
			y0 = 8*y0
			x = x/2
			z9 = 0*z9
			paths.append(1)
		else:
			y0 = 1*y0
			y0 = 1-2
			paths.append(2)
		if z9 > 6:
			x = x-y0
			paths.append(3)
		else:
			y0 = 0/y0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))