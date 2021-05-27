import numpy as np 

def function(x):

	s3 = x
	l5 = x
	paths = []
	try:
		if l5 >= 4:
			l5 = l5/3
			s3 = 7-s3
			paths.append(1)
		else:
			l5 = 0+x
			paths.append(2)
		if s3 >= 8:
			s3 = s3*6
			l5 = 0/l5
			l5 = l5+8
			paths.append(3)
		else:
			x = 2+1
			x = s3*x
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))