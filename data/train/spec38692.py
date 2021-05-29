import numpy as np 

def function(x):

	h5 = 8
	e5 = x
	x = 9
	paths = []
	try:
		if h5 >= 5:
			h5 = 3-e5
			h5 = h5/x
			paths.append(1)
		else:
			e5 = x/h5
			x = 6*7
			paths.append(2)
		if h5 >= 3:
			h5 = 7-h5
			paths.append(3)
		else:
			e5 = 5-0
			h5 = h5*h5
			x = 6-h5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))