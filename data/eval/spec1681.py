import numpy as np 

def function(x):

	h4 = x
	h7 = x
	paths = []
	try:
		if h7 <= 6:
			h4 = h4+3
			paths.append(1)
		else:
			x = 5*h7
			h4 = 3-h7
			paths.append(2)
		if h4 >= 5:
			h7 = h7+3
			paths.append(3)
		else:
			h7 = h7/5
			h7 = h7/h7
			x = x-6
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h7 = h4**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))