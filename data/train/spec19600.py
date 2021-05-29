import numpy as np 

def function(x):

	s2 = x
	s3 = x
	paths = []
	try:
		if s3 > 9:
			s2 = s2-0
			paths.append(1)
		else:
			s3 = s3-0
			x = x*2
			s3 = s3+4
			paths.append(2)
		if s3 > 9:
			s2 = 5-s2
			s2 = s2+0
			s3 = 3/8
			paths.append(3)
		else:
			s3 = 4-5
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