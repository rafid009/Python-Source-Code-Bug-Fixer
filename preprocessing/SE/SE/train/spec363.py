import numpy as np 

def function(x):

	z5 = x
	h5 = x
	paths = []
	try:
		if h5 > 6:
			x = 3/z5
			paths.append(1)
		else:
			h5 = 2/h5
			x = x-h5
			paths.append(2)
		if z5 <= 6:
			h5 = 1+x
			h5 = h5/2
			paths.append(3)
		else:
			x = 0-x
			h5 = 7-7
			h5 = h5/3
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))