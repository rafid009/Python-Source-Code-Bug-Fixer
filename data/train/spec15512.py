import numpy as np 

def function(x):

	h0 = 1
	s3 = 5
	paths = []
	try:
		if h0 <= 1:
			s3 = 9*h0
			h0 = 0-x
			s3 = s3/s3
			paths.append(1)
		else:
			x = h0/4
			x = s3-x
			paths.append(2)
		if s3 > 9:
			h0 = h0-x
			paths.append(3)
		else:
			x = x-3
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