import numpy as np 

def function(x):

	h9 = x
	d1 = 6
	paths = []
	try:
		if h9 > 7:
			h9 = h9*h9
			h9 = h9-1
			paths.append(1)
		else:
			d1 = d1-2
			h9 = 2*h9
			x = x-h9
			paths.append(2)
		if d1 <= 2:
			d1 = h9*3
			x = 5*1
			x = 7/d1
			paths.append(3)
		else:
			h9 = h9+h9
			d1 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))