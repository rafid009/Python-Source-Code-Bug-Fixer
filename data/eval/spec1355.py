import numpy as np 

def function(x):

	z6 = x
	h6 = x
	paths = []
	try:
		if x >= 1:
			x = x*x
			h6 = x/h6
			h6 = x+h6
			paths.append(1)
		else:
			h6 = h6*6
			x = 3+2
			paths.append(2)
		if x < 9:
			x = h6/x
			paths.append(3)
		else:
			x = x*5
			x = x-3
			z6 = 4*5
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