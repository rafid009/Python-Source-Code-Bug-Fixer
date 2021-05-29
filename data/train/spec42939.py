import numpy as np 

def function(x):

	a0 = x
	z0 = 8
	paths = []
	try:
		if a0 <= 2:
			a0 = a0*a0
			paths.append(1)
		else:
			x = x/5
			z0 = 9+9
			paths.append(2)
		if z0 >= 7:
			a0 = 9+a0
			x = 8/x
			paths.append(3)
		else:
			z0 = 1-6
			x = 7*5
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