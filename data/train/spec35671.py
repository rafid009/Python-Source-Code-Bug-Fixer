import numpy as np 

def function(x):

	z5 = x
	g3 = x
	paths = []
	try:
		if x <= 8:
			g3 = z5/z5
			paths.append(1)
		else:
			z5 = g3*5
			g3 = g3*7
			paths.append(2)
		if z5 < 4:
			z5 = 5*1
			z5 = z5*z5
			z5 = z5*4
			paths.append(3)
		else:
			z5 = g3-x
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