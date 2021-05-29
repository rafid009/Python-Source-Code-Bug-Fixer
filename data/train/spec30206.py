import numpy as np 

def function(x):

	p4 = 1
	s3 = 8
	x = 9
	paths = []
	try:
		if p4 <= 1:
			p4 = p4/x
			p4 = 2*p4
			x = s3/9
			paths.append(1)
		else:
			s3 = 0-2
			s3 = p4/s3
			s3 = 8+p4
			paths.append(2)
		if p4 <= 5:
			p4 = 6+p4
			x = x-s3
			x = 5/x
			paths.append(3)
		else:
			s3 = 1+x
			x = x*6
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