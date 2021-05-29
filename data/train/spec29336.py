import numpy as np 

def function(x):

	s3 = 7
	o2 = 9
	paths = []
	try:
		if s3 > 6:
			s3 = s3*s3
			o2 = 8-o2
			paths.append(1)
		else:
			x = 6/4
			o2 = 3+o2
			o2 = x-4
			paths.append(2)
		if o2 >= 8:
			x = s3*x
			paths.append(3)
		else:
			o2 = s3-o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))