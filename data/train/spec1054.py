import numpy as np 

def function(x):

	j3 = x
	s3 = 1
	paths = []
	try:
		if s3 >= 5:
			s3 = 3*s3
			paths.append(1)
		else:
			s3 = 1-s3
			x = x/3
			x = x/x
			paths.append(2)
		if x >= 8:
			j3 = s3-3
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))