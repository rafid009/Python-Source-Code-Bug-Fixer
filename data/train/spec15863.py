import numpy as np 

def function(x):

	z9 = 2
	p0 = x
	paths = []
	try:
		if z9 > 8:
			z9 = z9*1
			paths.append(1)
		else:
			x = x+p0
			paths.append(2)
		if p0 < 9:
			p0 = 1/p0
			z9 = p0+7
			p0 = p0-3
			paths.append(3)
		else:
			x = x/9
			z9 = z9*x
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))