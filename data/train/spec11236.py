import numpy as np 

def function(x):

	v9 = 2
	s3 = x
	paths = []
	try:
		if v9 >= 5:
			s3 = 8+s3
			v9 = v9+8
			paths.append(1)
		else:
			s3 = 1*1
			v9 = s3/4
			paths.append(2)
		if v9 > 1:
			s3 = s3+4
			paths.append(3)
		else:
			s3 = v9+x
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))