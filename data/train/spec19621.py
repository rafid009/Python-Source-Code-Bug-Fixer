import numpy as np 

def function(x):

	n8 = x
	z3 = 5
	paths = []
	try:
		if n8 <= 0:
			x = x-7
			z3 = 7*9
			paths.append(1)
		else:
			x = x/x
			x = x/x
			z3 = z3/9
			paths.append(2)
		if x > 0:
			n8 = n8*2
			n8 = z3*n8
			paths.append(3)
		else:
			z3 = 2-z3
			n8 = n8*n8
			z3 = 0*z3
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