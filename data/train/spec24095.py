import numpy as np 

def function(x):

	h8 = x
	z4 = x
	paths = []
	try:
		if h8 < 0:
			x = 8*6
			x = 9-7
			paths.append(1)
		else:
			h8 = 8*h8
			z4 = h8*5
			paths.append(2)
		if x > 3:
			x = 2-x
			z4 = z4*0
			z4 = z4-x
			paths.append(3)
		else:
			x = z4/x
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