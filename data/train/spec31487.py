import numpy as np 

def function(x):

	k5 = x
	s3 = x
	paths = []
	try:
		if x <= 2:
			k5 = k5+s3
			paths.append(1)
		else:
			x = 9*7
			paths.append(2)
		if k5 < 4:
			k5 = 1-4
			k5 = k5+k5
			k5 = 9-8
			paths.append(3)
		else:
			s3 = s3-7
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		k5 = s3**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))