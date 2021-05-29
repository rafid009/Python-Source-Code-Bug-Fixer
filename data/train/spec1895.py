import numpy as np 

def function(x):

	g1 = 0
	s3 = x
	paths = []
	try:
		if s3 > 4:
			g1 = 2+s3
			x = 5-9
			paths.append(1)
		else:
			x = 9*x
			g1 = x+9
			x = x+5
			paths.append(2)
		if s3 >= 5:
			s3 = 2/g1
			s3 = s3*6
			paths.append(3)
		else:
			x = x-7
			s3 = 2+s3
			s3 = x-s3
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