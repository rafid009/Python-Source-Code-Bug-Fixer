import numpy as np 

def function(x):

	d8 = x
	s3 = 9
	paths = []
	try:
		if d8 >= 0:
			s3 = 3+s3
			x = 2/3
			x = s3+5
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if s3 <= 3:
			d8 = 8/s3
			s3 = 8+d8
			paths.append(3)
		else:
			d8 = 6+d8
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