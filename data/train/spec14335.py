import numpy as np 

def function(x):

	o2 = x
	s3 = 9
	x = x
	paths = []
	try:
		if s3 <= 0:
			s3 = s3-6
			o2 = o2-5
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x <= 1:
			s3 = 7+5
			x = s3/5
			x = s3-x
			paths.append(3)
		else:
			o2 = 2/o2
			s3 = 0/o2
			x = x/x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))