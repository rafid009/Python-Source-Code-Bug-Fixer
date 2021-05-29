import numpy as np 

def function(x):

	y0 = 6
	z6 = x
	paths = []
	try:
		if z6 <= 1:
			y0 = 1/x
			x = x/7
			paths.append(1)
		else:
			z6 = z6*7
			z6 = x/5
			paths.append(2)
		if z6 >= 7:
			x = x-0
			y0 = y0-0
			z6 = x/2
			paths.append(3)
		else:
			z6 = 5+4
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))