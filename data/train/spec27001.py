import numpy as np 

def function(x):

	h0 = x
	h5 = x
	paths = []
	try:
		if h5 >= 8:
			x = 6+5
			paths.append(1)
		else:
			h0 = x/9
			x = x-3
			paths.append(2)
		if h5 > 2:
			h5 = 1/x
			paths.append(3)
		else:
			h5 = h5-2
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