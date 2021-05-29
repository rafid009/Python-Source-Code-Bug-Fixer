import numpy as np 

def function(x):

	s3 = 2
	g8 = x
	paths = []
	try:
		if x < 4:
			x = 7-x
			s3 = s3+g8
			x = x*7
			paths.append(1)
		else:
			s3 = s3/2
			paths.append(2)
		if s3 >= 7:
			x = 7/s3
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		g8 = s3**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))