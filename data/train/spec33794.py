import numpy as np 

def function(x):

	x0 = x
	h9 = 9
	paths = []
	try:
		if x >= 1:
			x = 7/x
			paths.append(1)
		else:
			x = x-3
			h9 = h9/7
			x0 = h9+6
			paths.append(2)
		if x0 <= 6:
			x = x/6
			h9 = 1-8
			x0 = x0-9
			paths.append(3)
		else:
			h9 = x0*5
			x0 = 1-x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))