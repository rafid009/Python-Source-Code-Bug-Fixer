import numpy as np 

def function(x):

	s3 = 1
	i1 = x
	x = 0
	paths = []
	try:
		if s3 < 2:
			i1 = 2+i1
			s3 = 4-s3
			x = 6*i1
			paths.append(1)
		else:
			s3 = x-2
			i1 = i1-1
			x = 2-i1
			paths.append(2)
		if x > 8:
			i1 = i1*s3
			s3 = s3-2
			x = 2*x
			paths.append(3)
		else:
			s3 = s3-4
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))