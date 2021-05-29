import numpy as np 

def function(x):

	x7 = 4
	s3 = 9
	paths = []
	try:
		if x7 <= 6:
			x7 = 7-8
			s3 = s3-9
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if x7 <= 0:
			x = x*6
			x = x*5
			s3 = s3/9
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))