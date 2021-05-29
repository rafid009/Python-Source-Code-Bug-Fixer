import numpy as np 

def function(x):

	z6 = x
	g6 = 8
	x = x
	paths = []
	try:
		if g6 >= 0:
			z6 = x+z6
			x = 8-x
			z6 = z6/4
			paths.append(1)
		else:
			x = 6+x
			z6 = z6*1
			paths.append(2)
		if x <= 5:
			z6 = x-x
			x = 2-x
			z6 = z6-g6
			paths.append(3)
		else:
			x = x*z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))