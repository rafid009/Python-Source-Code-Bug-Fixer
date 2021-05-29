import numpy as np 

def function(x):

	r5 = 7
	s3 = 7
	paths = []
	try:
		if x >= 1:
			x = x*x
			s3 = s3+1
			paths.append(1)
		else:
			x = 2-8
			s3 = 2/s3
			r5 = x/r5
			paths.append(2)
		if x <= 7:
			s3 = 9/r5
			paths.append(3)
		else:
			s3 = s3*3
			s3 = s3/r5
			s3 = s3+x
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