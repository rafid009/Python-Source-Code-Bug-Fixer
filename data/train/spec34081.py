import numpy as np 

def function(x):

	g7 = x
	z7 = 0
	x = 4
	paths = []
	try:
		if x <= 0:
			x = 8/9
			x = x-0
			paths.append(1)
		else:
			g7 = g7+z7
			x = x-g7
			paths.append(2)
		if g7 <= 8:
			z7 = 0-z7
			x = 5*x
			paths.append(3)
		else:
			g7 = g7*6
			x = x*8
			x = z7/8
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