import numpy as np 

def function(x):

	y5 = x
	s3 = 0
	x = 1
	paths = []
	try:
		if x <= 0:
			x = 4*3
			paths.append(1)
		else:
			s3 = s3/2
			paths.append(2)
		if s3 > 5:
			x = 5*7
			paths.append(3)
		else:
			x = x/y5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))