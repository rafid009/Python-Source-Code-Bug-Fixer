import numpy as np 

def function(x):

	d7 = x
	h0 = 8
	paths = []
	try:
		if h0 > 6:
			x = 5+x
			h0 = h0-0
			d7 = d7/h0
			paths.append(1)
		else:
			h0 = h0+h0
			h0 = x*5
			paths.append(2)
		if h0 <= 1:
			x = 3+h0
			d7 = 7-d7
			x = h0/x
			paths.append(3)
		else:
			h0 = 2-h0
			x = h0-h0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))