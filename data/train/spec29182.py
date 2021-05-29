import numpy as np 

def function(x):

	h8 = 9
	s3 = 1
	paths = []
	try:
		if s3 <= 4:
			h8 = h8+7
			paths.append(1)
		else:
			h8 = h8*x
			paths.append(2)
		if x <= 4:
			s3 = 0-s3
			paths.append(3)
		else:
			h8 = s3+h8
			s3 = 6+3
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