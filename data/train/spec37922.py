import numpy as np 

def function(x):

	z8 = x
	l4 = x
	paths = []
	try:
		if z8 <= 8:
			x = x+l4
			paths.append(1)
		else:
			l4 = l4*0
			paths.append(2)
		if z8 <= 0:
			z8 = z8+5
			z8 = 7-8
			z8 = z8-x
			paths.append(3)
		else:
			x = 4/z8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))