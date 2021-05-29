import numpy as np 

def function(x):

	h6 = x
	e9 = x
	paths = []
	try:
		if x >= 8:
			x = 0/7
			paths.append(1)
		else:
			h6 = h6-2
			x = x*3
			paths.append(2)
		if x > 9:
			h6 = e9+2
			h6 = h6-e9
			x = x*8
			paths.append(3)
		else:
			e9 = e9-9
			h6 = 2*h6
			h6 = 1-e9
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