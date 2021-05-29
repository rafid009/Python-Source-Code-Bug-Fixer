import numpy as np 

def function(x):

	i3 = x
	s3 = 2
	paths = []
	try:
		if i3 > 1:
			s3 = s3-x
			s3 = s3/3
			paths.append(1)
		else:
			i3 = x*s3
			s3 = i3-s3
			paths.append(2)
		if s3 <= 1:
			x = i3/i3
			s3 = 9-s3
			x = i3*x
			paths.append(3)
		else:
			i3 = 1-2
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