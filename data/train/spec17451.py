import numpy as np 

def function(x):

	p0 = 0
	z6 = x
	x = x
	paths = []
	try:
		if z6 <= 9:
			p0 = p0*3
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if x > 8:
			z6 = p0*3
			paths.append(3)
		else:
			x = 9*x
			x = x+4
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