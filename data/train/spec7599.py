import numpy as np 

def function(x):

	s3 = 9
	i6 = 2
	paths = []
	try:
		if x > 2:
			x = 5/s3
			s3 = 6-s3
			paths.append(1)
		else:
			s3 = 7*s3
			s3 = s3+i6
			i6 = i6*9
			paths.append(2)
		if x < 2:
			s3 = s3-i6
			paths.append(3)
		else:
			x = x*7
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))