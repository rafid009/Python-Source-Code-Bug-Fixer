import numpy as np 

def function(x):

	a5 = 3
	h5 = 8
	paths = []
	try:
		if x <= 2:
			h5 = a5+a5
			a5 = 4+7
			paths.append(1)
		else:
			a5 = h5*7
			paths.append(2)
		if h5 < 3:
			h5 = h5/a5
			h5 = 4/h5
			paths.append(3)
		else:
			h5 = h5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))