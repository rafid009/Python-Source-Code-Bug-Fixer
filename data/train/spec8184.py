import numpy as np 

def function(x):

	a0 = 2
	s3 = x
	paths = []
	try:
		if x <= 9:
			s3 = 9/s3
			s3 = s3*7
			s3 = s3/8
			paths.append(1)
		else:
			a0 = s3/x
			s3 = 2+s3
			s3 = 1+a0
			paths.append(2)
		if x > 2:
			x = x+6
			s3 = s3-x
			a0 = a0-0
			paths.append(3)
		else:
			a0 = 4/a0
			s3 = 3*s3
			a0 = a0/5
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