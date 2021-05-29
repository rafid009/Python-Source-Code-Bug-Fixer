import numpy as np 

def function(x):

	h0 = x
	d0 = 6
	x = 9
	paths = []
	try:
		if d0 >= 1:
			x = x-7
			d0 = 9/d0
			paths.append(1)
		else:
			h0 = h0/8
			paths.append(2)
		if x > 3:
			d0 = 1/h0
			h0 = d0*9
			paths.append(3)
		else:
			d0 = 6-d0
			d0 = h0-d0
			x = x/h0
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