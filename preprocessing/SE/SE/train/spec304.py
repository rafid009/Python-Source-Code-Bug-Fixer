import numpy as np 

def function(x):

	s3 = 9
	c7 = 3
	paths = []
	try:
		if s3 >= 3:
			c7 = s3*0
			paths.append(1)
		else:
			c7 = 1+c7
			c7 = c7/c7
			paths.append(2)
		if x < 6:
			c7 = c7+x
			x = 7/x
			paths.append(3)
		else:
			c7 = c7+s3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s3 = x**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))