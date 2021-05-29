import numpy as np 

def function(x):

	s3 = 9
	v5 = 9
	paths = []
	try:
		if v5 <= 2:
			s3 = s3-8
			paths.append(1)
		else:
			x = x+s3
			v5 = v5-6
			paths.append(2)
		if s3 > 0:
			v5 = x+v5
			s3 = 0-s3
			paths.append(3)
		else:
			v5 = v5/s3
			s3 = s3-4
			s3 = s3*0
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		x = s3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))