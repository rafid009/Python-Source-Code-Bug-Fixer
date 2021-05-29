import numpy as np 

def function(x):

	h4 = x
	h6 = x
	paths = []
	try:
		if h6 <= 4:
			x = x-1
			h4 = 1*h4
			paths.append(1)
		else:
			x = 2-h4
			x = 0+8
			paths.append(2)
		if h6 > 2:
			h6 = h4/h6
			h6 = h6/x
			x = x/6
			paths.append(3)
		else:
			h6 = 8/2
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h6 = h4**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))