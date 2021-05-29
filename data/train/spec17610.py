import numpy as np 

def function(x):

	w5 = x
	s3 = 9
	paths = []
	try:
		if w5 <= 8:
			s3 = x/s3
			paths.append(1)
		else:
			w5 = x*w5
			w5 = 3+w5
			paths.append(2)
		if x > 8:
			x = 5-s3
			s3 = s3+8
			s3 = s3+3
			paths.append(3)
		else:
			w5 = w5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))