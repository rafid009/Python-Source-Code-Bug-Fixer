import numpy as np 

def function(x):

	s3 = x
	c0 = 1
	paths = []
	try:
		if x >= 6:
			c0 = c0-s3
			s3 = 5+s3
			paths.append(1)
		else:
			x = x*s3
			c0 = s3*1
			paths.append(2)
		if x > 5:
			x = x-0
			paths.append(3)
		else:
			c0 = c0*c0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))