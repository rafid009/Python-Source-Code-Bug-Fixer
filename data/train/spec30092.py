import numpy as np 

def function(x):

	h0 = x
	o8 = 7
	paths = []
	try:
		if h0 <= 0:
			o8 = o8/4
			paths.append(1)
		else:
			h0 = 5-h0
			paths.append(2)
		if o8 <= 0:
			x = x-2
			paths.append(3)
		else:
			h0 = h0-8
			h0 = h0+4
			h0 = h0/7
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