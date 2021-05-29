import numpy as np 

def function(x):

	s3 = x
	u3 = 7
	paths = []
	try:
		if s3 > 3:
			x = 8-x
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if u3 <= 2:
			x = x-x
			x = 0/x
			paths.append(3)
		else:
			u3 = s3-3
			x = u3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s3 = x**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))