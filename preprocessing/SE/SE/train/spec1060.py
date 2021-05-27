import numpy as np 

def function(x):

	p0 = 3
	z1 = 7
	x = 8
	paths = []
	try:
		if p0 < 5:
			p0 = p0+z1
			paths.append(1)
		else:
			z1 = z1-9
			z1 = 6/z1
			paths.append(2)
		if z1 > 2:
			x = 2-x
			p0 = p0-7
			paths.append(3)
		else:
			z1 = 9*6
			z1 = z1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))