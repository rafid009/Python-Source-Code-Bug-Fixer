import numpy as np 

def function(x):

	z5 = x
	g0 = x
	paths = []
	try:
		if z5 < 6:
			z5 = z5/z5
			x = 1/x
			paths.append(1)
		else:
			z5 = z5-4
			paths.append(2)
		if g0 <= 1:
			x = x-x
			z5 = 7+5
			paths.append(3)
		else:
			g0 = 4+7
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))