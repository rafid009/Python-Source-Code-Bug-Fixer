import numpy as np 

def function(x):

	w1 = 3
	s3 = 5
	paths = []
	try:
		if s3 <= 9:
			s3 = s3-1
			s3 = 1/9
			paths.append(1)
		else:
			w1 = w1-x
			w1 = 5/w1
			paths.append(2)
		if s3 >= 6:
			s3 = s3-6
			x = 6*x
			x = s3*4
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))