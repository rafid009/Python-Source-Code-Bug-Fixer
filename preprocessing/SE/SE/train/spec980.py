import numpy as np 

def function(x):

	k6 = 7
	s3 = x
	paths = []
	try:
		if x <= 8:
			k6 = 0-k6
			paths.append(1)
		else:
			k6 = k6*x
			k6 = k6/7
			k6 = k6+k6
			paths.append(2)
		if s3 < 1:
			x = 8/x
			x = s3-s3
			paths.append(3)
		else:
			k6 = 4/7
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		k6 = s3**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))