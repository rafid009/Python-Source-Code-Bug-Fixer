import numpy as np 

def function(x):

	s3 = x
	b6 = x
	paths = []
	try:
		if s3 > 9:
			x = x*x
			b6 = s3+x
			b6 = b6*s3
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if s3 > 0:
			b6 = 6/b6
			b6 = 1*3
			s3 = 0-6
			paths.append(3)
		else:
			s3 = s3+3
			x = 4/b6
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