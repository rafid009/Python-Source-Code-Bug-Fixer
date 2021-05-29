import numpy as np 

def function(x):

	g9 = 2
	z2 = x
	paths = []
	try:
		if x <= 0:
			g9 = 9-z2
			z2 = 6+4
			paths.append(1)
		else:
			z2 = 3-0
			paths.append(2)
		if g9 >= 5:
			x = 7+7
			paths.append(3)
		else:
			g9 = 0*g9
			x = x-4
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