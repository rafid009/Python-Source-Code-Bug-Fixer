import numpy as np 

def function(x):

	n1 = 3
	s3 = 0
	paths = []
	try:
		if x <= 3:
			n1 = n1+9
			paths.append(1)
		else:
			n1 = n1-9
			n1 = n1+n1
			s3 = 4-s3
			paths.append(2)
		if s3 <= 0:
			x = s3/n1
			x = 0*x
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))