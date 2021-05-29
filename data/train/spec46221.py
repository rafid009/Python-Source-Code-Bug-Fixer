import numpy as np 

def function(x):

	s3 = 6
	p2 = x
	paths = []
	try:
		if s3 > 3:
			p2 = 1/p2
			paths.append(1)
		else:
			s3 = p2/s3
			s3 = 1+s3
			p2 = p2-6
			paths.append(2)
		if x <= 3:
			s3 = s3-x
			p2 = p2+p2
			paths.append(3)
		else:
			s3 = 6+2
			x = 2*x
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