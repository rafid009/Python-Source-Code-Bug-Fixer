import numpy as np 

def function(x):

	z2 = 7
	e4 = 7
	paths = []
	try:
		if e4 <= 5:
			e4 = 2*7
			x = x-7
			z2 = z2-z2
			paths.append(1)
		else:
			x = x*e4
			paths.append(2)
		if z2 >= 5:
			z2 = z2/z2
			e4 = e4*2
			paths.append(3)
		else:
			z2 = 1*e4
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