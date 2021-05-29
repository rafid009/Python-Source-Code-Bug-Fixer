import numpy as np 

def function(x):

	s3 = x
	e7 = 6
	paths = []
	try:
		if x < 2:
			e7 = e7-x
			paths.append(1)
		else:
			s3 = e7+e7
			paths.append(2)
		if s3 > 1:
			e7 = 0+8
			x = x*9
			x = s3-s3
			paths.append(3)
		else:
			e7 = e7-0
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		x = s3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))