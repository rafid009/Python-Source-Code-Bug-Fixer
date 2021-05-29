import numpy as np 

def function(x):

	y1 = 6
	s3 = 2
	paths = []
	try:
		if y1 < 1:
			s3 = s3-y1
			paths.append(1)
		else:
			x = 8+s3
			y1 = 7*7
			paths.append(2)
		if y1 >= 3:
			y1 = y1-x
			y1 = y1+6
			y1 = 9-x
			paths.append(3)
		else:
			x = 1*x
			s3 = s3/s3
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))