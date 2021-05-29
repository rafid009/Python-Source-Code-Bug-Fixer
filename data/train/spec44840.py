import numpy as np 

def function(x):

	d4 = 6
	h5 = x
	paths = []
	try:
		if h5 < 6:
			h5 = 6+h5
			d4 = d4-8
			paths.append(1)
		else:
			h5 = 5+4
			paths.append(2)
		if x > 8:
			d4 = 7-d4
			d4 = 5*d4
			paths.append(3)
		else:
			h5 = d4*5
			x = 4*x
			d4 = d4*h5
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