import numpy as np 

def function(x):

	v3 = x
	s3 = 4
	paths = []
	try:
		if v3 >= 9:
			v3 = 7*9
			paths.append(1)
		else:
			x = 8*x
			x = x/7
			s3 = 9+9
			paths.append(2)
		if s3 < 7:
			s3 = s3*3
			s3 = s3+5
			x = s3*v3
			paths.append(3)
		else:
			x = 1*s3
			v3 = 9*v3
			x = x-s3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		s3 = v3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))