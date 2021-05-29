import numpy as np 

def function(x):

	o7 = x
	s3 = 1
	paths = []
	try:
		if s3 >= 4:
			x = 6*x
			paths.append(1)
		else:
			o7 = o7/9
			s3 = 4-6
			paths.append(2)
		if s3 >= 3:
			x = x+x
			s3 = s3-o7
			paths.append(3)
		else:
			x = 0/2
			s3 = s3+4
			o7 = o7+2
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		s3 = o7**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))