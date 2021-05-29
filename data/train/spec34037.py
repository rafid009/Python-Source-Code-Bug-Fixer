import numpy as np 

def function(x):

	s3 = x
	b7 = 1
	paths = []
	try:
		if x <= 9:
			b7 = b7+x
			paths.append(1)
		else:
			x = 9-2
			b7 = x*1
			paths.append(2)
		if s3 > 2:
			s3 = 4-s3
			x = x+s3
			paths.append(3)
		else:
			x = x*4
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