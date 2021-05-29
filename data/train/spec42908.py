import numpy as np 

def function(x):

	s3 = x
	p3 = x
	paths = []
	try:
		if x > 5:
			x = p3+0
			p3 = s3*p3
			paths.append(1)
		else:
			s3 = s3-3
			paths.append(2)
		if x > 5:
			s3 = x-s3
			p3 = 0/x
			paths.append(3)
		else:
			x = x+s3
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