import numpy as np 

def function(x):

	y0 = 0
	h7 = 4
	paths = []
	try:
		if x < 1:
			x = x/4
			h7 = 3/x
			y0 = y0-2
			paths.append(1)
		else:
			h7 = 8/5
			x = 7/x
			h7 = 6-h7
			paths.append(2)
		if y0 >= 3:
			x = x*5
			paths.append(3)
		else:
			x = h7*y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		h7 = y0**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))