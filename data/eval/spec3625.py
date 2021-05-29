import numpy as np 

def function(x):

	p3 = x
	z8 = 0
	x = 6
	paths = []
	try:
		if x <= 1:
			z8 = z8-z8
			p3 = 6*x
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x < 2:
			z8 = z8+4
			paths.append(3)
		else:
			z8 = 5*9
			x = 5/z8
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))