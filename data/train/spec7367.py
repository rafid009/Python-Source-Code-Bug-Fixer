import numpy as np 

def function(x):

	s3 = 8
	f7 = x
	x = 1
	paths = []
	try:
		if s3 < 1:
			s3 = s3/s3
			f7 = f7-5
			paths.append(1)
		else:
			f7 = f7-5
			paths.append(2)
		if f7 >= 1:
			f7 = 6*6
			x = x*x
			paths.append(3)
		else:
			f7 = 0-s3
			s3 = s3+7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))