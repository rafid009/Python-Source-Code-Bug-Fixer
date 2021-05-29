import numpy as np 

def function(x):

	e4 = x
	s3 = 6
	paths = []
	try:
		if s3 <= 3:
			x = x-7
			s3 = 8-2
			paths.append(1)
		else:
			s3 = s3/e4
			s3 = s3*8
			paths.append(2)
		if e4 >= 5:
			e4 = 4-x
			e4 = e4-0
			paths.append(3)
		else:
			e4 = 7/e4
			x = e4+s3
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))