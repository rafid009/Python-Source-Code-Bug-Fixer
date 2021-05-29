import numpy as np 

def function(x):

	n1 = x
	z8 = x
	paths = []
	try:
		if n1 >= 3:
			z8 = n1+z8
			paths.append(1)
		else:
			n1 = 5*2
			paths.append(2)
		if x <= 3:
			n1 = 9/z8
			z8 = z8/7
			z8 = z8-n1
			paths.append(3)
		else:
			x = x+3
			n1 = 6-x
			n1 = 6/n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))