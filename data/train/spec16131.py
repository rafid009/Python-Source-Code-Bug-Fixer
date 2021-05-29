import numpy as np 

def function(x):

	k5 = 3
	s3 = x
	paths = []
	try:
		if k5 > 8:
			s3 = s3-5
			paths.append(1)
		else:
			x = x*s3
			paths.append(2)
		if k5 <= 0:
			s3 = s3*7
			x = 6-x
			s3 = s3/3
			paths.append(3)
		else:
			k5 = 2+k5
			k5 = k5/2
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