import numpy as np 

def function(x):

	h6 = 7
	h0 = 8
	paths = []
	try:
		if h6 < 2:
			h0 = 4-h0
			paths.append(1)
		else:
			h6 = 3-h6
			x = x+h6
			paths.append(2)
		if h6 < 1:
			x = 9+x
			h6 = h6/1
			h6 = 8*h6
			paths.append(3)
		else:
			h0 = h0/9
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