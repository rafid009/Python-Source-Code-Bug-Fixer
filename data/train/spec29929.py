import numpy as np 

def function(x):

	h1 = 6
	z9 = 6
	paths = []
	try:
		if h1 < 1:
			x = z9/3
			h1 = 7/2
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if z9 < 3:
			h1 = 7*h1
			h1 = h1/9
			h1 = h1*x
			paths.append(3)
		else:
			z9 = 0+8
			x = 9*x
			z9 = z9-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))