import numpy as np 

def function(x):

	s3 = 6
	c9 = x
	paths = []
	try:
		if s3 > 3:
			c9 = s3-c9
			s3 = c9/7
			x = s3*1
			paths.append(1)
		else:
			s3 = 2-7
			paths.append(2)
		if x >= 4:
			x = 3-s3
			x = s3/2
			paths.append(3)
		else:
			s3 = 6*s3
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))