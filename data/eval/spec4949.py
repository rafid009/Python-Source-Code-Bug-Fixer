import numpy as np 

def function(x):

	z1 = 4
	y0 = x
	paths = []
	try:
		if y0 >= 9:
			y0 = 3-z1
			paths.append(1)
		else:
			z1 = z1/9
			z1 = 0*1
			x = x-z1
			paths.append(2)
		if z1 < 9:
			y0 = y0/4
			paths.append(3)
		else:
			x = z1*2
			y0 = 7/y0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))