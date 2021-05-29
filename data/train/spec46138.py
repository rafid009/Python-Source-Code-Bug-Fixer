import numpy as np 

def function(x):

	r9 = x
	z3 = x
	paths = []
	try:
		if z3 > 4:
			x = 3+8
			r9 = 8/1
			paths.append(1)
		else:
			z3 = z3+9
			x = 7-x
			x = x+3
			paths.append(2)
		if x >= 2:
			z3 = 3*z3
			z3 = z3/x
			paths.append(3)
		else:
			z3 = 4*z3
			x = r9*x
			r9 = z3*r9
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))