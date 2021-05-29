import numpy as np 

def function(x):

	h7 = x
	d4 = x
	paths = []
	try:
		if x <= 9:
			x = 3*x
			d4 = x/x
			h7 = h7-x
			paths.append(1)
		else:
			h7 = h7-d4
			x = 8+h7
			paths.append(2)
		if h7 > 2:
			h7 = d4*5
			paths.append(3)
		else:
			x = x-h7
			x = x*d4
			d4 = 8-d4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))