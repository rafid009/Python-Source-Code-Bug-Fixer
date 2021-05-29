import numpy as np 

def function(x):

	z5 = x
	y0 = x
	paths = []
	try:
		if x > 8:
			x = x-6
			paths.append(1)
		else:
			x = y0-4
			paths.append(2)
		if z5 > 8:
			x = x*x
			z5 = z5-2
			x = x-z5
			paths.append(3)
		else:
			y0 = 5+y0
			x = z5+0
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))