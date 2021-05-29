import numpy as np 

def function(x):

	s3 = 5
	k1 = 6
	paths = []
	try:
		if x < 0:
			k1 = k1+k1
			k1 = 8+k1
			paths.append(1)
		else:
			x = 6+6
			paths.append(2)
		if x <= 3:
			s3 = 7*s3
			paths.append(3)
		else:
			x = x*8
			s3 = s3-4
			k1 = 5-k1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))