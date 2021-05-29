import numpy as np 

def function(x):

	h6 = 5
	x4 = 9
	paths = []
	try:
		if x >= 1:
			x4 = x4/1
			x = x/8
			x = x4*x
			paths.append(1)
		else:
			h6 = 5+x4
			x4 = x4/x4
			h6 = h6+x4
			paths.append(2)
		if x4 <= 0:
			x4 = 0*x4
			x = x-x4
			h6 = 4+4
			paths.append(3)
		else:
			x4 = 3-x4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		h6 = x4**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))