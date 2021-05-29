import numpy as np 

def function(x):

	z2 = 7
	h6 = 1
	paths = []
	try:
		if x >= 6:
			x = x-9
			h6 = x*h6
			paths.append(1)
		else:
			x = 3*x
			x = x*9
			paths.append(2)
		if h6 >= 4:
			h6 = h6*4
			paths.append(3)
		else:
			z2 = z2+z2
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