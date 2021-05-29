import numpy as np 

def function(x):

	z0 = 2
	h0 = x
	paths = []
	try:
		if h0 < 4:
			h0 = 3/7
			z0 = 6-h0
			paths.append(1)
		else:
			z0 = x*3
			z0 = 1+8
			x = 4/3
			paths.append(2)
		if x < 7:
			h0 = h0-x
			x = 1*2
			x = x+h0
			paths.append(3)
		else:
			x = 7+h0
			z0 = z0-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))