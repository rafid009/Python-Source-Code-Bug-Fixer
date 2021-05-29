import numpy as np 

def function(x):

	h8 = x
	x0 = 5
	paths = []
	try:
		if x > 2:
			x0 = x0+x
			x = 8*x
			paths.append(1)
		else:
			x0 = 7-h8
			h8 = h8*2
			paths.append(2)
		if h8 > 8:
			h8 = 9-x
			h8 = h8/8
			paths.append(3)
		else:
			x0 = 2/x
			h8 = h8*6
			h8 = 9+x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		h8 = x0**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))