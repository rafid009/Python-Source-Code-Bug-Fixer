import numpy as np 

def function(x):

	s3 = x
	t5 = 6
	paths = []
	try:
		if t5 >= 4:
			x = 1/s3
			s3 = s3*2
			paths.append(1)
		else:
			x = 1/x
			s3 = x*2
			s3 = 3/5
			paths.append(2)
		if x <= 6:
			s3 = 8+s3
			paths.append(3)
		else:
			t5 = s3-x
			s3 = s3-5
			t5 = 4/5
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