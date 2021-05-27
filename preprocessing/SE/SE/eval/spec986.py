import numpy as np 

def function(x):

	k4 = 8
	h5 = 2
	paths = []
	try:
		if k4 <= 3:
			h5 = 2/3
			paths.append(1)
		else:
			k4 = 3+6
			k4 = k4*4
			paths.append(2)
		if k4 >= 0:
			h5 = 6-h5
			x = x+2
			k4 = 9-k4
			paths.append(3)
		else:
			h5 = h5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))