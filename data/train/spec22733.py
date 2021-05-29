import numpy as np 

def function(x):

	m1 = 4
	z8 = x
	paths = []
	try:
		if z8 <= 3:
			x = 9*8
			m1 = m1/z8
			paths.append(1)
		else:
			z8 = 8-7
			z8 = z8*3
			paths.append(2)
		if z8 < 3:
			m1 = x/m1
			z8 = z8/z8
			x = 7-x
			paths.append(3)
		else:
			m1 = m1-x
			z8 = 0+z8
			x = 7*x
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