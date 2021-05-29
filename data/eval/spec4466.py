import numpy as np 

def function(x):

	z2 = x
	h2 = 0
	paths = []
	try:
		if x < 8:
			z2 = z2-6
			z2 = z2-4
			paths.append(1)
		else:
			z2 = 6/z2
			paths.append(2)
		if x <= 2:
			x = x+3
			h2 = h2/5
			paths.append(3)
		else:
			z2 = z2+6
			z2 = z2-z2
			h2 = 3*h2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))