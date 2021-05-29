import numpy as np 

def function(x):

	v6 = x
	s3 = 6
	x = 6
	paths = []
	try:
		if x <= 5:
			x = x/8
			x = 8/s3
			paths.append(1)
		else:
			s3 = x/s3
			s3 = s3-6
			x = 9/x
			paths.append(2)
		if x > 7:
			s3 = 2*s3
			paths.append(3)
		else:
			x = 2*5
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		v6 = s3**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))