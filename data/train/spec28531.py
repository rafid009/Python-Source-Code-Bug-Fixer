import numpy as np 

def function(x):

	z3 = x
	l7 = x
	paths = []
	try:
		if z3 > 6:
			z3 = z3*x
			z3 = x-z3
			paths.append(1)
		else:
			l7 = 6/l7
			x = x/5
			paths.append(2)
		if z3 >= 7:
			z3 = z3*z3
			paths.append(3)
		else:
			x = x*0
			z3 = z3*x
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))