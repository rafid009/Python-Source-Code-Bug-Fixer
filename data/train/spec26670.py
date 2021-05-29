import numpy as np 

def function(x):

	s3 = 3
	d1 = 0
	paths = []
	try:
		if s3 >= 5:
			d1 = d1*9
			d1 = 1*d1
			paths.append(1)
		else:
			s3 = s3*7
			paths.append(2)
		if d1 > 1:
			x = 5-x
			paths.append(3)
		else:
			x = d1-1
			d1 = d1-s3
			s3 = s3+x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))