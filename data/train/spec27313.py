import numpy as np 

def function(x):

	e5 = x
	s3 = 9
	paths = []
	try:
		if s3 >= 3:
			s3 = s3/s3
			paths.append(1)
		else:
			s3 = 0+s3
			paths.append(2)
		if e5 < 2:
			e5 = 9/e5
			s3 = s3*9
			x = x-x
			paths.append(3)
		else:
			x = x*e5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))