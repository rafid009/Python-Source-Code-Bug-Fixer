import numpy as np 

def function(x):

	a4 = x
	z6 = 0
	paths = []
	try:
		if a4 >= 1:
			z6 = z6/a4
			a4 = 3+7
			paths.append(1)
		else:
			z6 = a4+6
			a4 = 2+a4
			paths.append(2)
		if x <= 6:
			x = 5/x
			z6 = z6-3
			a4 = x-x
			paths.append(3)
		else:
			z6 = 5+z6
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