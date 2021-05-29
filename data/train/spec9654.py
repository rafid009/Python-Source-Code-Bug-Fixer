import numpy as np 

def function(x):

	c8 = x
	h7 = x
	paths = []
	try:
		if h7 <= 1:
			h7 = 1*9
			paths.append(1)
		else:
			h7 = h7/c8
			x = 7*x
			paths.append(2)
		if x >= 7:
			h7 = 7+h7
			paths.append(3)
		else:
			h7 = c8-h7
			h7 = 2-5
			c8 = 9-7
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		h7 = h7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))