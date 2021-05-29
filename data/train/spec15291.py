import numpy as np 

def function(x):

	l0 = x
	z5 = 1
	paths = []
	try:
		if x >= 9:
			x = x/l0
			z5 = z5/x
			z5 = 0+z5
			paths.append(1)
		else:
			z5 = l0+z5
			x = x+z5
			paths.append(2)
		if l0 <= 0:
			z5 = z5+9
			z5 = 0*x
			z5 = 3/3
			paths.append(3)
		else:
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))