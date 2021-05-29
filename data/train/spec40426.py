import numpy as np 

def function(x):

	z7 = 5
	k0 = x
	paths = []
	try:
		if x <= 1:
			k0 = 0+x
			paths.append(1)
		else:
			z7 = z7+x
			k0 = k0+4
			x = 4+x
			paths.append(2)
		if x < 5:
			z7 = z7-z7
			z7 = 1*3
			paths.append(3)
		else:
			z7 = z7+k0
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