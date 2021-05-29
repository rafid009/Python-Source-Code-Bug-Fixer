import numpy as np 

def function(x):

	h7 = 2
	h4 = x
	x = 0
	paths = []
	try:
		if h7 > 2:
			h4 = h4-5
			paths.append(1)
		else:
			h7 = 2-0
			paths.append(2)
		if h4 > 6:
			h4 = h4/5
			h4 = 7-h4
			h7 = h7/6
			paths.append(3)
		else:
			x = x-1
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