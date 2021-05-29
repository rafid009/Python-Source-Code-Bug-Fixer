import numpy as np 

def function(x):

	x4 = 3
	s3 = 8
	paths = []
	try:
		if x4 < 4:
			x4 = x4-8
			paths.append(1)
		else:
			s3 = x4*s3
			s3 = 9+s3
			paths.append(2)
		if x4 > 2:
			x4 = x4/x4
			paths.append(3)
		else:
			x = 5/x
			x4 = x/x4
			x4 = x4-6
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		s3 = x4**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))