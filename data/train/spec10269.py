import numpy as np 

def function(x):

	z5 = 9
	v0 = 8
	paths = []
	try:
		if x >= 1:
			v0 = 8*8
			v0 = 7/4
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if z5 > 0:
			x = x-2
			v0 = 8-v0
			z5 = 6-z5
			paths.append(3)
		else:
			v0 = v0-6
			z5 = z5*z5
			v0 = v0/2
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))