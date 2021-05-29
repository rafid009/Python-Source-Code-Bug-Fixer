import numpy as np 

def function(x):

	s3 = x
	v2 = x
	paths = []
	try:
		if s3 <= 1:
			v2 = v2-x
			v2 = v2+v2
			paths.append(1)
		else:
			v2 = s3-1
			x = x-x
			paths.append(2)
		if s3 >= 8:
			x = x-v2
			x = 2+x
			x = x*5
			paths.append(3)
		else:
			v2 = v2+v2
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		s3 = s3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))