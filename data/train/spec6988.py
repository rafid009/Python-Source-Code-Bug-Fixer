import numpy as np 

def function(x):

	h1 = x
	z5 = 8
	paths = []
	try:
		if h1 > 7:
			h1 = h1/h1
			paths.append(1)
		else:
			h1 = 3-h1
			z5 = z5/2
			x = x+5
			paths.append(2)
		if x > 5:
			z5 = 1/z5
			paths.append(3)
		else:
			h1 = 8-h1
			x = x+4
			h1 = 4-h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))