import numpy as np 

def function(x):

	s3 = 9
	j4 = 5
	paths = []
	try:
		if x < 0:
			x = x-2
			s3 = s3+5
			x = x+4
			paths.append(1)
		else:
			x = j4*s3
			paths.append(2)
		if s3 < 2:
			j4 = 6+j4
			paths.append(3)
		else:
			j4 = s3-4
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