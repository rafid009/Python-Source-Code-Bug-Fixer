import numpy as np 

def function(x):

	n0 = x
	h5 = 1
	paths = []
	try:
		if h5 >= 5:
			x = x/5
			paths.append(1)
		else:
			n0 = n0*h5
			h5 = x-h5
			n0 = n0+n0
			paths.append(2)
		if n0 > 8:
			x = x-6
			x = x*x
			paths.append(3)
		else:
			h5 = 6-h5
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))