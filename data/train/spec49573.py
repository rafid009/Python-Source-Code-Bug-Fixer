import numpy as np 

def function(x):

	z9 = x
	h6 = x
	paths = []
	try:
		if h6 < 1:
			h6 = h6*8
			z9 = 1-z9
			z9 = 6+9
			paths.append(1)
		else:
			z9 = z9/z9
			x = x/x
			x = 9+x
			paths.append(2)
		if h6 < 1:
			z9 = 5-7
			paths.append(3)
		else:
			h6 = z9/4
			x = h6+x
			h6 = h6+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))