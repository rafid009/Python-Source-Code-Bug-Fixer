import numpy as np 

def function(x):

	g9 = x
	z3 = 1
	paths = []
	try:
		if x < 5:
			z3 = z3-8
			paths.append(1)
		else:
			g9 = 5/2
			x = x+6
			g9 = g9-4
			paths.append(2)
		if z3 >= 1:
			z3 = z3/z3
			z3 = 9+x
			g9 = g9/6
			paths.append(3)
		else:
			x = x*6
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