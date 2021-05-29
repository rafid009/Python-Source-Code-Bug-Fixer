import numpy as np 

def function(x):

	s3 = 3
	f9 = x
	paths = []
	try:
		if x >= 8:
			s3 = f9-x
			s3 = s3/f9
			f9 = f9/8
			paths.append(1)
		else:
			x = 3+f9
			f9 = f9+8
			paths.append(2)
		if s3 < 5:
			f9 = 7-f9
			paths.append(3)
		else:
			f9 = f9-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))