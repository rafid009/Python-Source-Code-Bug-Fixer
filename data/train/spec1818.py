import numpy as np 

def function(x):

	s3 = 1
	b0 = x
	paths = []
	try:
		if s3 >= 4:
			x = b0*8
			x = x-4
			paths.append(1)
		else:
			s3 = s3/6
			b0 = b0+b0
			paths.append(2)
		if b0 > 0:
			x = x+s3
			b0 = b0-b0
			paths.append(3)
		else:
			s3 = 2+2
			b0 = b0-5
			b0 = b0-b0
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