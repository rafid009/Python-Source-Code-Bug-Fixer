import numpy as np 

def function(x):

	s3 = 0
	n7 = x
	paths = []
	try:
		if s3 < 9:
			n7 = n7+4
			s3 = 2*s3
			x = s3-x
			paths.append(1)
		else:
			n7 = n7/6
			s3 = 3*s3
			paths.append(2)
		if s3 < 2:
			x = 2-x
			s3 = n7/2
			s3 = 2*x
			paths.append(3)
		else:
			n7 = 1+4
			s3 = s3/3
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))