import numpy as np 

def function(x):

	h5 = x
	h0 = 4
	paths = []
	try:
		if h5 < 9:
			h0 = h0-8
			x = 6-7
			h0 = 9+h0
			paths.append(1)
		else:
			x = x/3
			x = 5+5
			h0 = 2/2
			paths.append(2)
		if h0 <= 7:
			h0 = h0/5
			x = x+4
			x = x/3
			paths.append(3)
		else:
			h0 = h0/5
			h5 = h5*x
			h0 = 5/x
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		h5 = h5**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))