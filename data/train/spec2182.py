import numpy as np 

def function(x):

	c2 = 9
	s3 = 7
	x = x
	paths = []
	try:
		if x < 1:
			c2 = c2-7
			s3 = s3*x
			paths.append(1)
		else:
			x = 0*x
			x = 6+x
			s3 = s3*s3
			paths.append(2)
		if s3 >= 4:
			x = x*1
			s3 = s3/c2
			paths.append(3)
		else:
			x = x-c2
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