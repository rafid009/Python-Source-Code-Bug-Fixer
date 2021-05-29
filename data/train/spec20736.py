import numpy as np 

def function(x):

	s3 = 5
	f3 = 2
	paths = []
	try:
		if x <= 7:
			x = x*f3
			s3 = x-s3
			s3 = f3-s3
			paths.append(1)
		else:
			f3 = 0-s3
			f3 = 3-f3
			paths.append(2)
		if f3 >= 9:
			f3 = s3-f3
			paths.append(3)
		else:
			f3 = f3-f3
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		f3 = s3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))