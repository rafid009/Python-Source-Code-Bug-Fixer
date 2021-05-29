import numpy as np 

def function(x):

	h9 = 9
	p3 = 9
	paths = []
	try:
		if h9 <= 9:
			h9 = p3-x
			h9 = 9/h9
			paths.append(1)
		else:
			h9 = h9/4
			paths.append(2)
		if h9 > 0:
			h9 = 8/8
			h9 = 0/h9
			paths.append(3)
		else:
			h9 = 1-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))