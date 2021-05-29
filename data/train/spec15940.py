import numpy as np 

def function(x):

	h0 = 2
	z0 = x
	paths = []
	try:
		if h0 <= 6:
			x = 8*x
			paths.append(1)
		else:
			z0 = 8/7
			paths.append(2)
		if x <= 0:
			x = 3/8
			h0 = 9*z0
			paths.append(3)
		else:
			h0 = 8-8
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))