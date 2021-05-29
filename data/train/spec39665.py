import numpy as np 

def function(x):

	h5 = x
	s3 = x
	paths = []
	try:
		if x >= 8:
			x = x-0
			paths.append(1)
		else:
			h5 = h5/4
			h5 = 3-h5
			paths.append(2)
		if x <= 9:
			h5 = h5/8
			paths.append(3)
		else:
			x = 7+x
			h5 = 2+9
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