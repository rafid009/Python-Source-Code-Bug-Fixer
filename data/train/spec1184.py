import numpy as np 

def function(x):

	h7 = x
	z4 = x
	paths = []
	try:
		if z4 > 5:
			h7 = 9+h7
			z4 = z4/1
			paths.append(1)
		else:
			x = 9/x
			z4 = 8+8
			paths.append(2)
		if z4 > 6:
			z4 = z4+4
			x = x-z4
			x = x-3
			paths.append(3)
		else:
			h7 = h7/7
			z4 = 6*z4
			z4 = 6*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))