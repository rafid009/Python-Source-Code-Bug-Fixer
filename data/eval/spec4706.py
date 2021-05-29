import numpy as np 

def function(x):

	e1 = x
	z6 = 6
	paths = []
	try:
		if e1 <= 7:
			x = x+6
			z6 = 8*z6
			z6 = 9-z6
			paths.append(1)
		else:
			e1 = 8-x
			e1 = 2/z6
			paths.append(2)
		if x >= 9:
			e1 = 3+0
			paths.append(3)
		else:
			z6 = z6-4
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