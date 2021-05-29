import numpy as np 

def function(x):

	y0 = x
	h9 = x
	x = x
	paths = []
	try:
		if h9 >= 2:
			x = x-6
			paths.append(1)
		else:
			h9 = h9-6
			paths.append(2)
		if y0 <= 4:
			x = y0-y0
			y0 = y0+2
			y0 = y0/9
			paths.append(3)
		else:
			y0 = 7/3
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