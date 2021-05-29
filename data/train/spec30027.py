import numpy as np 

def function(x):

	w8 = x
	h0 = 4
	paths = []
	try:
		if h0 > 1:
			w8 = 6*w8
			paths.append(1)
		else:
			x = x-8
			x = 0*x
			paths.append(2)
		if x < 5:
			h0 = h0-w8
			w8 = 5*w8
			paths.append(3)
		else:
			x = 8+h0
			x = x*8
			w8 = w8-x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		h0 = w8**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))