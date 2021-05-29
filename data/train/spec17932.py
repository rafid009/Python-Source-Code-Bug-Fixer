import numpy as np 

def function(x):

	p3 = 7
	z8 = x
	paths = []
	try:
		if z8 <= 4:
			x = 4+8
			paths.append(1)
		else:
			x = 8-x
			z8 = p3*p3
			paths.append(2)
		if p3 <= 8:
			x = x-p3
			z8 = 5/z8
			paths.append(3)
		else:
			p3 = p3-p3
			x = 8/8
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