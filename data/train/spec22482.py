import numpy as np 

def function(x):

	s3 = x
	t5 = 3
	paths = []
	try:
		if t5 < 5:
			s3 = 0+s3
			s3 = x-t5
			paths.append(1)
		else:
			s3 = s3/3
			paths.append(2)
		if t5 <= 5:
			s3 = s3-5
			t5 = t5*s3
			x = t5*x
			paths.append(3)
		else:
			x = 0-6
			x = t5-s3
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))