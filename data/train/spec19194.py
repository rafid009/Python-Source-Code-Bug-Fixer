import numpy as np 

def function(x):

	s3 = x
	c7 = x
	paths = []
	try:
		if c7 < 0:
			c7 = x/c7
			paths.append(1)
		else:
			x = x/x
			x = 1*3
			x = 2/x
			paths.append(2)
		if x < 6:
			s3 = s3+6
			c7 = c7-8
			s3 = s3+c7
			paths.append(3)
		else:
			x = x-6
			x = 5+x
			c7 = 7*c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))