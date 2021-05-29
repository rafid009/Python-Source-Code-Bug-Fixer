import numpy as np 

def function(x):

	x0 = 3
	h0 = x
	paths = []
	try:
		if x0 < 5:
			h0 = h0/9
			x0 = h0+h0
			paths.append(1)
		else:
			h0 = h0-x0
			h0 = x0/5
			paths.append(2)
		if h0 >= 8:
			x0 = x0*3
			h0 = h0+3
			paths.append(3)
		else:
			h0 = 3-0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))