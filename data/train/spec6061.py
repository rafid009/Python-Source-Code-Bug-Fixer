import numpy as np 

def function(x):

	z3 = x
	l4 = 9
	paths = []
	try:
		if z3 > 8:
			z3 = l4-6
			x = 9/x
			paths.append(1)
		else:
			x = l4*2
			l4 = 1/l4
			paths.append(2)
		if l4 <= 9:
			l4 = l4/z3
			paths.append(3)
		else:
			z3 = z3*9
			l4 = 1/7
			z3 = z3/7
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))