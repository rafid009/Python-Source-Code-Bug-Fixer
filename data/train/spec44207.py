import numpy as np 

def function(x):

	r4 = 7
	z3 = x
	paths = []
	try:
		if r4 >= 3:
			x = x+9
			r4 = 2+r4
			r4 = r4/7
			paths.append(1)
		else:
			z3 = z3-7
			z3 = z3-0
			r4 = r4+z3
			paths.append(2)
		if x < 5:
			r4 = r4-r4
			r4 = z3-0
			paths.append(3)
		else:
			x = r4-x
			z3 = z3*x
			r4 = 8*r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z3 = x**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))