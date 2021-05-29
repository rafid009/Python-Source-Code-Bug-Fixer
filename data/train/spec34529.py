import numpy as np 

def function(x):

	h8 = x
	z1 = 4
	paths = []
	try:
		if x >= 5:
			h8 = 4*h8
			h8 = h8/4
			paths.append(1)
		else:
			z1 = 0/z1
			z1 = 5+z1
			paths.append(2)
		if h8 >= 9:
			x = x*9
			paths.append(3)
		else:
			x = h8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))