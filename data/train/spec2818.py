import numpy as np 

def function(x):

	u2 = x
	z0 = x
	paths = []
	try:
		if z0 > 1:
			u2 = 9+u2
			x = x/x
			paths.append(1)
		else:
			x = 9-7
			paths.append(2)
		if x <= 8:
			x = x-2
			u2 = u2-7
			u2 = 2+u2
			paths.append(3)
		else:
			z0 = z0/6
			u2 = u2/u2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))