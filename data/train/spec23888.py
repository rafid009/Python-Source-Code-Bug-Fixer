import numpy as np 

def function(x):

	c3 = x
	z3 = 4
	paths = []
	try:
		if z3 >= 3:
			c3 = c3+3
			c3 = z3/c3
			paths.append(1)
		else:
			x = x+0
			c3 = 1/c3
			z3 = 3/1
			paths.append(2)
		if z3 <= 5:
			z3 = z3+3
			z3 = 4-z3
			paths.append(3)
		else:
			x = x*x
			c3 = c3+x
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