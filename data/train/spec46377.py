import numpy as np 

def function(x):

	s3 = 3
	f0 = 5
	x = 4
	paths = []
	try:
		if s3 < 7:
			f0 = f0-9
			s3 = s3*1
			x = s3*x
			paths.append(1)
		else:
			s3 = s3+f0
			s3 = s3+f0
			f0 = f0/4
			paths.append(2)
		if f0 > 0:
			s3 = 6*s3
			f0 = f0/8
			paths.append(3)
		else:
			s3 = s3+9
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))