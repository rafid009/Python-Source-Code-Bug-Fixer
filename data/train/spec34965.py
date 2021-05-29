import numpy as np 

def function(x):

	w4 = x
	h5 = 9
	paths = []
	try:
		if x < 6:
			x = x*7
			h5 = x/w4
			h5 = h5/h5
			paths.append(1)
		else:
			w4 = h5/9
			paths.append(2)
		if h5 > 6:
			h5 = 9+3
			w4 = w4/2
			x = x+8
			paths.append(3)
		else:
			x = x+6
			h5 = 8/h5
			h5 = 9*5
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