import numpy as np 

def function(x):

	s3 = 5
	e9 = 0
	x = 9
	paths = []
	try:
		if e9 >= 2:
			e9 = s3+e9
			x = s3/x
			s3 = s3*1
			paths.append(1)
		else:
			s3 = 3*8
			s3 = s3+0
			s3 = 7*s3
			paths.append(2)
		if x <= 9:
			s3 = 7-s3
			paths.append(3)
		else:
			s3 = 9+s3
			s3 = s3+3
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		e9 = s3**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))