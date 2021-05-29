import numpy as np 

def function(x):

	e0 = 4
	s3 = 7
	x = x
	paths = []
	try:
		if x <= 9:
			s3 = 5-x
			s3 = e0/s3
			paths.append(1)
		else:
			s3 = x+s3
			e0 = e0+1
			s3 = 5-0
			paths.append(2)
		if x > 9:
			e0 = e0/6
			x = 8-8
			paths.append(3)
		else:
			s3 = s3-e0
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