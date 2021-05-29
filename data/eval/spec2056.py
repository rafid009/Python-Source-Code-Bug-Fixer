import numpy as np 

def function(x):

	s3 = x
	e3 = 0
	paths = []
	try:
		if x > 6:
			s3 = 5*s3
			e3 = x+9
			x = x-3
			paths.append(1)
		else:
			x = x-2
			e3 = e3+6
			paths.append(2)
		if x < 7:
			e3 = 2*7
			s3 = s3-3
			s3 = s3+2
			paths.append(3)
		else:
			e3 = 0+8
			s3 = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))