import numpy as np 

def function(x):

	h7 = 8
	y7 = x
	paths = []
	try:
		if h7 >= 8:
			x = 2-x
			x = h7+y7
			paths.append(1)
		else:
			x = 9*x
			x = h7-h7
			paths.append(2)
		if h7 >= 4:
			y7 = y7*3
			h7 = h7-y7
			paths.append(3)
		else:
			h7 = 0*h7
			h7 = x-h7
			y7 = 2*6
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		h7 = y7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))