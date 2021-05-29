import numpy as np 

def function(x):

	s3 = x
	y0 = 0
	paths = []
	try:
		if y0 <= 8:
			x = x*7
			y0 = 4/x
			s3 = s3/8
			paths.append(1)
		else:
			s3 = s3*y0
			x = x/s3
			s3 = x*5
			paths.append(2)
		if y0 > 4:
			s3 = 1-3
			y0 = y0/x
			paths.append(3)
		else:
			x = 3-1
			s3 = s3+s3
			s3 = 2-0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))