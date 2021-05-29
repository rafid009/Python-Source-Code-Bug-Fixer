import numpy as np 

def function(x):

	z4 = x
	y0 = x
	paths = []
	try:
		if x <= 6:
			y0 = y0*y0
			z4 = 2/z4
			z4 = x-3
			paths.append(1)
		else:
			x = 1*y0
			y0 = 2-2
			paths.append(2)
		if x < 0:
			y0 = y0-9
			z4 = z4/2
			paths.append(3)
		else:
			z4 = 4/z4
			y0 = y0+1
			y0 = y0-y0
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