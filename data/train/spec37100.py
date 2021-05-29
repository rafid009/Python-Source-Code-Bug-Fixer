import numpy as np 

def function(x):

	y0 = x
	z1 = 7
	paths = []
	try:
		if y0 < 2:
			y0 = y0/5
			paths.append(1)
		else:
			z1 = z1+0
			z1 = z1-x
			paths.append(2)
		if y0 < 4:
			z1 = 0+y0
			z1 = 6/2
			z1 = z1+5
			paths.append(3)
		else:
			x = 7/y0
			y0 = y0-3
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))