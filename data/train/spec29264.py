import numpy as np 

def function(x):

	z3 = 9
	g2 = x
	paths = []
	try:
		if x <= 5:
			x = g2-0
			paths.append(1)
		else:
			z3 = 7+g2
			paths.append(2)
		if g2 >= 9:
			x = x-g2
			z3 = z3/6
			paths.append(3)
		else:
			z3 = z3-g2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		z3 = g2**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))