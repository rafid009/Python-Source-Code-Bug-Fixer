import numpy as np 

def function(x):

	e5 = x
	h3 = 8
	x = x
	paths = []
	try:
		if h3 > 8:
			h3 = h3*h3
			x = x-e5
			paths.append(1)
		else:
			e5 = e5*8
			paths.append(2)
		if h3 < 5:
			x = 9+3
			paths.append(3)
		else:
			e5 = e5-e5
			x = x-e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))