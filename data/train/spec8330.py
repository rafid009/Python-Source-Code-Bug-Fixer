import numpy as np 

def function(x):

	u0 = 1
	z3 = 3
	paths = []
	try:
		if z3 > 6:
			x = x+z3
			z3 = x*2
			z3 = z3/2
			paths.append(1)
		else:
			z3 = x-0
			z3 = 6/z3
			x = z3+x
			paths.append(2)
		if u0 <= 9:
			x = x-x
			z3 = 6/z3
			paths.append(3)
		else:
			x = x*x
			x = x/3
			z3 = 6/z3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		u0 = z3**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))