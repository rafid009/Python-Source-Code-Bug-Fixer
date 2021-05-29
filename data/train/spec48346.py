import numpy as np 

def function(x):

	q0 = x
	s3 = x
	paths = []
	try:
		if s3 >= 4:
			x = x-1
			paths.append(1)
		else:
			x = 3/x
			s3 = s3+5
			x = s3/q0
			paths.append(2)
		if x > 2:
			s3 = 5+2
			s3 = x-5
			q0 = 4-q0
			paths.append(3)
		else:
			s3 = 0-s3
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		s3 = q0**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))