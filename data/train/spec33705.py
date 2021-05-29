import numpy as np 

def function(x):

	a5 = 5
	h0 = x
	paths = []
	try:
		if a5 < 5:
			h0 = 9*h0
			x = 4-x
			h0 = 9-5
			paths.append(1)
		else:
			x = x/8
			x = 4*h0
			paths.append(2)
		if a5 < 3:
			a5 = 9-6
			paths.append(3)
		else:
			h0 = h0/6
			h0 = x/8
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