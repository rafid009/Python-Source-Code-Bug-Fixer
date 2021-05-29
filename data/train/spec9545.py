import numpy as np 

def function(x):

	s3 = 5
	c0 = 3
	paths = []
	try:
		if c0 > 6:
			x = x*9
			c0 = c0*8
			paths.append(1)
		else:
			c0 = x/c0
			paths.append(2)
		if s3 > 0:
			s3 = 3-c0
			paths.append(3)
		else:
			c0 = c0-9
			s3 = s3*s3
			s3 = 2-s3
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