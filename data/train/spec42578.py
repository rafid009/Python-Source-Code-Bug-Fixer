import numpy as np 

def function(x):

	h5 = x
	a4 = x
	x = 5
	paths = []
	try:
		if h5 >= 1:
			x = 0-h5
			h5 = h5*x
			paths.append(1)
		else:
			h5 = a4-6
			paths.append(2)
		if x <= 4:
			a4 = a4-4
			paths.append(3)
		else:
			x = x-x
			a4 = a4/4
			h5 = h5-a4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))