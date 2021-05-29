import numpy as np 

def function(x):

	g6 = x
	z8 = x
	paths = []
	try:
		if x < 9:
			g6 = g6*6
			z8 = g6-z8
			x = 1*x
			paths.append(1)
		else:
			g6 = g6-6
			x = 0-z8
			x = 7+g6
			paths.append(2)
		if g6 <= 5:
			z8 = z8-0
			paths.append(3)
		else:
			x = 2+9
			x = x+x
			x = g6*3
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		z8 = g6**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))