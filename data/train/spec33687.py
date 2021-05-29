import numpy as np 

def function(x):

	s3 = x
	d5 = x
	paths = []
	try:
		if s3 > 1:
			x = 5+1
			paths.append(1)
		else:
			d5 = 6/d5
			paths.append(2)
		if s3 > 1:
			d5 = s3+7
			s3 = x-s3
			x = 5/x
			paths.append(3)
		else:
			d5 = 8*d5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))