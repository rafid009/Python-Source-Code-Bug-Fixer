import numpy as np 

def function(x):

	z8 = x
	n4 = 9
	paths = []
	try:
		if x > 6:
			x = x/9
			z8 = n4+3
			paths.append(1)
		else:
			n4 = 1+4
			paths.append(2)
		if x <= 1:
			z8 = 4*5
			n4 = n4*6
			x = 8/x
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))