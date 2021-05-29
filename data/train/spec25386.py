import numpy as np 

def function(x):

	e8 = 9
	s3 = 1
	paths = []
	try:
		if s3 > 0:
			e8 = e8-x
			paths.append(1)
		else:
			e8 = 0/4
			x = 6/x
			s3 = s3+0
			paths.append(2)
		if e8 <= 3:
			s3 = 5/s3
			paths.append(3)
		else:
			x = 1/x
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