import numpy as np 

def function(x):

	z1 = x
	l6 = x
	paths = []
	try:
		if x > 6:
			x = x+z1
			l6 = x+5
			l6 = 3*x
			paths.append(1)
		else:
			x = x-z1
			paths.append(2)
		if z1 > 0:
			z1 = 6+7
			paths.append(3)
		else:
			z1 = 7+z1
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		z1 = l6**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))