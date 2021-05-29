import numpy as np 

def function(x):

	s3 = 6
	w4 = 0
	paths = []
	try:
		if x <= 9:
			s3 = x+s3
			w4 = w4+9
			s3 = 1-s3
			paths.append(1)
		else:
			w4 = 3/s3
			paths.append(2)
		if s3 < 8:
			s3 = w4+x
			w4 = w4*x
			paths.append(3)
		else:
			s3 = 7*s3
			x = s3+1
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		w4 = s3**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))