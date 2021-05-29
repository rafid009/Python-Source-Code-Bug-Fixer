import numpy as np 

def function(x):

	k6 = 0
	s3 = x
	x = 5
	paths = []
	try:
		if x >= 0:
			x = 4+5
			k6 = x+k6
			k6 = 8*s3
			paths.append(1)
		else:
			s3 = s3*6
			x = x/1
			paths.append(2)
		if x < 6:
			k6 = k6/3
			s3 = s3/2
			paths.append(3)
		else:
			x = 1/s3
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		x = s3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))