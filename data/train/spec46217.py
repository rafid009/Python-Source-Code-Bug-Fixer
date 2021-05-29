import numpy as np 

def function(x):

	s3 = 7
	b4 = 9
	paths = []
	try:
		if s3 < 8:
			s3 = b4-7
			s3 = x/s3
			paths.append(1)
		else:
			x = b4+5
			paths.append(2)
		if s3 < 2:
			b4 = b4*b4
			s3 = s3/b4
			x = x/7
			paths.append(3)
		else:
			b4 = x-6
			x = 6-x
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