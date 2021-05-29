import numpy as np 

def function(x):

	z7 = 5
	g6 = 0
	paths = []
	try:
		if x < 6:
			g6 = 0*0
			g6 = g6/x
			paths.append(1)
		else:
			g6 = x/3
			paths.append(2)
		if g6 > 3:
			g6 = z7+x
			z7 = z7+x
			paths.append(3)
		else:
			x = x/z7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))