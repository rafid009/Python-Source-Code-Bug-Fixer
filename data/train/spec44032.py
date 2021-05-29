import numpy as np 

def function(x):

	z5 = 7
	x2 = x
	paths = []
	try:
		if x2 > 6:
			x2 = x-x2
			x = z5+x2
			paths.append(1)
		else:
			x = x+8
			x2 = 5*z5
			paths.append(2)
		if x >= 6:
			x2 = x2-1
			x = 0*x
			paths.append(3)
		else:
			z5 = 6-z5
			x = 3*5
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		z5 = x2**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))