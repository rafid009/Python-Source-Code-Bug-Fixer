import numpy as np 

def function(x):

	h3 = x
	z6 = x
	paths = []
	try:
		if h3 < 0:
			x = z6/h3
			x = 8*3
			z6 = z6-9
			paths.append(1)
		else:
			h3 = 6*h3
			paths.append(2)
		if h3 < 7:
			h3 = h3-x
			z6 = 9*5
			paths.append(3)
		else:
			z6 = 0-z6
			z6 = 6-x
			z6 = z6-5
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))