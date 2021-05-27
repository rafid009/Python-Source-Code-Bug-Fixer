import numpy as np 

def function(x):

	a2 = 2
	s3 = 1
	x = 7
	paths = []
	try:
		if x >= 4:
			a2 = x-6
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if s3 <= 6:
			s3 = 0-s3
			paths.append(3)
		else:
			s3 = s3+x
			x = a2/9
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		s3 = s3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))