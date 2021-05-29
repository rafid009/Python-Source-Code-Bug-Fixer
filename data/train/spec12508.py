import numpy as np 

def function(x):

	e9 = 0
	s3 = 0
	paths = []
	try:
		if s3 > 5:
			x = s3+x
			s3 = s3*9
			e9 = s3+e9
			paths.append(1)
		else:
			s3 = 8-s3
			paths.append(2)
		if x >= 7:
			e9 = e9-8
			x = 3*0
			x = x/3
			paths.append(3)
		else:
			x = x-3
			s3 = e9+8
			s3 = 7+x
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