import numpy as np 

def function(x):

	s3 = 4
	s6 = x
	paths = []
	try:
		if s3 <= 0:
			s6 = s3*s3
			s6 = 8*0
			paths.append(1)
		else:
			s3 = s6+6
			paths.append(2)
		if s3 <= 3:
			x = 4-s6
			s6 = 4-s6
			s6 = 4-9
			paths.append(3)
		else:
			s6 = s6/s3
			s3 = x/6
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))