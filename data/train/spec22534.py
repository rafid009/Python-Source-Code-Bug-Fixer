import numpy as np 

def function(x):

	j1 = x
	s3 = x
	paths = []
	try:
		if s3 < 2:
			x = x+s3
			x = 1/j1
			x = 7*s3
			paths.append(1)
		else:
			j1 = 4+x
			paths.append(2)
		if j1 <= 6:
			j1 = 2+j1
			s3 = 3-s3
			paths.append(3)
		else:
			j1 = j1-6
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