import numpy as np 

def function(x):

	s3 = x
	v7 = 8
	paths = []
	try:
		if x > 5:
			v7 = s3*x
			paths.append(1)
		else:
			v7 = v7-s3
			paths.append(2)
		if v7 >= 7:
			s3 = x*v7
			paths.append(3)
		else:
			s3 = s3/v7
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