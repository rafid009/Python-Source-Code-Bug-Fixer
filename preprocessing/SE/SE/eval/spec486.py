import numpy as np 

def function(x):

	z3 = x
	g1 = x
	paths = []
	try:
		if g1 < 9:
			x = 6*x
			paths.append(1)
		else:
			x = g1*4
			x = z3/x
			z3 = 7-z3
			paths.append(2)
		if g1 <= 8:
			z3 = z3+1
			x = 6+7
			g1 = 5/4
			paths.append(3)
		else:
			z3 = 9/9
			g1 = g1/z3
			g1 = 3-z3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))