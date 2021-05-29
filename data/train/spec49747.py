import numpy as np 

def function(x):

	s3 = x
	j0 = x
	x = x
	paths = []
	try:
		if x >= 5:
			j0 = j0/s3
			x = x*1
			paths.append(1)
		else:
			x = 8-0
			paths.append(2)
		if s3 <= 6:
			x = 8+x
			x = j0+1
			paths.append(3)
		else:
			j0 = j0-4
			s3 = x*s3
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		s3 = j0**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))