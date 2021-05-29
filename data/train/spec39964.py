import numpy as np 

def function(x):

	e0 = 0
	h9 = x
	paths = []
	try:
		if e0 <= 8:
			x = 7/x
			paths.append(1)
		else:
			x = 7-5
			paths.append(2)
		if e0 > 0:
			h9 = x-8
			e0 = 9+e0
			paths.append(3)
		else:
			h9 = h9/4
			x = h9/3
			e0 = e0*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))