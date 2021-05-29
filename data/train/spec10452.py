import numpy as np 

def function(x):

	l7 = 3
	s3 = 3
	paths = []
	try:
		if x <= 1:
			l7 = 9*l7
			x = x+4
			l7 = 9-l7
			paths.append(1)
		else:
			l7 = 7/x
			s3 = 5+s3
			paths.append(2)
		if l7 <= 1:
			x = x/x
			x = 9/2
			l7 = l7+l7
			paths.append(3)
		else:
			l7 = 6-s3
			x = 1+0
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))