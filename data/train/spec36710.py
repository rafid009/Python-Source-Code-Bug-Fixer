import numpy as np 

def function(x):

	z1 = x
	g5 = x
	paths = []
	try:
		if g5 > 9:
			z1 = 3*z1
			g5 = g5+g5
			paths.append(1)
		else:
			x = x+7
			x = x/x
			z1 = g5*x
			paths.append(2)
		if x < 1:
			g5 = 5/g5
			paths.append(3)
		else:
			g5 = x*3
			z1 = 2-5
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))