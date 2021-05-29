import numpy as np 

def function(x):

	k8 = 6
	z5 = 8
	paths = []
	try:
		if x >= 2:
			z5 = 3-z5
			paths.append(1)
		else:
			x = k8+x
			z5 = z5-z5
			paths.append(2)
		if z5 < 1:
			x = z5+x
			paths.append(3)
		else:
			k8 = k8+4
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