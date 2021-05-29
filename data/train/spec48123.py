import numpy as np 

def function(x):

	z0 = x
	h6 = 2
	paths = []
	try:
		if h6 >= 0:
			z0 = z0+1
			z0 = h6-7
			paths.append(1)
		else:
			z0 = h6+8
			h6 = h6+7
			paths.append(2)
		if x > 6:
			x = x*8
			h6 = h6*4
			h6 = 3*h6
			paths.append(3)
		else:
			z0 = h6+8
			h6 = h6*h6
			h6 = h6*z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		h6 = z0**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))