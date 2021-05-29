import numpy as np 

def function(x):

	e0 = 8
	h8 = 9
	paths = []
	try:
		if x <= 7:
			h8 = e0*h8
			paths.append(1)
		else:
			x = x+x
			e0 = h8-x
			h8 = x+h8
			paths.append(2)
		if h8 >= 2:
			x = x+e0
			h8 = h8+x
			h8 = 7-h8
			paths.append(3)
		else:
			e0 = e0-3
			e0 = e0/9
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