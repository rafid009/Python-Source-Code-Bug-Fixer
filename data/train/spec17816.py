import numpy as np 

def function(x):

	d1 = x
	s3 = 3
	paths = []
	try:
		if x > 2:
			s3 = 6-8
			d1 = d1-6
			d1 = d1/x
			paths.append(1)
		else:
			s3 = s3+x
			x = x*9
			s3 = x/6
			paths.append(2)
		if x <= 2:
			x = x/x
			paths.append(3)
		else:
			d1 = s3*d1
			x = 9-d1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))