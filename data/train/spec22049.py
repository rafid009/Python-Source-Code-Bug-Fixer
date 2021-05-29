import numpy as np 

def function(x):

	x7 = 8
	z0 = x
	paths = []
	try:
		if z0 <= 0:
			z0 = z0-1
			x7 = x+5
			x = x7+x
			paths.append(1)
		else:
			x = 3/x
			x = x7-x
			x = x7/x
			paths.append(2)
		if x7 >= 9:
			z0 = z0*5
			z0 = 9-z0
			z0 = x7*2
			paths.append(3)
		else:
			x = x+5
			x7 = x*x7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))