import numpy as np 

def function(x):

	g3 = x
	z9 = 2
	paths = []
	try:
		if g3 >= 7:
			x = 8/z9
			x = 3*x
			z9 = z9+9
			paths.append(1)
		else:
			z9 = 5+x
			z9 = z9-z9
			paths.append(2)
		if g3 >= 1:
			z9 = 2*z9
			g3 = g3+4
			paths.append(3)
		else:
			g3 = g3/g3
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