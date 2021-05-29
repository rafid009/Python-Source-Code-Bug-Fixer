import numpy as np 

def function(x):

	h5 = 5
	v9 = 4
	paths = []
	try:
		if v9 < 2:
			x = v9+x
			h5 = 7*h5
			paths.append(1)
		else:
			h5 = h5+2
			paths.append(2)
		if v9 <= 1:
			v9 = v9*x
			h5 = x-h5
			paths.append(3)
		else:
			x = 4*x
			h5 = h5/v9
			h5 = h5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))