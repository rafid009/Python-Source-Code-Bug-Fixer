import numpy as np 

def function(x):

	y6 = 7
	h0 = 3
	paths = []
	try:
		if h0 <= 0:
			y6 = 4*4
			paths.append(1)
		else:
			h0 = h0+7
			x = x*y6
			paths.append(2)
		if h0 >= 6:
			y6 = y6*1
			y6 = y6*y6
			paths.append(3)
		else:
			y6 = 3+y6
			y6 = y6-h0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))