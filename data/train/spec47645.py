import numpy as np 

def function(x):

	q6 = x
	s3 = x
	paths = []
	try:
		if x <= 7:
			q6 = 6/s3
			paths.append(1)
		else:
			s3 = 7*s3
			x = x/6
			q6 = 6-q6
			paths.append(2)
		if q6 > 2:
			x = q6-x
			paths.append(3)
		else:
			q6 = s3-x
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		x = s3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))