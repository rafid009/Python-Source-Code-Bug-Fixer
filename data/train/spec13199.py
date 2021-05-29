import numpy as np 

def function(x):

	g8 = x
	s3 = x
	paths = []
	try:
		if x >= 5:
			s3 = 3+s3
			g8 = 3+3
			s3 = 2/x
			paths.append(1)
		else:
			g8 = g8/g8
			x = x-0
			paths.append(2)
		if s3 <= 0:
			x = 9*s3
			s3 = 8*2
			g8 = 5-x
			paths.append(3)
		else:
			g8 = 5*s3
			g8 = 6-8
			g8 = s3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))