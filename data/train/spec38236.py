import numpy as np 

def function(x):

	h5 = x
	n0 = x
	x = x
	paths = []
	try:
		if x > 6:
			n0 = n0*1
			paths.append(1)
		else:
			h5 = 8*6
			x = x-h5
			paths.append(2)
		if n0 >= 6:
			x = x-6
			x = x-x
			paths.append(3)
		else:
			h5 = n0*h5
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