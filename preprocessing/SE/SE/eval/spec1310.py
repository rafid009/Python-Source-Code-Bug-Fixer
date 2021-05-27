import numpy as np 

def function(x):

	z6 = 4
	k7 = x
	paths = []
	try:
		if k7 >= 2:
			z6 = z6-4
			paths.append(1)
		else:
			k7 = k7-3
			paths.append(2)
		if z6 < 2:
			k7 = 3-x
			k7 = 3/k7
			paths.append(3)
		else:
			k7 = 2-k7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))