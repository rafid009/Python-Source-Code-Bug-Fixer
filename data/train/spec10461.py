import numpy as np 

def function(x):

	z2 = x
	u1 = 3
	paths = []
	try:
		if x >= 8:
			z2 = z2-3
			paths.append(1)
		else:
			z2 = z2-3
			z2 = z2+x
			paths.append(2)
		if x > 8:
			u1 = 0+z2
			z2 = 5+0
			z2 = z2-z2
			paths.append(3)
		else:
			u1 = u1*8
			u1 = z2*u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))