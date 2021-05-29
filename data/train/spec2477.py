import numpy as np 

def function(x):

	s3 = x
	v8 = x
	paths = []
	try:
		if v8 < 3:
			v8 = x-v8
			paths.append(1)
		else:
			s3 = v8+s3
			paths.append(2)
		if v8 < 0:
			s3 = 5+s3
			s3 = 4*s3
			s3 = 0+v8
			paths.append(3)
		else:
			s3 = 9-x
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