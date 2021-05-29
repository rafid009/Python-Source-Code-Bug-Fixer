import numpy as np 

def function(x):

	w1 = 5
	s3 = 7
	paths = []
	try:
		if w1 <= 9:
			x = w1+w1
			w1 = s3*w1
			s3 = s3-w1
			paths.append(1)
		else:
			x = x*x
			w1 = 3+w1
			s3 = s3*5
			paths.append(2)
		if x < 0:
			s3 = s3*3
			paths.append(3)
		else:
			w1 = w1+7
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