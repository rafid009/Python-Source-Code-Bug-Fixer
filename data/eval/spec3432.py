import numpy as np 

def function(x):

	s3 = x
	t0 = 8
	paths = []
	try:
		if x <= 5:
			t0 = t0+1
			x = x*9
			t0 = 3+t0
			paths.append(1)
		else:
			t0 = t0+t0
			x = t0*x
			paths.append(2)
		if t0 > 2:
			x = 8*s3
			paths.append(3)
		else:
			t0 = 4*t0
			x = t0-x
			x = 1/t0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s3 = x**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))