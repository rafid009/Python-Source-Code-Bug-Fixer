import numpy as np 

def function(x):

	w7 = x
	z1 = 1
	paths = []
	try:
		if z1 < 9:
			z1 = w7-z1
			w7 = 3+z1
			paths.append(1)
		else:
			z1 = z1+0
			paths.append(2)
		if z1 < 0:
			x = x/5
			z1 = z1-0
			paths.append(3)
		else:
			x = x-x
			w7 = 3-x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		z1 = w7**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))