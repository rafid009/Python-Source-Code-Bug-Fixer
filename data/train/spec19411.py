import numpy as np 

def function(x):

	h3 = 1
	w0 = 8
	paths = []
	try:
		if h3 < 7:
			h3 = h3/4
			paths.append(1)
		else:
			h3 = h3+5
			paths.append(2)
		if h3 >= 2:
			x = 4/x
			paths.append(3)
		else:
			w0 = 3*7
			w0 = 5+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))