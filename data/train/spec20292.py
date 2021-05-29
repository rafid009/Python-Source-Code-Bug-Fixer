import numpy as np 

def function(x):

	k3 = 1
	z7 = x
	paths = []
	try:
		if z7 <= 6:
			z7 = z7*5
			k3 = x+z7
			paths.append(1)
		else:
			x = 9+z7
			z7 = 6-4
			paths.append(2)
		if k3 <= 9:
			z7 = z7-6
			x = 5+z7
			k3 = 6+x
			paths.append(3)
		else:
			x = x-3
			z7 = z7+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))