import numpy as np 

def function(x):

	s3 = x
	w2 = 1
	paths = []
	try:
		if x >= 5:
			x = 0/x
			w2 = 2+w2
			paths.append(1)
		else:
			x = s3-7
			s3 = 9/s3
			paths.append(2)
		if s3 > 3:
			w2 = 2+x
			x = x*6
			paths.append(3)
		else:
			x = x-w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		s3 = w2**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))