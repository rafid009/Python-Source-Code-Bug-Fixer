import numpy as np 

def function(x):

	s3 = x
	k5 = 8
	x = x
	paths = []
	try:
		if s3 < 9:
			k5 = s3+1
			s3 = 2*9
			k5 = k5-5
			paths.append(1)
		else:
			k5 = k5/8
			paths.append(2)
		if x < 4:
			x = k5-x
			s3 = k5+1
			x = 2+k5
			paths.append(3)
		else:
			s3 = s3*7
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))