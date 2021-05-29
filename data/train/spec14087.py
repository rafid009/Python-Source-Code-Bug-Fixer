import numpy as np 

def function(x):

	h5 = x
	e0 = x
	paths = []
	try:
		if x <= 2:
			e0 = 8-e0
			x = h5+x
			paths.append(1)
		else:
			e0 = 6+x
			paths.append(2)
		if e0 < 0:
			x = e0-h5
			paths.append(3)
		else:
			h5 = x*e0
			x = 5+x
			h5 = 3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))