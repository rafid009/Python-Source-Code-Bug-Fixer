import numpy as np 

def function(x):

	g4 = 0
	z2 = 2
	paths = []
	try:
		if z2 <= 4:
			z2 = 6-8
			z2 = 5-4
			g4 = g4+g4
			paths.append(1)
		else:
			x = 6/z2
			paths.append(2)
		if g4 >= 1:
			x = g4*x
			paths.append(3)
		else:
			z2 = z2-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))