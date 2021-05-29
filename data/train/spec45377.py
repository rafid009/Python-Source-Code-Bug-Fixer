import numpy as np 

def function(x):

	a5 = x
	s3 = x
	paths = []
	try:
		if x > 9:
			x = s3*2
			s3 = a5*s3
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if s3 <= 2:
			a5 = a5*5
			s3 = 7-s3
			paths.append(3)
		else:
			x = 0+1
			a5 = s3/1
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		s3 = a5**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))