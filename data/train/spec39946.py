import numpy as np 

def function(x):

	s3 = 1
	g9 = 3
	paths = []
	try:
		if s3 >= 1:
			g9 = g9*2
			g9 = g9+s3
			x = x*9
			paths.append(1)
		else:
			s3 = 7/2
			s3 = s3/7
			g9 = 5-g9
			paths.append(2)
		if s3 >= 4:
			s3 = 6-x
			x = x-1
			x = x-1
			paths.append(3)
		else:
			g9 = g9/3
			s3 = 5/s3
			g9 = g9-9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		s3 = g9**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))