import numpy as np 

def function(x):

	a7 = 5
	s3 = 9
	paths = []
	try:
		if s3 <= 8:
			s3 = a7/8
			s3 = 2-s3
			paths.append(1)
		else:
			a7 = x+9
			s3 = a7/9
			a7 = a7-5
			paths.append(2)
		if a7 < 1:
			a7 = 0-a7
			s3 = x+5
			paths.append(3)
		else:
			s3 = a7-s3
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