import numpy as np 

def function(x):

	o1 = 8
	s3 = x
	paths = []
	try:
		if s3 > 6:
			s3 = 9*s3
			s3 = 1*s3
			paths.append(1)
		else:
			o1 = x-2
			o1 = 2/2
			paths.append(2)
		if s3 > 0:
			s3 = s3-s3
			o1 = o1/x
			o1 = o1/7
			paths.append(3)
		else:
			o1 = o1-4
			o1 = 0*o1
			o1 = o1/5
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