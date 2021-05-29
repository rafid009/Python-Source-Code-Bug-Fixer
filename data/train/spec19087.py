import numpy as np 

def function(x):

	s3 = 6
	e2 = x
	paths = []
	try:
		if x >= 2:
			s3 = 4-s3
			paths.append(1)
		else:
			s3 = s3+x
			paths.append(2)
		if s3 > 0:
			x = x-2
			s3 = 3/2
			s3 = 3+s3
			paths.append(3)
		else:
			e2 = e2*7
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