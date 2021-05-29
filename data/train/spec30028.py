import numpy as np 

def function(x):

	s3 = x
	g9 = x
	paths = []
	try:
		if s3 >= 2:
			x = x+9
			paths.append(1)
		else:
			x = 2-x
			x = s3-5
			paths.append(2)
		if g9 <= 6:
			s3 = 1/s3
			x = g9+x
			s3 = s3*x
			paths.append(3)
		else:
			g9 = g9-7
			g9 = g9*5
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))