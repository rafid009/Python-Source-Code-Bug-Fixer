import numpy as np 

def function(x):

	s3 = 3
	b0 = x
	paths = []
	try:
		if b0 > 5:
			s3 = s3-8
			s3 = s3*b0
			paths.append(1)
		else:
			b0 = b0/2
			b0 = 8*b0
			b0 = b0-4
			paths.append(2)
		if x < 1:
			s3 = s3+x
			b0 = b0/b0
			paths.append(3)
		else:
			b0 = s3*4
			b0 = 6-1
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		b0 = s3**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))