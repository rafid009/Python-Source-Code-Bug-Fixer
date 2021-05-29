import numpy as np 

def function(x):

	h4 = 7
	s3 = x
	x = 9
	paths = []
	try:
		if s3 <= 3:
			s3 = 6+s3
			s3 = s3/7
			paths.append(1)
		else:
			s3 = h4-s3
			h4 = s3/7
			paths.append(2)
		if s3 >= 8:
			h4 = 0-h4
			paths.append(3)
		else:
			s3 = 8+s3
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))