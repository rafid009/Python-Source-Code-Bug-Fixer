import numpy as np 

def function(x):

	b4 = x
	z8 = 9
	paths = []
	try:
		if x >= 8:
			x = x/b4
			x = x-1
			z8 = 6*z8
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if z8 <= 7:
			x = 9*x
			z8 = b4*5
			paths.append(3)
		else:
			z8 = z8-1
			z8 = z8+z8
			z8 = x+7
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))