import numpy as np 

def function(x):

	q4 = 1
	s3 = x
	paths = []
	try:
		if x < 1:
			x = 9+3
			x = x+5
			paths.append(1)
		else:
			x = 9/4
			x = x/1
			x = 8-0
			paths.append(2)
		if x >= 7:
			x = q4+q4
			x = x*x
			x = x+5
			paths.append(3)
		else:
			s3 = s3-3
			q4 = 1*q4
			q4 = q4/5
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