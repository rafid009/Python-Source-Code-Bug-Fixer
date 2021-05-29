import numpy as np 

def function(x):

	s3 = 4
	p9 = 0
	paths = []
	try:
		if x <= 6:
			s3 = x/8
			p9 = s3-p9
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if s3 <= 0:
			p9 = 5*6
			paths.append(3)
		else:
			s3 = s3+3
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