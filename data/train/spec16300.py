import numpy as np 

def function(x):

	s3 = x
	k6 = 7
	paths = []
	try:
		if k6 <= 7:
			s3 = s3-5
			k6 = k6*x
			paths.append(1)
		else:
			s3 = s3-k6
			s3 = s3+6
			paths.append(2)
		if s3 <= 1:
			s3 = s3+2
			k6 = k6/s3
			s3 = s3+5
			paths.append(3)
		else:
			k6 = k6+k6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))