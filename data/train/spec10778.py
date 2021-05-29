import numpy as np 

def function(x):

	h2 = 8
	z0 = 9
	paths = []
	try:
		if z0 >= 2:
			z0 = z0*0
			h2 = 5/h2
			paths.append(1)
		else:
			z0 = 4-z0
			paths.append(2)
		if z0 >= 1:
			z0 = 2+z0
			h2 = 3+h2
			h2 = x*8
			paths.append(3)
		else:
			h2 = h2+2
			h2 = 9-h2
			z0 = h2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))