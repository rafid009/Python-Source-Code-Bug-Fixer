import numpy as np 

def function(x):

	y2 = x
	s3 = x
	paths = []
	try:
		if s3 <= 1:
			s3 = s3*s3
			paths.append(1)
		else:
			x = 6*x
			x = x/6
			s3 = 2-s3
			paths.append(2)
		if y2 > 1:
			y2 = s3*6
			x = x-4
			s3 = x*s3
			paths.append(3)
		else:
			x = x/y2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))