import numpy as np 

def function(x):

	s3 = 0
	k2 = 2
	paths = []
	try:
		if x < 1:
			s3 = 2-2
			k2 = x*k2
			paths.append(1)
		else:
			s3 = 9*k2
			paths.append(2)
		if k2 >= 0:
			s3 = 6-2
			paths.append(3)
		else:
			x = 2/k2
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))