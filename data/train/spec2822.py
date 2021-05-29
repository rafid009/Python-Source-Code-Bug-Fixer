import numpy as np 

def function(x):

	w0 = 0
	h3 = x
	x = 9
	paths = []
	try:
		if w0 > 1:
			h3 = 4+8
			paths.append(1)
		else:
			h3 = 8+2
			paths.append(2)
		if h3 < 1:
			h3 = 9/w0
			h3 = 9+h3
			paths.append(3)
		else:
			w0 = w0-3
			x = 3/x
			x = 0*6
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))