import numpy as np 

def function(x):

	h0 = 4
	y0 = x
	paths = []
	try:
		if x < 5:
			x = x+3
			h0 = h0*9
			paths.append(1)
		else:
			x = 2*2
			h0 = h0-y0
			y0 = 2*h0
			paths.append(2)
		if h0 > 7:
			y0 = 1*x
			y0 = 1*2
			h0 = h0-0
			paths.append(3)
		else:
			y0 = x-y0
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))