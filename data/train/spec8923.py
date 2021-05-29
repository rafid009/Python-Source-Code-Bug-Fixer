import numpy as np 

def function(x):

	s3 = 5
	h9 = 7
	paths = []
	try:
		if x >= 1:
			x = x-6
			x = s3/x
			paths.append(1)
		else:
			h9 = 7/h9
			paths.append(2)
		if x < 7:
			h9 = 9/h9
			paths.append(3)
		else:
			h9 = h9*6
			h9 = 7-x
			h9 = h9*h9
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