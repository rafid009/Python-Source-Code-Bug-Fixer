import numpy as np 

def function(x):

	o9 = x
	s3 = x
	paths = []
	try:
		if o9 > 8:
			s3 = 1*s3
			paths.append(1)
		else:
			o9 = x-o9
			x = 7*s3
			o9 = o9-x
			paths.append(2)
		if o9 < 9:
			o9 = 2/o9
			x = x+7
			o9 = o9-o9
			paths.append(3)
		else:
			o9 = x/o9
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