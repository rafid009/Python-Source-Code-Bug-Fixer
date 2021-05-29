import numpy as np 

def function(x):

	h6 = x
	n3 = 9
	paths = []
	try:
		if n3 > 5:
			n3 = 8+n3
			h6 = x/h6
			paths.append(1)
		else:
			n3 = n3/x
			h6 = x-5
			n3 = 5/n3
			paths.append(2)
		if h6 < 1:
			x = 5*x
			h6 = 4*n3
			h6 = x-3
			paths.append(3)
		else:
			h6 = x/h6
			h6 = 8/h6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))