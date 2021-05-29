import numpy as np 

def function(x):

	z0 = 2
	b1 = x
	paths = []
	try:
		if b1 <= 5:
			b1 = 3+b1
			paths.append(1)
		else:
			z0 = z0-b1
			x = 6-x
			paths.append(2)
		if b1 > 6:
			z0 = z0-3
			b1 = 7+5
			paths.append(3)
		else:
			b1 = 7/b1
			b1 = b1/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))