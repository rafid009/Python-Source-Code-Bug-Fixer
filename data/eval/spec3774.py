import numpy as np 

def function(x):

	s3 = x
	c4 = x
	paths = []
	try:
		if x <= 5:
			s3 = 7*x
			paths.append(1)
		else:
			s3 = s3+x
			x = c4-3
			s3 = 1-1
			paths.append(2)
		if c4 < 5:
			x = 2*x
			s3 = c4+8
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))