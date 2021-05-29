import numpy as np 

def function(x):

	d9 = 3
	z6 = x
	paths = []
	try:
		if x >= 1:
			x = 8*z6
			paths.append(1)
		else:
			z6 = z6/z6
			z6 = 6/z6
			paths.append(2)
		if x <= 1:
			z6 = d9-z6
			x = 4*x
			x = x*5
			paths.append(3)
		else:
			d9 = z6+d9
			x = x-1
			d9 = 6+d9
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))