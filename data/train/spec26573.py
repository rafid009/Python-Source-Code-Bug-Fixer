import numpy as np 

def function(x):

	x0 = 7
	z6 = 1
	paths = []
	try:
		if x0 > 9:
			x = x-x
			z6 = x/x
			paths.append(1)
		else:
			z6 = x0/z6
			x0 = z6-5
			z6 = x/4
			paths.append(2)
		if x0 >= 1:
			x0 = 6/z6
			x0 = x0+x
			x = x0-x
			paths.append(3)
		else:
			x0 = x0-x
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