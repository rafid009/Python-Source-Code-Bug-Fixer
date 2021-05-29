import numpy as np 

def function(x):

	b5 = 8
	z0 = 5
	x = x
	paths = []
	try:
		if b5 <= 6:
			x = 1*2
			b5 = 7/x
			b5 = b5/2
			paths.append(1)
		else:
			b5 = b5*x
			z0 = z0/x
			paths.append(2)
		if z0 < 8:
			z0 = 8+x
			z0 = 4-z0
			paths.append(3)
		else:
			z0 = 8-z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))