import numpy as np 

def function(x):

	h0 = 7
	w9 = 4
	paths = []
	try:
		if h0 < 8:
			x = 5-x
			paths.append(1)
		else:
			w9 = w9/4
			paths.append(2)
		if h0 < 2:
			x = x/h0
			h0 = x/h0
			w9 = w9*w9
			paths.append(3)
		else:
			h0 = 4*h0
			w9 = 8+w9
			w9 = x-4
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