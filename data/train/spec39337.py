import numpy as np 

def function(x):

	z0 = 3
	r9 = 4
	paths = []
	try:
		if x < 5:
			z0 = z0/5
			paths.append(1)
		else:
			z0 = 8-z0
			paths.append(2)
		if z0 > 0:
			r9 = r9*x
			r9 = r9*2
			paths.append(3)
		else:
			x = 1*x
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