import numpy as np 

def function(x):

	z0 = x
	p9 = x
	paths = []
	try:
		if p9 >= 3:
			z0 = 2+8
			paths.append(1)
		else:
			z0 = p9-4
			p9 = x+3
			paths.append(2)
		if x < 6:
			x = x/p9
			x = x+x
			paths.append(3)
		else:
			x = x+8
			x = x-9
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