import numpy as np 

def function(x):

	r0 = x
	h4 = 6
	paths = []
	try:
		if h4 < 8:
			x = x-h4
			paths.append(1)
		else:
			x = 6-x
			x = 1-x
			paths.append(2)
		if h4 < 6:
			x = 9+x
			paths.append(3)
		else:
			h4 = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))