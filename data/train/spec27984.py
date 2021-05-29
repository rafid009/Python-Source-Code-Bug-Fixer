import numpy as np 

def function(x):

	e2 = 8
	s3 = 4
	paths = []
	try:
		if s3 < 0:
			e2 = 0-2
			e2 = e2-s3
			paths.append(1)
		else:
			s3 = s3+7
			e2 = 3*e2
			e2 = e2*3
			paths.append(2)
		if s3 >= 2:
			x = x*s3
			x = 9*x
			e2 = e2+s3
			paths.append(3)
		else:
			x = x-4
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