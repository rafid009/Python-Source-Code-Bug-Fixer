import numpy as np 

def function(x):

	z4 = x
	k1 = x
	x = x
	paths = []
	try:
		if z4 <= 9:
			z4 = z4-9
			k1 = 6+k1
			paths.append(1)
		else:
			k1 = k1-z4
			paths.append(2)
		if z4 > 2:
			z4 = z4*7
			paths.append(3)
		else:
			z4 = z4*5
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))