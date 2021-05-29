import numpy as np 

def function(x):

	h5 = 8
	h6 = x
	paths = []
	try:
		if h5 > 5:
			h6 = 5*h6
			paths.append(1)
		else:
			h6 = h6-h6
			x = x+0
			paths.append(2)
		if h6 <= 5:
			h6 = 4-7
			x = 3/x
			paths.append(3)
		else:
			x = 9*h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))