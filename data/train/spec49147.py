import numpy as np 

def function(x):

	h8 = 7
	z0 = 7
	paths = []
	try:
		if x <= 6:
			h8 = h8/5
			h8 = 1+h8
			paths.append(1)
		else:
			h8 = 9*x
			paths.append(2)
		if z0 <= 8:
			h8 = h8/h8
			z0 = x/2
			paths.append(3)
		else:
			z0 = 3/6
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))