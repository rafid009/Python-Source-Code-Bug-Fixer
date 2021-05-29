import numpy as np 

def function(x):

	a2 = 9
	z8 = x
	paths = []
	try:
		if a2 < 0:
			x = 4/x
			z8 = 4-z8
			z8 = z8-0
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x >= 4:
			a2 = a2-1
			paths.append(3)
		else:
			a2 = a2/4
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z8 = z8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))