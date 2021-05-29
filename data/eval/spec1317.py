import numpy as np 

def function(x):

	k0 = 5
	s3 = x
	paths = []
	try:
		if x < 5:
			k0 = k0-x
			x = x+s3
			paths.append(1)
		else:
			x = 3*x
			x = x+1
			s3 = x+s3
			paths.append(2)
		if s3 >= 0:
			s3 = s3-6
			paths.append(3)
		else:
			k0 = x+k0
			x = x+0
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		x = s3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))