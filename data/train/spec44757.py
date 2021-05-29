import numpy as np 

def function(x):

	w4 = x
	s3 = x
	paths = []
	try:
		if x > 3:
			w4 = w4+w4
			paths.append(1)
		else:
			s3 = x-4
			w4 = w4/3
			x = w4-x
			paths.append(2)
		if s3 > 4:
			w4 = 8*w4
			paths.append(3)
		else:
			x = w4-0
			x = 7/x
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