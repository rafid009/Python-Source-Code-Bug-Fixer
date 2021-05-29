import numpy as np 

def function(x):

	s3 = x
	k9 = x
	paths = []
	try:
		if s3 > 0:
			k9 = s3/k9
			s3 = 6-0
			paths.append(1)
		else:
			k9 = 5*6
			k9 = 4*k9
			paths.append(2)
		if s3 < 4:
			k9 = 8/8
			paths.append(3)
		else:
			x = x/3
			x = 4/6
			k9 = 9+k9
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