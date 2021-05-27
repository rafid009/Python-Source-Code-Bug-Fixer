import numpy as np 

def function(x):

	s3 = 0
	s0 = 4
	paths = []
	try:
		if s3 < 4:
			s3 = x/8
			paths.append(1)
		else:
			x = x/1
			s0 = s0*9
			paths.append(2)
		if s0 >= 9:
			s0 = 9/x
			paths.append(3)
		else:
			x = s3*x
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		x = s3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))