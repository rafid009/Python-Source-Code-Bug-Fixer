import numpy as np 

def function(x):

	y6 = x
	s3 = 9
	paths = []
	try:
		if y6 < 1:
			y6 = 3-y6
			x = 2-9
			x = 8-0
			paths.append(1)
		else:
			y6 = y6-s3
			paths.append(2)
		if x >= 1:
			x = s3*6
			y6 = 6*y6
			paths.append(3)
		else:
			s3 = s3+4
			y6 = y6*6
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))