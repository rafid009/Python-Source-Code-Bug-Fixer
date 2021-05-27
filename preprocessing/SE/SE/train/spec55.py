import numpy as np 

def function(x):

	s3 = x
	c8 = x
	paths = []
	try:
		if s3 < 6:
			s3 = s3+0
			s3 = s3+x
			s3 = s3-7
			paths.append(1)
		else:
			c8 = 1-5
			c8 = x*c8
			paths.append(2)
		if x >= 2:
			s3 = s3+5
			c8 = 8-5
			paths.append(3)
		else:
			c8 = c8-5
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