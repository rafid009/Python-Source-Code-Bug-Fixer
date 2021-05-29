import numpy as np 

def function(x):

	s3 = 2
	l8 = x
	paths = []
	try:
		if s3 < 6:
			x = x/s3
			x = x+1
			paths.append(1)
		else:
			s3 = 3/l8
			paths.append(2)
		if s3 >= 2:
			l8 = l8+4
			x = x*8
			s3 = s3*4
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))