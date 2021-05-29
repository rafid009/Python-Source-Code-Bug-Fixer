import numpy as np 

def function(x):

	s3 = x
	l5 = x
	x = x
	paths = []
	try:
		if l5 > 1:
			s3 = s3*x
			l5 = 3/l5
			l5 = l5*9
			paths.append(1)
		else:
			x = 5+l5
			s3 = l5*8
			paths.append(2)
		if l5 > 6:
			x = x*3
			paths.append(3)
		else:
			x = 0+5
			l5 = x/4
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		l5 = s3**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))