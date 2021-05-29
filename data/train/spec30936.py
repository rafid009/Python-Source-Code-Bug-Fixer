import numpy as np 

def function(x):

	s3 = 5
	q4 = 4
	paths = []
	try:
		if q4 >= 4:
			x = x-q4
			q4 = x*1
			paths.append(1)
		else:
			q4 = q4/x
			s3 = 9*s3
			paths.append(2)
		if x > 3:
			x = x/2
			s3 = s3*x
			x = 2-2
			paths.append(3)
		else:
			s3 = 6/s3
			x = 3/x
			s3 = s3/q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))