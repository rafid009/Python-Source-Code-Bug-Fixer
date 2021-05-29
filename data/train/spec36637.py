import numpy as np 

def function(x):

	o8 = 5
	h0 = x
	paths = []
	try:
		if o8 > 7:
			o8 = o8-x
			x = x-h0
			h0 = h0-o8
			paths.append(1)
		else:
			h0 = 9+h0
			paths.append(2)
		if x > 7:
			h0 = x+6
			x = x-o8
			paths.append(3)
		else:
			o8 = x/4
			h0 = h0-0
			h0 = x+h0
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		h0 = o8**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))