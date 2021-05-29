import numpy as np 

def function(x):

	q6 = x
	s3 = 8
	x = x
	paths = []
	try:
		if x <= 8:
			x = 2*s3
			s3 = s3*9
			s3 = s3/s3
			paths.append(1)
		else:
			s3 = 7+9
			s3 = 7-4
			paths.append(2)
		if q6 < 2:
			s3 = q6-s3
			x = x*6
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))