import numpy as np 

def function(x):

	s3 = x
	j0 = x
	paths = []
	try:
		if s3 >= 9:
			j0 = s3*8
			paths.append(1)
		else:
			s3 = 4-s3
			paths.append(2)
		if x >= 3:
			j0 = 4+j0
			x = x*x
			j0 = x-j0
			paths.append(3)
		else:
			j0 = s3*4
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