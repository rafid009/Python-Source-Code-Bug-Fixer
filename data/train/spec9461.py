import numpy as np 

def function(x):

	s3 = x
	a9 = 3
	paths = []
	try:
		if s3 > 4:
			a9 = s3-a9
			a9 = a9+s3
			paths.append(1)
		else:
			a9 = a9*1
			paths.append(2)
		if x < 0:
			s3 = 6+s3
			x = 2-3
			a9 = s3-0
			paths.append(3)
		else:
			s3 = 9*s3
			a9 = a9+9
			a9 = a9/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))