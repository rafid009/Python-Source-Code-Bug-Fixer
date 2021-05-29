import numpy as np 

def function(x):

	s3 = x
	a0 = 3
	paths = []
	try:
		if a0 <= 0:
			x = x/s3
			paths.append(1)
		else:
			a0 = s3-8
			x = a0+x
			paths.append(2)
		if s3 > 2:
			x = 7*x
			x = x*x
			paths.append(3)
		else:
			a0 = a0*8
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		s3 = s3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))