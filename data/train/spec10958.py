import numpy as np 

def function(x):

	x0 = x
	z5 = x
	x = 7
	paths = []
	try:
		if x0 >= 7:
			x = x0/x
			x0 = 2*z5
			paths.append(1)
		else:
			x0 = x0-2
			x = x/9
			paths.append(2)
		if x <= 7:
			z5 = 6/x0
			x0 = x0+x0
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))