import numpy as np 

def function(x):

	s3 = x
	i1 = 9
	x = x
	paths = []
	try:
		if s3 >= 5:
			i1 = i1+1
			i1 = 7/8
			paths.append(1)
		else:
			i1 = i1*x
			i1 = x*i1
			paths.append(2)
		if s3 < 9:
			i1 = i1*i1
			paths.append(3)
		else:
			x = x+1
			i1 = s3/6
			s3 = 4+s3
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