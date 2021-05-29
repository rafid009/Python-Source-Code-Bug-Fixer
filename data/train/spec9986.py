import numpy as np 

def function(x):

	x0 = x
	h0 = x
	x = 9
	paths = []
	try:
		if x >= 4:
			h0 = h0-5
			x = x/x0
			paths.append(1)
		else:
			h0 = x0/h0
			paths.append(2)
		if x0 > 2:
			h0 = h0-5
			x0 = x0-7
			x = x/9
			paths.append(3)
		else:
			h0 = 4-2
			h0 = 8+h0
			x0 = 2-x0
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