import numpy as np 

def function(x):

	h5 = 2
	i9 = 9
	paths = []
	try:
		if x < 6:
			i9 = i9*6
			paths.append(1)
		else:
			i9 = i9+2
			paths.append(2)
		if h5 >= 5:
			x = x+0
			i9 = x-h5
			paths.append(3)
		else:
			h5 = i9*8
			i9 = i9/4
			x = 3-h5
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