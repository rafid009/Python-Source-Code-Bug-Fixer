import numpy as np 

def function(x):

	h0 = 7
	d4 = 6
	paths = []
	try:
		if d4 < 2:
			x = 8*x
			h0 = h0-0
			paths.append(1)
		else:
			d4 = x+d4
			paths.append(2)
		if d4 <= 5:
			h0 = h0-h0
			d4 = 5*d4
			paths.append(3)
		else:
			h0 = h0/h0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))