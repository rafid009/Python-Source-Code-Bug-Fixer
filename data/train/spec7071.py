import numpy as np 

def function(x):

	k0 = 4
	z8 = x
	paths = []
	try:
		if z8 >= 5:
			k0 = 3/3
			paths.append(1)
		else:
			k0 = z8-k0
			paths.append(2)
		if x <= 8:
			z8 = z8+4
			paths.append(3)
		else:
			z8 = 6+1
			k0 = 2*k0
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))