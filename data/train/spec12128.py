import numpy as np 

def function(x):

	h5 = x
	a6 = x
	paths = []
	try:
		if x <= 3:
			a6 = 8-a6
			a6 = 6-a6
			paths.append(1)
		else:
			h5 = h5/6
			paths.append(2)
		if a6 < 1:
			x = x/7
			h5 = a6-0
			paths.append(3)
		else:
			a6 = h5-a6
			h5 = 2-h5
			a6 = 1-a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))