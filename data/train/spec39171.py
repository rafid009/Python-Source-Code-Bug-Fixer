import numpy as np 

def function(x):

	s3 = x
	k9 = x
	paths = []
	try:
		if s3 > 1:
			x = 6/x
			s3 = k9+k9
			paths.append(1)
		else:
			s3 = s3-s3
			paths.append(2)
		if k9 > 3:
			s3 = 4+3
			paths.append(3)
		else:
			s3 = 7+3
			x = x/x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))