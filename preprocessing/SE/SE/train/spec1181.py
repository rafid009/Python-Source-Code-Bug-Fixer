import numpy as np 

def function(x):

	n5 = 4
	s3 = 7
	paths = []
	try:
		if s3 > 1:
			x = 8-x
			paths.append(1)
		else:
			x = x-2
			x = 2-s3
			s3 = s3*3
			paths.append(2)
		if x < 2:
			x = x*0
			s3 = s3*0
			x = 2+8
			paths.append(3)
		else:
			n5 = 0*s3
			n5 = 6+x
			x = 2-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))