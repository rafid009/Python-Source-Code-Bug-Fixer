import numpy as np 

def function(x):

	z5 = x
	h7 = 2
	x = 8
	paths = []
	try:
		if x > 0:
			x = x/z5
			x = x-h7
			z5 = z5+4
			paths.append(1)
		else:
			z5 = z5*5
			paths.append(2)
		if h7 < 6:
			h7 = h7+6
			h7 = 7/6
			paths.append(3)
		else:
			h7 = 8*5
			x = x*1
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