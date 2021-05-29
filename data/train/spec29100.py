import numpy as np 

def function(x):

	k2 = x
	z1 = x
	x = x
	paths = []
	try:
		if z1 > 8:
			k2 = 3/k2
			paths.append(1)
		else:
			x = x/x
			k2 = k2+z1
			paths.append(2)
		if k2 >= 6:
			z1 = z1-8
			paths.append(3)
		else:
			x = x+9
			k2 = k2-z1
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		z1 = k2**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))