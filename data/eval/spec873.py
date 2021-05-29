import numpy as np 

def function(x):

	s3 = x
	t0 = 8
	paths = []
	try:
		if x < 2:
			x = s3-5
			t0 = 7-4
			t0 = t0*6
			paths.append(1)
		else:
			t0 = 0-t0
			t0 = t0/9
			paths.append(2)
		if t0 <= 4:
			t0 = 2/t0
			t0 = 7/3
			t0 = s3/t0
			paths.append(3)
		else:
			x = 7/1
			s3 = 4+s3
			t0 = t0/t0
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