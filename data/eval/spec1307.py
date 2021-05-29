import numpy as np 

def function(x):

	y7 = x
	h1 = x
	paths = []
	try:
		if x >= 9:
			x = x*h1
			paths.append(1)
		else:
			h1 = 9-h1
			paths.append(2)
		if x >= 8:
			h1 = 0*h1
			x = 1*x
			paths.append(3)
		else:
			y7 = 8/y7
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))