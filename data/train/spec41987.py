import numpy as np 

def function(x):

	z5 = 3
	h6 = x
	paths = []
	try:
		if h6 >= 6:
			h6 = h6-3
			paths.append(1)
		else:
			x = 6*x
			h6 = h6*7
			h6 = h6*3
			paths.append(2)
		if h6 <= 8:
			x = 7*3
			x = h6+x
			z5 = z5/5
			paths.append(3)
		else:
			x = x/z5
			z5 = z5/9
			h6 = 1/h6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))