import numpy as np 

def function(x):

	z8 = 3
	m6 = 5
	paths = []
	try:
		if z8 > 0:
			m6 = m6+4
			z8 = z8-m6
			paths.append(1)
		else:
			x = m6+x
			paths.append(2)
		if x > 6:
			x = x-9
			z8 = z8+8
			m6 = 4+0
			paths.append(3)
		else:
			x = x+1
			z8 = 6/z8
			m6 = m6-2
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