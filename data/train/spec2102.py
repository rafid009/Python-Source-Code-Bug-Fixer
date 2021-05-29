import numpy as np 

def function(x):

	h9 = 4
	s3 = x
	x = 9
	paths = []
	try:
		if h9 >= 7:
			s3 = s3/s3
			s3 = s3-h9
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x > 3:
			h9 = h9/6
			paths.append(3)
		else:
			s3 = s3+1
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