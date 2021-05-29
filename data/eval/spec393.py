import numpy as np 

def function(x):

	h0 = 0
	w4 = 4
	paths = []
	try:
		if x <= 8:
			x = x-7
			h0 = 4/8
			w4 = x/1
			paths.append(1)
		else:
			w4 = w4*9
			h0 = 5/6
			paths.append(2)
		if w4 <= 0:
			w4 = h0*3
			w4 = 3+w4
			paths.append(3)
		else:
			w4 = h0/x
			h0 = h0-5
			h0 = 2*h0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))