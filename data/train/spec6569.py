import numpy as np 

def function(x):

	s3 = 1
	c6 = x
	paths = []
	try:
		if s3 <= 6:
			s3 = x+2
			x = x-6
			paths.append(1)
		else:
			c6 = c6/8
			x = x*6
			x = c6+s3
			paths.append(2)
		if x < 1:
			x = 5-x
			paths.append(3)
		else:
			c6 = 5*c6
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