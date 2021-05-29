import numpy as np 

def function(x):

	d6 = 1
	s3 = x
	paths = []
	try:
		if s3 > 9:
			d6 = d6+4
			paths.append(1)
		else:
			x = x+x
			d6 = s3-x
			paths.append(2)
		if d6 >= 7:
			x = x-6
			x = d6*x
			x = 1/x
			paths.append(3)
		else:
			s3 = s3/6
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