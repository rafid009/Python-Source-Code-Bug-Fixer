import numpy as np 

def function(x):

	w0 = 1
	h0 = x
	paths = []
	try:
		if h0 >= 2:
			w0 = w0+h0
			paths.append(1)
		else:
			h0 = 6+h0
			paths.append(2)
		if w0 >= 1:
			h0 = w0/h0
			h0 = 6*5
			h0 = h0*9
			paths.append(3)
		else:
			x = 7/w0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))