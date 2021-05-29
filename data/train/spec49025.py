import numpy as np 

def function(x):

	s3 = 7
	b6 = 4
	paths = []
	try:
		if s3 < 5:
			x = 9/x
			paths.append(1)
		else:
			s3 = 3*b6
			x = 7-x
			b6 = 1-b6
			paths.append(2)
		if s3 > 0:
			b6 = 3-5
			paths.append(3)
		else:
			x = 8/7
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		s3 = b6**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))