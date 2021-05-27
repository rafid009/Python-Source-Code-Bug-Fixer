import numpy as np 

def function(x):

	h9 = 2
	h8 = 6
	x = x
	paths = []
	try:
		if h9 > 7:
			h8 = h8/6
			paths.append(1)
		else:
			h9 = h9*6
			h8 = h9-h8
			h9 = 7/1
			paths.append(2)
		if x < 5:
			h8 = 4-h8
			x = 1*x
			paths.append(3)
		else:
			h9 = 6/h9
			h9 = 8+h9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))