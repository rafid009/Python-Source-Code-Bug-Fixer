import numpy as np 

def function(x):

	h3 = 0
	h0 = 6
	paths = []
	try:
		if x >= 7:
			x = x*h0
			x = 7*x
			x = 1+h3
			paths.append(1)
		else:
			h3 = h3*h0
			h0 = 2/h0
			x = x-4
			paths.append(2)
		if x < 2:
			h3 = h3*h3
			x = 1/x
			paths.append(3)
		else:
			x = 3-x
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