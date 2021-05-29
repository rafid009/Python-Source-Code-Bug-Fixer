import numpy as np 

def function(x):

	d0 = x
	z6 = x
	paths = []
	try:
		if d0 > 3:
			z6 = 3+4
			x = 2+9
			x = x+x
			paths.append(1)
		else:
			z6 = x/1
			d0 = d0+2
			z6 = 2-z6
			paths.append(2)
		if d0 > 1:
			z6 = x-3
			paths.append(3)
		else:
			z6 = 2*z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))