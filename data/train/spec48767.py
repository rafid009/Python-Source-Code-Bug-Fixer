import numpy as np 

def function(x):

	z0 = x
	g9 = x
	paths = []
	try:
		if x >= 6:
			z0 = 9-2
			g9 = g9/3
			paths.append(1)
		else:
			x = 8/6
			x = 2/x
			paths.append(2)
		if x < 3:
			g9 = 4-g9
			paths.append(3)
		else:
			g9 = g9/9
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))