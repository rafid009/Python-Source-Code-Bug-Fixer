import numpy as np 

def function(x):

	h0 = 9
	w0 = 4
	paths = []
	try:
		if w0 > 5:
			w0 = w0*3
			x = 0/x
			h0 = 2+h0
			paths.append(1)
		else:
			w0 = x-8
			x = w0-x
			h0 = h0+x
			paths.append(2)
		if w0 >= 9:
			w0 = 2+w0
			x = x-w0
			paths.append(3)
		else:
			x = 1-w0
			w0 = 4*x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		h0 = w0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))