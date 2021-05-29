import numpy as np 

def function(x):

	w2 = 1
	s3 = 8
	paths = []
	try:
		if x < 5:
			s3 = 4+w2
			x = x-3
			paths.append(1)
		else:
			s3 = x-6
			paths.append(2)
		if w2 > 1:
			s3 = s3+6
			x = x*w2
			s3 = x-9
			paths.append(3)
		else:
			x = 1/w2
			s3 = 7-s3
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