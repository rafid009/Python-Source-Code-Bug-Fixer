import numpy as np 

def function(x):

	h6 = x
	r1 = 6
	paths = []
	try:
		if h6 >= 5:
			x = 2/x
			h6 = h6-r1
			paths.append(1)
		else:
			h6 = h6+2
			x = 8+x
			h6 = h6*x
			paths.append(2)
		if r1 <= 8:
			h6 = h6*8
			x = 1*x
			paths.append(3)
		else:
			r1 = 8/r1
			x = 5+x
			x = x-9
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