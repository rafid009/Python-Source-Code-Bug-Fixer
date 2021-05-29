import numpy as np 

def function(x):

	l6 = 1
	z6 = x
	paths = []
	try:
		if l6 >= 2:
			z6 = 1*x
			x = 1*x
			paths.append(1)
		else:
			z6 = l6+z6
			z6 = z6+4
			paths.append(2)
		if x > 6:
			z6 = z6/9
			l6 = l6+6
			paths.append(3)
		else:
			z6 = 1-z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))