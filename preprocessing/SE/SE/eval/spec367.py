import numpy as np 

def function(x):

	d2 = x
	h0 = 9
	x = x
	paths = []
	try:
		if x <= 7:
			d2 = h0+d2
			paths.append(1)
		else:
			h0 = h0-5
			h0 = h0/h0
			paths.append(2)
		if x > 9:
			d2 = 7+4
			h0 = h0*x
			d2 = d2/4
			paths.append(3)
		else:
			h0 = 7-h0
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		h0 = d2**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))