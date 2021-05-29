import numpy as np 

def function(x):

	r3 = x
	s3 = x
	paths = []
	try:
		if r3 <= 2:
			x = r3-x
			s3 = s3*r3
			r3 = r3+r3
			paths.append(1)
		else:
			s3 = s3/9
			x = 7/s3
			paths.append(2)
		if r3 < 1:
			x = 6*x
			r3 = r3/s3
			paths.append(3)
		else:
			s3 = s3-2
			s3 = s3*6
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