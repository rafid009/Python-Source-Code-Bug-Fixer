import numpy as np 

def function(x):

	h0 = 3
	l1 = 2
	x = 0
	paths = []
	try:
		if h0 <= 0:
			l1 = 2*l1
			h0 = 2-6
			paths.append(1)
		else:
			x = h0-9
			x = h0/x
			paths.append(2)
		if h0 < 6:
			h0 = h0+2
			h0 = x-h0
			paths.append(3)
		else:
			h0 = h0/x
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