import numpy as np 

def function(x):

	h0 = x
	x7 = x
	paths = []
	try:
		if x7 < 5:
			h0 = 0-h0
			x7 = 4+h0
			paths.append(1)
		else:
			x7 = x7+1
			h0 = x-h0
			paths.append(2)
		if x < 6:
			x7 = h0-x7
			h0 = h0*7
			paths.append(3)
		else:
			x7 = 9-x7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))