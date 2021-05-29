import numpy as np 

def function(x):

	z3 = 6
	g7 = 5
	paths = []
	try:
		if z3 > 4:
			g7 = 4-g7
			z3 = x*8
			g7 = 7*g7
			paths.append(1)
		else:
			z3 = x/5
			paths.append(2)
		if g7 >= 0:
			g7 = g7+z3
			x = x/1
			paths.append(3)
		else:
			z3 = 8/z3
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))