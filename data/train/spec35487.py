import numpy as np 

def function(x):

	c8 = x
	s3 = x
	paths = []
	try:
		if c8 > 6:
			c8 = 8-4
			c8 = 7*c8
			paths.append(1)
		else:
			s3 = c8-7
			paths.append(2)
		if x < 8:
			s3 = 6-9
			paths.append(3)
		else:
			x = 9-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s3 = x**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))