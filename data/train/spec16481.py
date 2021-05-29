import numpy as np 

def function(x):

	x3 = 7
	h0 = x
	paths = []
	try:
		if x > 2:
			x = 9/8
			paths.append(1)
		else:
			h0 = x/h0
			x3 = x3/x3
			h0 = h0+h0
			paths.append(2)
		if x >= 3:
			h0 = x3*3
			h0 = 8-h0
			paths.append(3)
		else:
			x3 = h0-x3
			x = h0/x
			x = x3/x
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))