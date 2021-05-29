import numpy as np 

def function(x):

	l4 = 8
	z4 = 7
	paths = []
	try:
		if x < 8:
			z4 = l4*l4
			l4 = 2+z4
			paths.append(1)
		else:
			z4 = 2/z4
			paths.append(2)
		if l4 > 1:
			l4 = l4*7
			paths.append(3)
		else:
			l4 = 2+l4
			x = z4*x
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