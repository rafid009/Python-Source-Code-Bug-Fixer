import numpy as np 

def function(x):

	h6 = 3
	h2 = 2
	paths = []
	try:
		if h6 < 6:
			h6 = h2/h6
			paths.append(1)
		else:
			h2 = 9*h2
			paths.append(2)
		if h6 < 1:
			h6 = h2/x
			paths.append(3)
		else:
			h2 = h6+h2
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