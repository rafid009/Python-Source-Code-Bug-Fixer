import numpy as np 

def function(x):

	s3 = 2
	h9 = x
	paths = []
	try:
		if x > 9:
			h9 = x*h9
			h9 = 9+h9
			s3 = 1*s3
			paths.append(1)
		else:
			h9 = 1*h9
			s3 = 5-h9
			paths.append(2)
		if h9 <= 6:
			s3 = s3+5
			paths.append(3)
		else:
			x = 0/x
			h9 = x-h9
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		h9 = s3**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))