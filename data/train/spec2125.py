import numpy as np 

def function(x):

	c1 = x
	s3 = x
	paths = []
	try:
		if c1 >= 1:
			c1 = c1+c1
			x = x*5
			paths.append(1)
		else:
			s3 = c1*s3
			s3 = s3/s3
			s3 = c1*4
			paths.append(2)
		if x <= 7:
			c1 = c1-7
			x = x+3
			c1 = 0+c1
			paths.append(3)
		else:
			x = 8*x
			c1 = x+c1
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		s3 = s3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))