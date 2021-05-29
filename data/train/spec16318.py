import numpy as np 

def function(x):

	s3 = 9
	c8 = x
	paths = []
	try:
		if s3 < 4:
			c8 = c8+8
			paths.append(1)
		else:
			s3 = 2*3
			paths.append(2)
		if c8 > 7:
			x = x-x
			paths.append(3)
		else:
			c8 = c8+5
			s3 = s3/1
			s3 = s3-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))