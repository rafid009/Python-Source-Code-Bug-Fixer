import numpy as np 

def function(x):

	s3 = 9
	a7 = x
	paths = []
	try:
		if x <= 1:
			a7 = a7*6
			paths.append(1)
		else:
			s3 = 0+s3
			s3 = a7-4
			paths.append(2)
		if s3 <= 9:
			s3 = s3-6
			paths.append(3)
		else:
			s3 = 5/s3
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