import numpy as np 

def function(x):

	s3 = x
	g8 = 5
	paths = []
	try:
		if s3 >= 3:
			g8 = 4-g8
			paths.append(1)
		else:
			g8 = 9*g8
			s3 = s3-7
			paths.append(2)
		if g8 <= 0:
			s3 = 2*s3
			g8 = g8+1
			g8 = g8-g8
			paths.append(3)
		else:
			g8 = g8+4
			g8 = g8-s3
			x = 4-g8
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