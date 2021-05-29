import numpy as np 

def function(x):

	z3 = x
	a5 = 8
	x = 1
	paths = []
	try:
		if x >= 7:
			z3 = 4*8
			z3 = x/z3
			x = x/1
			paths.append(1)
		else:
			x = x-x
			a5 = z3+a5
			z3 = 7/z3
			paths.append(2)
		if z3 > 5:
			z3 = z3*0
			paths.append(3)
		else:
			a5 = 6/a5
			z3 = 2-z3
			a5 = 0*x
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		a5 = z3**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))