import numpy as np 

def function(x):

	a4 = 4
	s3 = 7
	paths = []
	try:
		if s3 < 3:
			s3 = s3*a4
			x = 6-x
			x = x+s3
			paths.append(1)
		else:
			a4 = a4-a4
			paths.append(2)
		if s3 > 6:
			a4 = 4+a4
			a4 = a4-0
			a4 = 7-x
			paths.append(3)
		else:
			s3 = s3*8
			s3 = 3-a4
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))