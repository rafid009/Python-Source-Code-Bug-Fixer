import numpy as np 

def function(x):

	n0 = 3
	z0 = x
	paths = []
	try:
		if x > 0:
			n0 = n0/7
			z0 = z0-1
			n0 = n0-4
			paths.append(1)
		else:
			x = x/4
			z0 = 8*z0
			x = x/1
			paths.append(2)
		if n0 > 8:
			x = x-x
			n0 = z0-n0
			x = x/x
			paths.append(3)
		else:
			n0 = 8-9
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