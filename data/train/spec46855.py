import numpy as np 

def function(x):

	h0 = 7
	o8 = 3
	paths = []
	try:
		if x < 7:
			o8 = x*h0
			h0 = h0/h0
			o8 = 8+o8
			paths.append(1)
		else:
			o8 = 7+o8
			x = x+0
			paths.append(2)
		if o8 > 3:
			h0 = o8/h0
			h0 = 4+x
			o8 = o8-h0
			paths.append(3)
		else:
			x = 7/x
			x = h0+6
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