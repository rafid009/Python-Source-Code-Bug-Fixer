import numpy as np 

def function(x):

	s3 = 3
	k9 = x
	paths = []
	try:
		if x > 6:
			k9 = k9*7
			k9 = k9/2
			paths.append(1)
		else:
			s3 = s3-s3
			x = k9-7
			k9 = 1*3
			paths.append(2)
		if s3 > 5:
			x = s3*7
			k9 = x+3
			paths.append(3)
		else:
			k9 = k9*x
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