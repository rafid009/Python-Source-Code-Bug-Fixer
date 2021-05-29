import numpy as np 

def function(x):

	h6 = 6
	h0 = 3
	paths = []
	try:
		if x <= 4:
			x = x+2
			h0 = h0-6
			paths.append(1)
		else:
			h0 = h6+4
			paths.append(2)
		if h6 <= 3:
			h6 = 7/h6
			paths.append(3)
		else:
			h6 = h6/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))