import numpy as np 

def function(x):

	s3 = x
	b9 = 6
	paths = []
	try:
		if s3 >= 0:
			s3 = s3*3
			x = x/s3
			paths.append(1)
		else:
			b9 = s3/b9
			x = x+3
			paths.append(2)
		if b9 >= 9:
			x = s3-8
			b9 = b9+x
			paths.append(3)
		else:
			b9 = 5-8
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))