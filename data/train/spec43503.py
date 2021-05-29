import numpy as np 

def function(x):

	d8 = x
	z3 = 2
	paths = []
	try:
		if z3 < 6:
			d8 = d8-6
			x = x*z3
			x = z3-x
			paths.append(1)
		else:
			d8 = d8*4
			paths.append(2)
		if d8 < 2:
			d8 = z3+3
			z3 = x+x
			z3 = 8+z3
			paths.append(3)
		else:
			d8 = 8/x
			z3 = x*d8
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		z3 = d8**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))