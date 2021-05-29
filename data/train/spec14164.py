import numpy as np 

def function(x):

	s3 = 6
	f6 = 7
	paths = []
	try:
		if s3 <= 8:
			f6 = x+s3
			paths.append(1)
		else:
			s3 = s3-s3
			f6 = 1-1
			paths.append(2)
		if f6 > 6:
			s3 = f6/s3
			paths.append(3)
		else:
			s3 = 5-s3
			s3 = x*7
			s3 = 9+f6
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