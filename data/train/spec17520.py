import numpy as np 

def function(x):

	z5 = x
	x1 = x
	paths = []
	try:
		if x1 < 5:
			z5 = z5+4
			x1 = 3-x
			paths.append(1)
		else:
			x1 = 3/x
			x = 4+x
			x = 6*3
			paths.append(2)
		if x1 >= 4:
			x = x*x
			paths.append(3)
		else:
			x = 0*x
			z5 = z5/7
			z5 = 7-z5
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))