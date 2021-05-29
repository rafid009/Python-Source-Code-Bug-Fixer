import numpy as np 

def function(x):

	s3 = 1
	j8 = 5
	x = x
	paths = []
	try:
		if s3 >= 3:
			x = x/s3
			paths.append(1)
		else:
			j8 = j8*5
			paths.append(2)
		if x < 2:
			s3 = x/7
			j8 = j8*s3
			paths.append(3)
		else:
			x = x-8
			j8 = 1/j8
			x = x*3
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