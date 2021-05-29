import numpy as np 

def function(x):

	h0 = x
	d9 = x
	x = 8
	paths = []
	try:
		if x <= 2:
			h0 = h0*9
			x = x-h0
			d9 = 3+6
			paths.append(1)
		else:
			d9 = d9*d9
			d9 = d9-x
			paths.append(2)
		if d9 > 3:
			h0 = 5-4
			paths.append(3)
		else:
			x = x/h0
			h0 = h0+0
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