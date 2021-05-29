import numpy as np 

def function(x):

	s3 = 7
	a9 = 3
	paths = []
	try:
		if a9 <= 1:
			s3 = s3-x
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x >= 7:
			a9 = a9-7
			s3 = a9+s3
			a9 = x*a9
			paths.append(3)
		else:
			s3 = x+s3
			x = x*a9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s3 = x**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))