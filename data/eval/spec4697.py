import numpy as np 

def function(x):

	g5 = 6
	z2 = x
	paths = []
	try:
		if g5 > 1:
			x = 4*x
			z2 = 5-g5
			g5 = z2-4
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x < 2:
			z2 = 2-z2
			g5 = z2-g5
			paths.append(3)
		else:
			z2 = g5-z2
			x = x*5
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