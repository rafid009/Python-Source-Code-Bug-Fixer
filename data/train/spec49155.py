import numpy as np 

def function(x):

	z5 = x
	x2 = 6
	paths = []
	try:
		if x2 <= 2:
			x = x*3
			paths.append(1)
		else:
			z5 = z5/8
			x2 = 6/z5
			paths.append(2)
		if z5 >= 3:
			x = x*z5
			z5 = z5*7
			paths.append(3)
		else:
			x = 2*x
			x = x-z5
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))