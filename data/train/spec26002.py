import numpy as np 

def function(x):

	h5 = 8
	a2 = x
	x = 5
	paths = []
	try:
		if h5 < 6:
			h5 = h5/6
			x = x-8
			paths.append(1)
		else:
			a2 = 2+a2
			h5 = h5-a2
			paths.append(2)
		if h5 < 7:
			a2 = h5+a2
			h5 = h5-3
			paths.append(3)
		else:
			h5 = h5+a2
			x = x-h5
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