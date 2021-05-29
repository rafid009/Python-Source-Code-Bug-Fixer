import numpy as np 

def function(x):

	h5 = x
	h9 = 3
	x = x
	paths = []
	try:
		if h9 > 7:
			h5 = h9/8
			x = h9*5
			paths.append(1)
		else:
			h5 = h9-h5
			paths.append(2)
		if x <= 1:
			h9 = x-x
			paths.append(3)
		else:
			x = h5/5
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))