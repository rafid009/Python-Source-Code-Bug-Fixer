import numpy as np 

def function(x):

	p8 = 4
	s3 = 7
	paths = []
	try:
		if s3 > 7:
			p8 = 6*x
			p8 = 9/p8
			paths.append(1)
		else:
			p8 = p8-9
			p8 = p8+x
			paths.append(2)
		if x > 8:
			x = p8-x
			paths.append(3)
		else:
			s3 = 1/s3
			p8 = p8+7
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