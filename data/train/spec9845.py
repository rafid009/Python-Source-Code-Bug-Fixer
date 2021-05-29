import numpy as np 

def function(x):

	x4 = x
	h8 = 2
	paths = []
	try:
		if x >= 5:
			x = x-x4
			h8 = h8+6
			h8 = 3-6
			paths.append(1)
		else:
			h8 = 6/h8
			paths.append(2)
		if x4 > 2:
			x4 = x4*7
			paths.append(3)
		else:
			x4 = 4/x4
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