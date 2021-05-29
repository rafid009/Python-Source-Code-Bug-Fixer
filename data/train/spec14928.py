import numpy as np 

def function(x):

	a0 = x
	z2 = x
	paths = []
	try:
		if z2 < 0:
			z2 = z2*6
			a0 = a0/z2
			a0 = x/a0
			paths.append(1)
		else:
			x = 5+x
			a0 = a0-0
			z2 = 3-z2
			paths.append(2)
		if x >= 1:
			z2 = z2/3
			x = x*z2
			paths.append(3)
		else:
			x = 9-x
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))