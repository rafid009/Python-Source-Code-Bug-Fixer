import numpy as np 

def function(x):

	s3 = x
	t6 = x
	paths = []
	try:
		if t6 < 3:
			s3 = s3/4
			paths.append(1)
		else:
			s3 = s3+s3
			x = x+t6
			paths.append(2)
		if s3 >= 9:
			x = x+s3
			t6 = 8*0
			paths.append(3)
		else:
			s3 = s3-0
			s3 = s3+t6
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