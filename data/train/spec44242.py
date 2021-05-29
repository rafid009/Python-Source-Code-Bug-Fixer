import numpy as np 

def function(x):

	h5 = 9
	z8 = 9
	paths = []
	try:
		if x < 3:
			z8 = 1/1
			paths.append(1)
		else:
			x = h5*6
			paths.append(2)
		if x < 2:
			x = 2+x
			h5 = h5-4
			paths.append(3)
		else:
			x = 8*4
			x = x+h5
			x = x/1
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